"""
Localizzazione di TextAsset CSV dentro un file .assets Unity, senza dipendenze.

Il payload di un TextAsset e' serializzato come:
    int32 nameLen | nome (ASCII) | padding ad allineamento 4
    int32 scriptLen | script (UTF-8, qui con BOM)

Finche' il nuovo payload ha ESATTAMENTE la stessa lunghezza in byte di quello
originale, la sostituzione e' un semplice splice: nessun offset del file si
sposta e le tabelle di intestazione restano valide. Da qui il padding.
"""
import re, struct

BOM = b"\xef\xbb\xbf"
MARKER = re.compile(re.escape(BOM) + rb"Key,")
NAME_RE = re.compile(rb"[A-Za-z0-9_]+\Z")

CATEGORIES = [
    "Attributes", "BuildItems", "Cinematics", "Codex", "Equipment", "Errors",
    "InScene", "Items", "NPCDialogues", "POIMarkers", "Passives", "Quests",
    "Skills", "Spells", "Tutorials", "UI",
]


class TextAssetSlot:
    __slots__ = ("name", "len_off", "payload_off", "size", "lang")

    def __init__(self, name, len_off, payload_off, size, lang):
        self.name, self.len_off = name, len_off
        self.payload_off, self.size, self.lang = payload_off, size, lang

    def payload(self, data):
        return data[self.payload_off:self.payload_off + self.size]

    def __repr__(self):
        return f"<{self.name}/{self.lang} @{self.payload_off} {self.size}B>"


def sniff_language(payload):
    """Identifica la lingua di un payload CSV. Euristica, ma sufficiente:
    ci serve solo distinguere UNA copia per categoria."""
    try:
        t = payload.decode("utf-8", "replace")
    except Exception:
        return "?"
    head = t[:200000]
    scripts = [
        ("Vietnamese", "ạảấầệộứườ"),
        ("Russian", "абвгдежзий"),
        ("Japanese", "のするですを"),
        ("Korean", "니다습의"),
        ("Chinese", "的是你我們们"),
    ]
    for name, chars in scripts:
        if sum(head.count(c) for c in chars) > 15:
            return name
    # pseudo-localizzazione: valori racchiusi fra parentesi quadre
    lines = head.split("\n")[1:400]
    bracketed = sum(1 for ln in lines if ln.count(',[') or ',"[' in ln)
    if lines and bracketed > len(lines) * 0.5:
        return "Pseudo"
    latin = {
        "German": (" der ", " und ", " die ", " Ihr ", "ß"),
        "Spanish": (" el ", " los ", " que ", " una ", "¿", "ñ"),
        "Portuguese": (" você ", " não ", " uma ", "ção"),
        "Italian": (" il ", " gli ", " che ", " per ", " della "),
        "English": (" the ", " you ", " and ", " your "),
    }
    best, score = "?", 0
    for name, toks in latin.items():
        v = sum(head.count(tok) for tok in toks)
        if v > score:
            best, score = name, v
    return best


def scan(data):
    """Trova tutti i TextAsset CSV nel file .assets."""
    slots = []
    for m in MARKER.finditer(data):
        bom = m.start()
        if bom < 8:
            continue
        len_off = bom - 4
        size = struct.unpack_from("<i", data, len_off)[0]
        if not (16 < size < 64 * 1024 * 1024) or bom + size > len(data):
            continue
        name = None
        for back in range(1, 48):
            p = len_off - back
            if p < 4:
                break
            nlen = struct.unpack_from("<i", data, p)[0]
            if 1 <= nlen <= 40 and p + 4 + nlen <= len_off and len_off - (p + 4 + nlen) < 4:
                cand = data[p + 4:p + 4 + nlen]
                if NAME_RE.match(cand):
                    name = cand.decode()
                    break
        if name is None:
            continue
        payload = data[bom:bom + size]
        slots.append(TextAssetSlot(name, len_off, bom, size, sniff_language(payload)))
    return slots


def pick_slots(slots, lang, categories=CATEGORIES):
    """Una copia per categoria per la lingua data. Errore se ambigua o assente."""
    out, problems = {}, []
    for cat in categories:
        found = [s for s in slots if s.name == cat and s.lang == lang]
        if len(found) == 1:
            out[cat] = found[0]
        elif not found:
            problems.append(f"{cat}: nessuno slot {lang}")
        else:
            problems.append(f"{cat}: {len(found)} slot {lang} (ambiguo)")
    return out, problems


MIN_PAD_ROW = len('_ITPAD_000001,""\r\n')


def pad_csv(payload, target):
    """Allunga un payload CSV fino a 'target' byte esatti, con righe inerti.

    Le righe di padding hanno chiavi uniche mai interrogate dal gioco: finiscono
    nel dizionario come voci morte e non alterano nessun testo visibile.
    """
    if len(payload) == target:
        return payload
    if len(payload) > target:
        raise ValueError(f"payload {len(payload)}B > slot {target}B")
    if not payload.endswith(b"\r\n"):
        payload += b"\r\n"
    if len(payload) > target:
        raise ValueError("payload eccede lo slot dopo la newline finale")
    out = bytearray(payload)
    i = 0
    # righe intere finche' ne resta spazio per almeno una
    while target - len(out) >= 2 * MIN_PAD_ROW:
        i += 1
        out += f'_ITPAD_{i:06d},""\r\n'.encode()
    deficit = target - len(out)
    if deficit:
        if deficit < MIN_PAD_ROW:
            # assorbe il resto allungando il valore dell'ultima riga di padding
            if i == 0:
                raise ValueError(
                    f"margine troppo piccolo ({deficit}B) per il padding")
            out = out[:-len(f'_ITPAD_{i:06d},""\r\n'.encode())]
            deficit = target - len(out) - MIN_PAD_ROW
            out += f'_ITPAD_{i:06d},"{"." * deficit}"\r\n'.encode()
        else:
            i += 1
            fill = deficit - MIN_PAD_ROW
            out += f'_ITPAD_{i:06d},"{"." * fill}"\r\n'.encode()
    assert len(out) == target, (len(out), target)
    return bytes(out)


def splice(data, slot, new_payload):
    """Sostituisce il payload di uno slot. Richiede lunghezza identica."""
    if len(new_payload) != slot.size:
        raise ValueError(
            f"{slot.name}: {len(new_payload)}B != {slot.size}B dello slot")
    return data[:slot.payload_off] + new_payload + data[slot.payload_off + slot.size:]

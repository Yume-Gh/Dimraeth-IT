"""Estrae i CSV di localizzazione da sharedassets1.assets in source/<lingua>/.

Sola lettura sul gioco: non scrive nulla nella cartella di installazione.
    python tools/extract.py --game "E:/Games/Steam/steamapps/common/Dimraeth"
    python tools/extract.py --lang English Russian      # solo alcune
"""
import argparse, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unityfile as uf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", required=True, help="cartella di installazione")
    ap.add_argument("--lang", nargs="*", default=["English"],
                    help="lingue da estrarre, oppure 'all'")
    ap.add_argument("--out", default=os.path.join(ROOT, "source"))
    a = ap.parse_args()

    assets = os.path.join(a.game, "Dimraeth_Data", "sharedassets1.assets")
    if not os.path.isfile(assets):
        sys.exit(f"non trovato: {assets}")

    data = open(assets, "rb").read()
    slots = uf.scan(data)
    print(f"{len(slots)} TextAsset CSV trovati in sharedassets1.assets")

    by_lang = collections.defaultdict(list)
    for s in slots:
        by_lang[s.lang].append(s)
    print("\nslot per lingua:")
    for lg in sorted(by_lang):
        cats = collections.Counter(s.name for s in by_lang[lg])
        dup = {k: v for k, v in cats.items() if v > 1}
        note = f"  ATTENZIONE duplicati: {dup}" if dup else ""
        print(f"  {lg:12s} {len(by_lang[lg]):3d} slot, {len(cats):2d} categorie{note}")

    wanted = sorted(by_lang) if a.lang == ["all"] else a.lang
    print()
    for lg in wanted:
        if lg not in by_lang:
            print(f"  {lg}: assente, salto")
            continue
        d = os.path.join(a.out, lg)
        os.makedirs(d, exist_ok=True)
        # se una categoria ha piu' copie nella stessa lingua tiene la piu' grande
        best = {}
        for s in by_lang[lg]:
            if s.name not in uf.CATEGORIES:
                continue
            if s.name not in best or s.size > best[s.name].size:
                if s.name in best:
                    print(f"    {s.name}: 2 copie {lg}, tengo la piu' grande")
                best[s.name] = s
        n = 0
        for name, s in best.items():
            with open(os.path.join(d, name + ".csv"), "wb") as f:
                f.write(s.payload(data))
            n += 1
        print(f"  {lg}: {n} file -> {os.path.relpath(d, ROOT)}")


if __name__ == "__main__":
    main()

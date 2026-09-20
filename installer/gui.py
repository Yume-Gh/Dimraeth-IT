# -*- coding: utf-8 -*-
"""Finestra dell'installer della traduzione italiana di Dimraeth.

Il lavoro vero sta in core.py. Qui c'e' solo la finestra, e una regola:
l'installazione gira in un thread, perche' il file del gioco pesa 283 MB e una
finestra che si congela per cinque secondi sembra una finestra che si e'
piantata.
"""
import os
import sys
import threading
import tkinter as tk
import tkinter.font as tkfont
import webbrowser
from tkinter import filedialog, messagebox, ttk

import core

TITOLO = "Traduzione italiana di Dimraeth"
COLORI = {
    "installata": "#1a7f37",
    "originale": "#57606a",
    "aggiornato": "#9a6700",
    "assente": "#cf222e",
    "errore": "#cf222e",
}


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITOLO)
        self.resizable(False, False)
        self._lavoro = False
        self._costruisci()
        self.after(100, self._cerca_gioco)

    # ------------------------------------------------------------ finestra --
    def _costruisci(self):
        pad = {"padx": 16}
        testa = tk.Frame(self)
        testa.pack(fill="x", pady=(16, 2), **pad)
        tk.Label(testa, text=TITOLO, font=("Segoe UI", 13, "bold"),
                 anchor="w").pack(side="left")
        self._icona_steam(testa)
        tk.Label(self, text="Sostituisce i testi russi del gioco con quelli italiani.",
                 fg="#57606a", anchor="w").pack(fill="x", pady=(0, 14), **pad)

        tk.Label(self, text="Cartella del gioco", anchor="w",
                 font=("Segoe UI", 9, "bold")).pack(fill="x", **pad)
        riga = tk.Frame(self)
        riga.pack(fill="x", pady=(2, 2), **pad)
        self.var_path = tk.StringVar()
        self.entry = tk.Entry(riga, textvariable=self.var_path, width=58)
        self.entry.pack(side="left", fill="x", expand=True)
        self.btn_sfoglia = tk.Button(riga, text="Sfoglia...", width=10,
                                     command=self._sfoglia)
        self.btn_sfoglia.pack(side="left", padx=(8, 0))
        self.var_path.trace_add("write", lambda *_: self._aggiorna_stato())

        self.lbl_trovata = tk.Label(self, text="", fg="#57606a", anchor="w")
        self.lbl_trovata.pack(fill="x", pady=(0, 12), **pad)

        self.lbl_stato = tk.Label(self, text="", anchor="w",
                                  font=("Segoe UI", 9, "bold"), wraplength=520,
                                  justify="left")
        self.lbl_stato.pack(fill="x", pady=(0, 14), **pad)

        bottoni = tk.Frame(self)
        bottoni.pack(pady=(0, 14))
        self.btn_install = tk.Button(bottoni, text="Installa la traduzione",
                                     width=24, height=2, command=self._installa)
        self.btn_install.pack(side="left", padx=6)
        self.btn_uninstall = tk.Button(bottoni, text="Rimuovi", width=14,
                                       height=2, command=self._rimuovi)
        self.btn_uninstall.pack(side="left", padx=6)

        self.barra = ttk.Progressbar(self, length=520, mode="determinate")
        self.barra.pack(**pad)
        self.lbl_prog = tk.Label(self, text="Pronto.", fg="#57606a", anchor="w")
        self.lbl_prog.pack(fill="x", pady=(2, 10), **pad)

        tk.Frame(self, height=1, bg="#d0d7de").pack(fill="x", **pad)
        self._piede(pad)

    def _piede(self, pad):
        """versione  ·  traduzione di Yume  ·  non ufficiale

        'Yume' e' un Label, non un Button: sembra un collegamento perche' lo e',
        e apre il profilo Steam nel browser predefinito.
        """
        piede = tk.Frame(self)
        piede.pack(fill="x", pady=(6, 12), **pad)
        grigio = "#8c959f"
        tk.Label(piede, text="versione %s  ·  traduzione di " % core.VERSION,
                 fg=grigio).pack(side="left")

        link = tk.Label(piede, text=core.AUTORE, fg="#0969da", cursor="hand2",
                        font=tkfont.Font(family="Segoe UI", size=9,
                                         weight="bold", underline=True))
        link.pack(side="left")
        link.bind("<Button-1>", lambda _e: self._apri(core.AUTORE_URL))
        link.bind("<Enter>", lambda _e: link.config(fg="#0a3069"))
        link.bind("<Leave>", lambda _e: link.config(fg="#0969da"))

        tk.Label(piede, text="  ·  non ufficiale", fg=grigio).pack(side="left")

    def _apri(self, url):
        try:
            webbrowser.open(url)
        except Exception:
            messagebox.showinfo(TITOLO, "Non riesco ad aprire il browser."
                                + chr(10) * 2 + url)

    def _icona_steam(self, parent):
        """Pastiglia con il marchio Steam, disegnata invece che impacchettata.

        Un Canvas evita di portarsi dietro un PNG e resta nitido a qualsiasi
        scalatura dello schermo. Apre la pagina del gioco sullo store.
        """
        lato = 22
        c = tk.Canvas(parent, width=lato, height=lato, highlightthickness=0,
                      bd=0, cursor="hand2", bg=self.cget("bg"))
        c.pack(side="left", padx=(8, 0))

        def disegna(sfondo):
            c.delete("all")
            c.create_oval(1, 1, lato - 1, lato - 1, fill=sfondo, outline="")
            # ruota grande in alto a destra, con il mozzo
            c.create_oval(9, 4, 18, 13, outline="white", width=1.6)
            c.create_oval(12, 7, 15, 10, fill="white", outline="")
            # biella verso il pistone in basso a sinistra
            c.create_line(13.5, 8.5, 7.5, 14.5, fill="white", width=1.8)
            c.create_oval(4, 11, 11, 18, fill="white", outline="")
            c.create_oval(6.5, 13.5, 8.5, 15.5, fill=sfondo, outline="")

        disegna("#171a21")
        c.bind("<Button-1>", lambda _e: self._apri(core.GIOCO_URL))
        c.bind("<Enter>", lambda _e: disegna("#1b2838"))
        c.bind("<Leave>", lambda _e: disegna("#171a21"))

    # -------------------------------------------------------------- ricerca --
    def _cerca_gioco(self):
        g = core.find_game()
        if g:
            self.var_path.set(g)
            self.lbl_trovata.config(text="trovata automaticamente tramite Steam",
                                    fg="#1a7f37")
        else:
            self.lbl_trovata.config(
                text="non l'ho trovata da solo: indicala con «Sfoglia»", fg="#9a6700")
            self._aggiorna_stato()

    def _sfoglia(self):
        d = filedialog.askdirectory(title="Scegli la cartella di Dimraeth",
                                    initialdir=self.var_path.get() or "/")
        if d:
            d = os.path.normpath(d)
            # cortesia: se indicano Dimraeth_Data o la cartella Steam, si aggiusta
            if os.path.basename(d).lower() == "dimraeth_data":
                d = os.path.dirname(d)
            if not core.is_game_folder(d):
                for sub in ("Dimraeth", os.path.join("steamapps", "common", "Dimraeth")):
                    if core.is_game_folder(os.path.join(d, sub)):
                        d = os.path.join(d, sub)
                        break
            self.var_path.set(d)
            self.lbl_trovata.config(text="")

    # ---------------------------------------------------------------- stato --
    def _aggiorna_stato(self):
        if self._lavoro:
            return
        g = self.var_path.get().strip()
        if not g:
            self.lbl_stato.config(text="Indica la cartella del gioco.", fg="#57606a")
            self._abilita(False, False)
            return
        stato, testo = core.status(g)
        self.lbl_stato.config(text=testo, fg=COLORI.get(stato, "#24292f"))
        if stato == "installata":
            self.btn_install.config(text="Reinstalla")
            self._abilita(True, True)
        elif stato == "originale":
            self.btn_install.config(text="Installa la traduzione")
            self._abilita(True, os.path.exists(core.rel_paths(g)[0] + core.BAK))
        elif stato == "aggiornato":
            self.btn_install.config(text="Installa la traduzione")
            self._abilita(False, False)
        else:
            self._abilita(False, False)

    def _abilita(self, inst, uninst):
        self.btn_install.config(state="normal" if inst else "disabled")
        self.btn_uninstall.config(state="normal" if uninst else "disabled")

    # ------------------------------------------------------------- lavoro ---
    def _progress(self, pct, testo):
        self.after(0, lambda: (self.barra.config(value=pct),
                               self.lbl_prog.config(text=testo)))

    def _lancia(self, funzione, nome):
        g = self.var_path.get().strip()
        self._lavoro = True
        self._abilita(False, False)
        self.btn_sfoglia.config(state="disabled")
        self.entry.config(state="disabled")
        self.barra.config(value=0)

        def worker():
            try:
                esito = funzione(g, self._progress)
                self.after(0, lambda: self._finito(nome, esito, None))
            except core.Problema as e:
                self.after(0, lambda: self._finito(nome, None, str(e)))
            except Exception as e:
                self.after(0, lambda: self._finito(
                    nome, None, "Errore imprevisto:\n\n%s: %s" % (type(e).__name__, e)))

        threading.Thread(target=worker, daemon=True).start()

    def _finito(self, nome, esito, errore):
        self._lavoro = False
        self.btn_sfoglia.config(state="normal")
        self.entry.config(state="normal")
        if errore:
            self.barra.config(value=0)
            self.lbl_prog.config(text="Non fatto.")
            messagebox.showerror(TITOLO, errore)
        elif nome == "install":
            self.lbl_prog.config(text="Installazione completata.")
            nl = chr(10) * 2
            messagebox.showinfo(
                TITOLO,
                "Traduzione installata." + nl
                + "Nel gioco: Impostazioni → Lingua → «%s»." % esito["voce"]
                + nl
                + "Il gioco originale e' stato salvato: riapri questo "
                  "programma e premi «Rimuovi» per tornare indietro.")
            self.destroy()      # l'utente ha finito: non farglielo chiudere a mano
            return
        else:
            self.lbl_prog.config(text="Traduzione rimossa.")
            messagebox.showinfo(TITOLO, "Gioco riportato alla versione originale.")
        self._aggiorna_stato()

    def _installa(self):
        self._lancia(core.install, "install")

    def _rimuovi(self):
        if messagebox.askyesno(TITOLO, "Rimuovo la traduzione e rimetto i "
                                       "file originali del gioco?"):
            self._lancia(core.uninstall, "uninstall")


def main():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)   # niente finestra sfocata
    except Exception:
        pass
    App().mainloop()


def selftest():
    """Diagnosi: verifica che il pacchetto dentro l'exe sia completo.

        Dimraeth-IT-Setup.exe --selftest

    Serve a chi costruisce il pacchetto, non a chi lo installa.
    """
    import glob
    righe = ["frozen: %s" % getattr(sys, "frozen", False),
             "base:   %s" % core.BASE,
             "payload:%s" % core.payload_dir()]
    csvs = sorted(glob.glob(os.path.join(core.payload_dir(), "*.csv")))
    righe.append("CSV trovati: %d/16" % len(csvs))
    tot = sum(os.path.getsize(f) for f in csvs)
    righe.append("byte totali: %d" % tot)
    mancanti = [c for c in core.uf.CATEGORIES
                if not os.path.isfile(os.path.join(core.payload_dir(), c + ".csv"))]
    righe.append("mancanti: %s" % (", ".join(mancanti) or "nessuno"))
    g = core.find_game()
    righe.append("autore: %s <%s>" % (core.AUTORE, core.AUTORE_URL))
    righe.append("gioco: %s" % g)
    righe.append("stato: %s" % ((core.status(g),) if g else ("non trovato",)))
    testo = chr(10).join(righe)
    with open(os.path.join(os.path.dirname(sys.executable
                                           if getattr(sys, "frozen", False)
                                           else __file__), "selftest.txt"),
              "w", encoding="utf-8") as f:
        f.write(testo)
    print(testo)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()

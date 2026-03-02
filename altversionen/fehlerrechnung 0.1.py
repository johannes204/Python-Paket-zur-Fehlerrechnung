# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 12:01:09 2025

@author: johan
"""

def fehlerklammern(wert, fehler,signifikante_stellen=1, dezimaltrennzeichen=","):
    import numpy as np
    if fehler <= 0:
        return f"{wert}({fehler})"
    
    # Bestimmen der Dezimalstellen, basierend auf dem Fehler
    stelle = max(0, -int(np.floor(np.log10(fehler))))+ (signifikante_stellen - 1)  # Verhindert negative Dezimalstellen
    # Runden der Werte auf die korrekte Anzahl der Dezimalstellen
    gerundet_fehler = round(fehler, stelle)
    gerundet_wert = round(wert, stelle)
    
    # Fehlerziffern extrahieren
    if "." in f"{gerundet_fehler:.{stelle}f}":
        fehler_ziffern = int(f"{gerundet_fehler:.{stelle}f}".split(".")[1])
    else:
        fehler_ziffern = "fehler"  # oder setze einen Standardwert für den Fehler
    
    # Formatierung des Werts und Fehler mit gewünschtem Trennzeichen
    wert_str = f"{gerundet_wert:.{stelle}f}".replace(".", dezimaltrennzeichen)
    
    # Rückgabe im gewünschten Format
    return f"{wert_str}({fehler_ziffern})"

def gewichteter_mittelwert_alle(werte, fehler):
    werte = list(werte)
    fehler = list(fehler)

    if len(werte) != len(fehler):
        raise ValueError("Die Anzahl der Werte und Fehler muss gleich sein.")

    gewichte = [1 / (u ** 2) for u in fehler]
    gewicht_summe = sum(gewichte)
    
    mittelwert = sum(x * g for x, g in zip(werte, gewichte)) / gewicht_summe
    unsicherheit = (1 / gewicht_summe) ** 0.5

    return mittelwert, unsicherheit
def latex_tabelle(*werte):
    ausgabe = " & ".join(str(wert) for wert in werte) + r" \\"
    print(ausgabe)

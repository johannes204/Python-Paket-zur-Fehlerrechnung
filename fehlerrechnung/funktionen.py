
def fehlerklammern(wert, fehler, signifikante_stellen=2,schreibweise="Klammer", dezimaltrennzeichen=","):
   import numpy as np
   import numbers
   if isinstance(fehler, numbers.Real) and isinstance(wert, numbers.Real):
    datentyp = "Zahl"
    einträge = 1
    wert = [float(wert)]
    fehler = [float(fehler)]

   elif isinstance(fehler, (list, np.ndarray)) and isinstance(wert, (list, np.ndarray)):
       datentyp = "Liste"
       wert = list(wert)
       fehler = list(fehler)
       einträge = len(wert)
       if einträge != len(fehler):
           raise ValueError("Die Listen von Ungenauigkeiten und Werten haben nicht die gleiche Länge")
   
   else:
       raise TypeError("Fehler: wert und fehler haben keinen erwarteten Datentyp, oder sind Liste und Zahl")
   
   ergebnisse=[]
   for i in range(einträge):
      if fehler[i] < 0:
          fehler[i] = abs(fehler[i])
          print("Fehler: Die Ungenauigkeit ist negativ, es wurde der Betrag genommen")
      elif fehler[i] == 0:
          raise ValueError("Fehler: Die Ungenauigkeit ist 0")
      if fehler[i] > abs(wert[i]):
        print("Fehler: Unsicherheit größer als Zahl")
      # Zehnerpotenz der ersten signifikanten Ziffer
      stelle = int(np.floor(np.log10(fehler[i])))
      # Rundungsfaktor
      r = 10**(stelle - signifikante_stellen + 1)
      # Fehler und Wert runden
      gerundet_fehler = round(fehler[i] / r) * r
      gerundet_wert = round(wert[i] / r) * r
      # Anzahl Dezimalstellen für Darstellung
      dezimalstellen = max(-int(np.floor(np.log10(r))), 0)
      
      if schreibweise =="Klammer":
         # Formatiere Strings
         wert_str = f"{gerundet_wert:.{dezimalstellen}f}".replace(".", dezimaltrennzeichen)
         fehler_str = f"{gerundet_fehler:.{dezimalstellen}f}".replace(".", "")
      
         # Hole nur die signifikanten Ziffern des Fehlers (z. B. 0.00056 → "56")
         fehler_ziffern = fehler_str.lstrip("0")
         ergebnisse.append(f"{wert_str}({fehler_ziffern})")
      elif schreibweise == "plusminus":
          format_str = f"{{:.{dezimalstellen}f}}"
          wert_str = format_str.format(gerundet_wert).replace('.', dezimaltrennzeichen)
          fehler_str = format_str.format(gerundet_fehler).replace('.', dezimaltrennzeichen)
          ergebnisse.append(f"{wert_str} ± {fehler_str}")
      else:
         print('Fehlerhafte Angabe für schreibweise, vielleicht meintest du "plusminus" oder die Voreinstellung "Klammer"?')
         ergebnisse.append(None)
   if datentyp=="Zahl":
      return ergebnisse[0]
   else:
      return ergebnisse


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
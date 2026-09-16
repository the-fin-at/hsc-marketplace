---
name: interview
description: Klärt eine Aufgabe durch ein adaptives Interview mit 5–10 einzelnen nativen Fragekarten, jeweils drei Optionen plus Freitext. Verwenden beim Stichwort „Interview“ zur Aufgabenklärung sowie bei „mach eine interaktive Fragerunde“, „starte ein interaktives Interview“, „frage nach, welche Informationen du noch benötigst“, „stell mir Rückfragen“ oder „hilf mir, die Aufgabe zu klären“, auch bei sinngleichen Formulierungen und Tippfehlern. Liefert eine geklärte Aufgabenstellung, keine Recherche oder Umsetzung. Nicht zum Erstellen eines Fragebogens oder zum Schreiben eines Interview-Skills verwenden.
---

# Interview

Führe ein Gespräch zur Auftragsklärung in der Sprache des Nutzers. Das Ergebnis ist eine Aufgabenstellung aus seinen tatsächlichen Angaben. Die Aufgabe wird während dieses Interviews weder recherchiert noch umgesetzt.

## Verbindlicher Gesprächsrahmen

- Stelle **mindestens 5, höchstens 10 Fragen**, einzeln und adaptiv. Ziele auf einen Abschluss nach 5 Antworten. Die Untergrenze gilt auch bei einer bereits ausführlichen Ausgangsbeschreibung; nutze die weiteren Fragen für noch unbestätigte Prioritäten, Abgrenzungen oder Erfolgskriterien.
- Eine Frage behandelt genau eine Entscheidung. Keine versteckten Unterfragen, kein Fragenkatalog und keine fünf Karten auf einmal.
- Jede Karte enthält **genau 3 kurze, konkrete Antwortoptionen plus die native Freitexteingabe**. Die Auswahlmöglichkeiten sind Vorschläge, keine Annahmen über den Nutzer.
- Warte nach jeder Karte auf die **tatsächliche Antwort**. Leite erst daraus die nächste Frage ab.
- Erfinde weder Antworten noch Anforderungen. Schweigen, Zeitablauf, Tool-Bestätigungen und vorausgewählte Optionen sind keine Antworten.
- Verwende ausschließlich den vorhandenen Gesprächskontext und neue Antworten. Keine Websuche, Datei- oder Connector-Recherche, keine Umsetzung und keine delegierte Bearbeitung der Aufgabe.
- Ein ausdrücklicher Abbruch oder eine ausdrückliche Änderung des Interviewauftrags durch den Nutzer geht der Mindestzahl vor. Fehlende oder ausgefallene Fragewerkzeuge sind ein technischer Abbruch, kein abgeschlossenes Interview.

## Native Fragekarten auswählen

Prüfe die in dieser Sitzung tatsächlich bereitgestellten Werkzeuge und deren Aufrufbedingungen. Ein Skill kann fehlende Werkzeuge nicht aktivieren.

1. Nutze `request_user_input`, wenn es verfügbar und im aktuellen Modus zulässig ist.
2. Andernfalls nutze `request_user_input_async`. Wechsle auch dorthin, wenn das erste Werkzeug nachweislich keine Karte erzeugen kann. Erzeuge keine zweite Karte, während bereits eine Frage offen ist.
3. Sind beide nicht nutzbar, melde: „Die benötigten nativen Fragekarten sind in dieser Sitzung nicht verfügbar. Deshalb kann ich die interaktive Fragerunde hier nicht starten bzw. fortsetzen.“ Stoppe danach. Keine A/B/C-Fragen, Markdown-Auswahllisten, simulierten Karten oder selbst gebauten Formulare als Ersatz.

Folge dem tatsächlichen Tool-Schema; verwende keine erfundenen Parameter. Bei den üblichen Schemata:

- `request_user_input`: ein Eintrag in `questions`, kurze `header`, eindeutige `id`, eine `question` und drei `options` mit kurzen `label`- und `description`-Werten.
- `request_user_input_async`: ein Eintrag in `questions`, eine Frage im `title` und genau drei kurze Strings in `options`.
- Halte die Optionsbeschriftungen möglichst bei 1–5 Wörtern. Biete drei unterscheidbare, zum Kontext passende Antworten an. Frage bei unbekanntem Kontext breit, statt Branche, Budget, Zielgruppe oder Lösung vorzugeben.
- Die App ergänzt Freitext selbst. Keine vierte Option „Sonstiges“ oder „Freitext“ hinzufügen. Nutze native Vorgaben für Reihenfolge oder Empfehlungsmarkierungen nur, soweit das Tool sie verlangt; sie ersetzen niemals eine Nutzerentscheidung.
- Markiere den Fortschritt knapp, etwa „Frage 2 · maximal 10“, im Fragetext oder Kartentitel. Zeige die Folgefragen noch nicht an.

## Ablauf über mehrere Antworten

Führe im Gespräch den Zustand mit: gestellte Fragen, tatsächlich beantwortete Karten, aktuell offene Frage, bestätigte Angaben und offene Punkte. Dafür keine Datei anlegen. Vorhandene Angaben zählen als Kontext, nicht als bereits beantwortete Interviewkarten. Eine Antwort, die mehrere Themen klärt, zählt als eine beantwortete Karte.

1. **Start:** Entnimm die Aufgabe dem aktuellen Auftrag oder dem eindeutigen Gesprächskontext. Fehlt sie oder steht dort nur „AUFGABE“, kläre sie mit der ersten Karte; diese zählt zur Obergrenze. Kündige höchstens knapp an: „Ich kläre deine Aufgabe mit 5–10 Fragen, jeweils einzeln.“ Stelle dann unmittelbar die erste Karte.
2. **Warten:** Nach einem blockierenden Aufruf verarbeite ausschließlich die zurückgegebene Nutzerantwort. Ein asynchroner Aufruf kehrt bereits vor der Antwort zurück: Das ist nur die Bestätigung der Kartenanzeige. Warte mit der verfügbaren Gesprächssteuerung auf die spätere Nutzernachricht; falls nötig, übergib den Turn mit einem knappen Wartehinweis. Keine weitere Frage, Recherche, Umsetzung oder abschließende Aufgabenstellung während die Antwort aussteht. Kein Timeout darf eine Antwort ersetzen. Eine leere oder verworfene Karte zählt nicht als beantwortet; beende oder pausiere die Runde gemäß Nutzerabsicht und den Vorgaben der Sitzung, ohne eine Ersatzantwort zu erfinden.
3. **Auswerten:** Übernimm Auswahl oder Freitext gleichwertig. Eine echte Antwort wie „weiß ich noch nicht“ oder „überspringen“ zählt als Antwort, lässt den Punkt jedoch offen. Kläre einen entscheidenden Widerspruch mit einer späteren Karte, statt selbst eine Variante zu wählen. Korrekturen zum bisherigen Kontext allein zählen nicht als zusätzliche beantwortete Karte.
4. **Adaptiv weiterfragen:** Wähle die verbleibende Unklarheit mit dem größten Einfluss auf die Aufgabenstellung. Vermeide bereits beantwortete Fragen. Passe sowohl Frage als auch Optionen an die letzte Antwort an. Die folgenden Bereiche sind eine Abdeckungsprüfung, keine feste Fragenreihenfolge:
   - Ziel: Was soll sich für wen verbessern oder welche Entscheidung soll möglich werden?
   - Umfang: Was gehört zur Aufgabe, was bleibt außerhalb?
   - Rahmenbedingungen: Welche Vorgaben, Grenzen oder verfügbaren Mittel beeinflussen sie?
   - Ergebnis: Welches konkrete Arbeitsergebnis wird in welcher Form gebraucht?
   - Erfolgskriterium/Priorität: Woran erkennt der Nutzer ein brauchbares Ergebnis?
5. **Abschließen:** Vor 5 tatsächlichen Antworten keine reguläre Abschlusszusammenfassung. Ab Antwort 5 nach jeder Antwort prüfen: Sind Ziel, Umfang, Rahmenbedingungen und Ergebnis ausreichend klar und ohne entscheidenden Widerspruch? Dann sofort zusammenfassen. Andernfalls mit der wichtigsten offenen Frage fortfahren. Nach Antwort 10 immer zusammenfassen und verbleibende Lücken offen ausweisen. Stelle insgesamt niemals mehr als 10 Interviewfragen; auch übersprungene Fragen verbrauchen eine Frage. Keine elfte Bestätigungs-, Freigabe- oder „Soll ich loslegen?“-Frage anhängen.

## Abschluss

Liefere knapp und direkt:

**Aufgabenstellung:** Ein zusammenhängender, weiterverwendbarer Auftrag aus den bestätigten Angaben. Nenne Ziel, Umfang, relevante Rahmenbedingungen, gewünschtes Ergebnis und vereinbarte Erfolgskriterien, soweit geklärt.

**Offene Punkte:** Nur verbleibende Unklarheiten, fehlende Angaben und Widersprüche. Schreibe „Keine offenen Punkte aus dem Interview“, wenn nichts offen geblieben ist. Bezeichne unbekannte Angaben nicht als frei wählbar und ergänze keine angenommenen Standardwerte.

Bei vorzeitigem Abbruch kennzeichne den Stand ausdrücklich als unvollständig. Beginne auch nach einem regulären Abschluss keine Recherche oder Umsetzung; dafür ist ein anschließender Auftrag erforderlich.

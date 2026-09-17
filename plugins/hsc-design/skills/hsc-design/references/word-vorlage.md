# Native Word-Vorlage

Für DOCX-Ausgaben eine Kopie von [HSC-Word-Vorlage.docx](../assets/word/HSC-Word-Vorlage.docx) bearbeiten. Nicht das Original-Styleguide-Dokument als Vorlage verwenden. Die Vorlage enthält keine Kommentare, Bankdaten oder fachlichen Beispielaussagen.

## Aufbau

A4, links/rechts/oben 2,5 cm. Unten sind bewusst 2,8 cm statt der 1 cm aus dem Original vorgesehen, damit die dreizeilige Firmenfußzeile und die zusätzliche automatische Seitenzahl den Textbereich nicht überlagern. Kopf-/Fußzeilenabstand 1 cm; Logo zentriert 37,6 mm. Diese Fußraum-Anpassung ist eine dokumentierte Umsetzung, keine ursprüngliche HSC-Vorgabe.

Word-Formatvorlagen: Title und Heading 1 grün 20 pt Versalien, Heading 2 grau 16 pt Versalien, Heading 3 grau 12 pt fett mit +1 pt Laufweite, Heading 4 grau 10 pt fett. Normal 10 pt, linksbündig, 1,15 Zeilenabstand. `HSC Liste` verwendet einen echten Gedankenstrich als Listenzeichen. Die dreispaltige Beispieltabelle enthält nur Platzhalter, graue 0,75-pt-Linien und eine wiederholte Kopfzeile.

## Bearbeiten

Alle `[[...]]`-Platzhalter ersetzen; nicht benötigte Beispielabsätze, Überschriftenebenen und Tabellen entfernen. Die Formatvorlagen, Kopf-/Fußzeile und Tabellenformatierung erhalten. Längere Inhalte laufen in neue Seiten; Überschriften mit dem Folgeabsatz zusammenhalten. Tabellen dürfen über mehrere Seiten laufen, einzelne Zeilen sollen nicht getrennt werden. Bei Änderung der Spaltenzahl die nutzbaren 16 cm neu aufteilen.

`PAGE` und `NUMPAGES` sind echte Felder. `updateFields` fordert Aktualisierung beim Öffnen an; vor Abgabe Felder im verwendeten Office-/Exportprogramm aktualisieren und Seitenzahlen prüfen.

Montserrat Regular, Italic, SemiBold und SemiBold Italic sind vollständig eingebettet; die Fettrolle verwendet SemiBold. Ob eine Office-Oberfläche eingebettete Fonts unterstützt, hängt vom Client ab. Für Renderer, die sie ignorieren, die mitgelieferten TTF-Dateien sitzungsbezogen laden. Nach jeder Bearbeitung prüfen, ob eingebettete Fontteile und ihre Beziehungen erhalten geblieben sind. Nicht ungeprüft behaupten, dass auf jedem Endgerät dieselbe Schrift erscheint.

Im Zielformat auf jeder Seite Logo, Fußzeile, Seitenzahl, Schrift und Umbrüche visuell prüfen. Montserrat-Lizenz liegt unter `assets/design-system/assets/OFL-Montserrat.txt`.

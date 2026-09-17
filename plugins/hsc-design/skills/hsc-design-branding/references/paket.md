# Paket und Vorlagen

Quelle: HSC_DesignSystem.zip, Design-System-Stand 17.09.2026.
ZIP SHA-256: `bad5d48b1e136d0fdb8edd640f00bc656efec0086ca41c39bc2fa26126affb63`.

`assets/design-system/` enthält alle 19 Originaldateien unverändert, einschließlich der Montserrat-Lizenz. `templates/` ergänzt daraus abgeleitete HTML-Vorlagen mit Platzhaltern. Die zwei Markdown-Referenzen sind Leseauszüge der HTML-Dokumentation; bei Unklarheit dort und in den CSS-Dateien nachsehen.

## Verwendung

- Titel: `templates/slide-titel.html`
- Kapiteltrenner: `templates/slide-trenner.html`
- Inhalte/Boxen/Merksatz: `templates/slide-inhalt.html`
- Prozess/Liste/Hinweis: `templates/slide-prozess.html`
- A4: `templates/document-a4.html`

`[[TEXT_N]]` sind pro Vorlage nummerierte Textplätze, keine Inhaltsvorgaben. Alle befüllen oder das zugehörige optionale Element entfernen; keine leeren Elemente stehen lassen. Überschriften, Zahlen, Datum, Fußzeile und Seitenzahlen aus der tatsächlichen Aufgabe einsetzen. Hochgestellte akademische Titel nur übernehmen, wenn sie tatsächlich vorkommen; sonst die ganze Beispielstruktur durch passenden Text ersetzen.

Die Originale in `slides/`, die PNGs und das Dokument in `index.html` illustrieren Gestaltung. Ihre Befragungszahlen, Projektbezeichnungen, Personen und Termine sind ausdrücklich erfunden. Sie dürfen nicht als Quellen oder Kundeninhalte übernommen werden. Firmenangaben stehen in der Markendokumentation; nicht mit erfundenen Kontaktdaten ergänzen.

## Präzisierungen für die Umsetzung

- Grün: Die 48-px-Untergrenze betrifft Folientext. Für A4-H1 gilt ausdrücklich der dokumentierte Wert 20 pt in Grün. Kleine grüne Mustertexte aus dem Styleguide nicht in Kundenunterlagen kopieren; Beispiele dort kursiv/grau setzen. Keine pauschale Kontrastfreigabe behaupten.
- Das Logo behält seine Originalfarben; seine gemessene Grünfarbe muss nicht dem CSS-Grün entsprechen. Transparente weiße Fußlinien auf dunklen Folien sind im Original-CSS vorgesehen.
- Eine Box-Reihe bzw. Prozessreihe ist ein Layoutblock. Die Prozessdemonstration enthält zusätzlich Liste und Hinweisbox; bei strikter Zwei-Baustein-Regel auf zwei Folien verteilen.
- Raster, Foliengrößen der Schrift und Tints sind teils Vorschläge/abgeleitet, keine bestätigte HSC-Freigabe.
- Das A4-HTML ist eine Einseitenvorlage. Mehrseitige Inhalte brauchen kontrollierte Seitenumbrüche und wiederholte Kopf-/Fußzeilen. Das mitgelieferte Druck-CSS ist keine Garantie für korrekte Paginierung; insbesondere Fußzeile und Textbereich im exportierten PDF prüfen.
- CSS nutzt feste Positionen und teils `overflow:hidden`. Lange Inhalte auf zusätzliche Seiten verteilen; nicht stillschweigend abschneiden oder die Schrift verkleinern.
- Dokument-H3: Textbeschreibung nennt +1 pt Laufweite, CSS verwendet .05em. Für native Dokumente den dokumentierten +1-pt-Wert verwenden; bei HTML die Abweichung nennen, solange das Original-CSS unverändert bleibt.

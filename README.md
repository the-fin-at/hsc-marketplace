# HSC Marketplace

Marketplace für HSC-Skills von THE FIN. Enthält `hsc-productivity` in Version `0.4.0` für Codex und Claude Code sowie `hsc-design` in Version `0.3.0` für Codex.

## Design-Plugin für Codex

`hsc-design` enthält [hsc-design](plugins/hsc-design/skills/hsc-design/SKILL.md) für ChatGPT und Codex: Neusatz vorhandener Unterlagen als Deck oder A4-Dokument im Corporate Design von HÖRHAN Strategy Consultants.

**Design-System enthalten:** alle 19 Originaldateien aus `HSC_DesignSystem.zip` (Stand 17.09.2026), darunter Tokens, CSS-Bausteine, Logo, sechs Montserrat-Schnitte samt Lizenz, HTML-Dokumentation und vier Beispielfolien mit PNG-Vorschauen. Ergänzt sind lesbare Regelreferenzen und fünf HTML-Vorlagen mit Platzhaltern, einschließlich A4. Zusätzlich enthalten: der originale HSC-Styleguide vom 18.02.2026 als unveränderte DOCX und lesbarer Textauszug; er hat bei Regelkonflikten Vorrang vor abgeleiteten Referenzen. Der Skill heißt **HSC Design** (technisch `hsc-design`, zuvor `hsc-design-branding`). Kein Claude-Artifact-Zugriff und kein zusätzlicher Design-Export nötig.

Der Nutzer stellt seine Ausgangsunterlage bereit. Die verwendete Oberfläche muss Dateierzeugung und für die Sichtprüfung Rendering unterstützen. Native Office-Masterdateien sind nicht enthalten; PPTX/DOCX werden aus den Designvorgaben erzeugt und gesondert geprüft. Die Installation und der vollständige Ablauf auf der ChatGPT-Testinstanz müssen noch dort getestet werden.

Nach Veröffentlichung bzw. Aktualisierung des Marketplace:

```sh
codex plugin add hsc-design@hsc-marketplace
```

Beispiel: „Nutze $hsc-design für diese Unterlage. Verwende die mitgelieferten Vorlagen und liefere ein A4-Dokument.“

## Productivity-Plugin

[interview](plugins/hsc-productivity/skills/interview/SKILL.md) klärt eine Aufgabe oder ein Thema mit mindestens 5 und höchstens 10 einzeln gestellten Fragen. Eine ausdrücklich gewünschte Anzahl innerhalb dieses Bereichs wird eingehalten. Jede Frage bietet drei kurze Optionen und die Möglichkeit, frei zu antworten. Der Skill wartet auf echte Antworten, passt die nächste Frage daran an und endet mit der Aufgabenstellung und offenen Punkten. Er recherchiert nicht und setzt die Aufgabe nicht um.

Typische Aufrufe: „Interview“, „Mach eine interaktive Fragerunde“, „Frage nach, welche Informationen du noch benötigst“ oder „Nutze $interview für meine Aufgabe: …“.

Der Skill beginnt direkt mit der ersten Frage. Er nutzt bevorzugt anklickbare Fragekarten und stellt die Fragen andernfalls einzeln im Gespräch. Nach jeder Frage wartet er auf die tatsächliche Antwort.

## Struktur

```text
.agents/plugins/marketplace.json       # Codex-Katalog
.claude-plugin/marketplace.json        # Claude-Code-Katalog
plugins/hsc-productivity/
  .codex-plugin/plugin.json            # Codex-Manifest
  .claude-plugin/plugin.json           # Claude-Code-Manifest
  skills/                             # Hier neue Skills ergänzen
scripts/validate.py                    # Prüfung von Katalogen und Pfaden
.github/workflows/validate.yml         # Prüfung bei Push und Pull Request
plugins/hsc-design/
  .codex-plugin/plugin.json            # Eigenständiges Codex-Design-Plugin
  skills/hsc-design/
    SKILL.md
    agents/openai.yaml
```

## Skills ergänzen

Skills nach Zweck im passenden Plugin ergänzen: `hsc-productivity` für Produktivität, `hsc-design` für Gestaltung. Weitere Themenbereiche können eigene Plugins und Katalogeinträge erhalten. Der gemeinsame Marketplace heißt weiterhin `hsc-marketplace`.

Pro Skill einen eigenen Ordner anlegen: `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`.

Beispiel für den Aufbau einer `SKILL.md`:

```markdown
---
name: hsc-beispiel
description: Beschreibt die konkrete Aufgabe und wann dieser Skill verwendet werden soll.
---

# HSC Beispiel

Hier stehen die Arbeitsanweisungen für den Skill.
```

Optionale Dateien liegen innerhalb des jeweiligen Skill-Ordners in `references/`, `scripts/` oder `assets/`. Neue Skills im bestehenden Plugin benötigen keinen zusätzlichen Katalogeintrag.

Vor einer Veröffentlichung:

1. `python3 scripts/validate.py` ausführen.
2. Die Version des geänderten Plugins erhöhen; bei Plugins für beide Clients beide Manifeste auf dieselbe Version setzen.
3. Änderungen committen und nach GitHub pushen.

Das Repository ist derzeit öffentlich. Eine Open-Source-Lizenz wurde noch nicht vergeben (`UNLICENSED`).

## Installation

Codex:

```sh
codex plugin marketplace add the-fin-at/hsc-marketplace
codex plugin add hsc-productivity@hsc-marketplace
```

Claude Code:

```text
/plugin marketplace add the-fin-at/hsc-marketplace
/plugin install hsc-productivity@hsc-marketplace
```

Das bisherige Plugin `hsc-marketplace` heißt seit Version `0.4.0` `hsc-productivity`. Bereits installierte Exemplare werden durch die Umbenennung nicht automatisch ersetzt: das neue Plugin installieren und anschließend das alte Plugin im jeweiligen Client entfernen. Der Skill-Aufruf `$interview` bleibt gleich.

## Prüfung

```sh
python3 scripts/validate.py
claude plugin validate .
claude plugin validate plugins/hsc-productivity
```

Die automatische Prüfung kontrolliert JSON-Dateien, übereinstimmende Namen und Versionen bei gemeinsamen Plugins, lokale Plugin-Pfade und vorhandene `SKILL.md`-Dateien. Reine Codex-Plugins benötigen keinen Claude-Katalogeintrag. Inhaltliche Tests der späteren Skills sind zusätzlich erforderlich.

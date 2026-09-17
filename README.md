# HSC Marketplace

Grundgerüst für HSC-Skills, veröffentlicht von THE FIN. Enthält Kataloge für Codex und Claude Code sowie das Plugin `hsc-marketplace` in Version `0.3.0`.

## Enthaltener Skill

[interview](plugins/hsc-marketplace/skills/interview/SKILL.md) klärt eine Aufgabe oder ein Thema mit mindestens 5 und höchstens 10 einzeln gestellten Fragen. Eine ausdrücklich gewünschte Anzahl innerhalb dieses Bereichs wird eingehalten. Jede Frage bietet drei kurze Optionen und die Möglichkeit, frei zu antworten. Der Skill wartet auf echte Antworten, passt die nächste Frage daran an und endet mit der Aufgabenstellung und offenen Punkten. Er recherchiert nicht und setzt die Aufgabe nicht um.

Typische Aufrufe: „Interview“, „Mach eine interaktive Fragerunde“, „Frage nach, welche Informationen du noch benötigst“ oder „Nutze $interview für meine Aufgabe: …“.

Der Skill beginnt direkt mit der ersten Frage. Er nutzt bevorzugt anklickbare Fragekarten und stellt die Fragen andernfalls einzeln im Gespräch. Nach jeder Frage wartet er auf die tatsächliche Antwort.

## Struktur

```text
.agents/plugins/marketplace.json       # Codex-Katalog
.claude-plugin/marketplace.json        # Claude-Code-Katalog
plugins/hsc-marketplace/
  .codex-plugin/plugin.json            # Codex-Manifest
  .claude-plugin/plugin.json           # Claude-Code-Manifest
  skills/                             # Hier neue Skills ergänzen
scripts/validate.py                    # Prüfung von Katalogen und Pfaden
.github/workflows/validate.yml         # Prüfung bei Push und Pull Request
```

## Skills ergänzen

Pro Skill einen eigenen Ordner anlegen: `plugins/hsc-marketplace/skills/<skill-name>/SKILL.md`.

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
2. Beide Plugin-Manifeste auf dieselbe neue Version setzen.
3. Änderungen committen und nach GitHub pushen.

Das Repository ist derzeit öffentlich. Eine Open-Source-Lizenz wurde noch nicht vergeben (`UNLICENSED`).

## Installation

Codex:

```sh
codex plugin marketplace add the-fin-at/hsc-marketplace
codex plugin add hsc-marketplace@hsc-marketplace
```

Claude Code:

```text
/plugin marketplace add the-fin-at/hsc-marketplace
/plugin install hsc-marketplace@hsc-marketplace
```

## Prüfung

```sh
python3 scripts/validate.py
claude plugin validate .
claude plugin validate plugins/hsc-marketplace
```

Die automatische Prüfung kontrolliert JSON-Dateien, übereinstimmende Namen und Versionen, lokale Plugin-Pfade und vorhandene `SKILL.md`-Dateien. Inhaltliche Tests der späteren Skills sind zusätzlich erforderlich.

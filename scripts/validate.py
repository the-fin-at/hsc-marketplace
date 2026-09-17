#!/usr/bin/env python3
"""Validate the repository structure with the Python standard library."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def main():
    for path in ROOT.rglob("*.json"):
        if ".git" not in path.parts:
            json.loads(path.read_text(encoding="utf-8"))
    codex = read(".agents/plugins/marketplace.json")
    claude = read(".claude-plugin/marketplace.json")
    require(codex["name"] == claude["name"] == "hsc-marketplace", "Marketplace names differ")
    codex_entries = {entry["name"]: entry for entry in codex["plugins"]}
    claude_entries = {entry["name"]: entry for entry in claude["plugins"]}
    require(len(codex_entries) == len(codex["plugins"]), "Duplicate Codex plugin name")
    require(len(claude_entries) == len(claude["plugins"]), "Duplicate Claude plugin name")
    require(claude_entries.keys() <= codex_entries.keys(), "Claude plugin missing from Codex catalog")
    skill_count = 0
    for name, entry in codex_entries.items():
        require(entry["source"]["source"] == "local", "Expected local plugin source")
        source = entry["source"]["path"]
        require(source == f"./plugins/{name}", "Unexpected plugin path")
        require(entry["policy"]["installation"] in {"AVAILABLE", "NOT_AVAILABLE", "INSTALLED_BY_DEFAULT"}, "Invalid installation policy")
        require(entry["policy"]["authentication"] in {"ON_INSTALL", "ON_USE"}, "Invalid authentication policy")
        require(bool(entry["category"]), "Missing category")
        plugin = ROOT / source
        manifests = [read(f"{source}/.codex-plugin/plugin.json")]
        if name in claude_entries:
            require(source == claude_entries[name]["source"], "Plugin paths differ")
            manifests.append(read(f"{source}/.claude-plugin/plugin.json"))
        else:
            require(not (plugin / ".claude-plugin/plugin.json").exists(), "Claude manifest missing from catalog")
        require(all(item["name"] == name for item in manifests), "Plugin names differ")
        require(all(item["version"] == manifests[0]["version"] for item in manifests), "Plugin versions differ")
        require(re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", manifests[0]["version"]), "Expected x.y.z version")
        require(all(item["skills"] == "./skills/" for item in manifests), "Unexpected skills path")
        skills = plugin / "skills"
        require(skills.is_dir(), "Missing skills directory")
        for skill in skills.iterdir():
            if skill.is_dir() and not skill.name.startswith("."):
                require((skill / "SKILL.md").is_file(), f"Missing SKILL.md: {skill.name}")
                skill_count += 1
    print(f"Structure valid: {len(codex_entries)} plugin(s), {skill_count} skill(s).")


if __name__ == "__main__":
    main()

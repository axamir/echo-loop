import json
import os
from pathlib import Path

def read_md_file(path):
    if not path.exists():
        return ""
    return path.read_text(encoding='utf-8')

def main():
    echoes_root = Path("echoes")
    output = []
    for echo_dir in sorted(echoes_root.glob("*_*")):
        if not echo_dir.is_dir():
            continue
        meta_en = echo_dir / "en" / "meta.json"
        if not meta_en.exists():
            continue
        with open(meta_en, "r", encoding="utf-8") as f:
            meta = json.load(f)
        en_conversation = read_md_file(echo_dir / "en" / "conversation.md")
        fa_conversation = read_md_file(echo_dir / "fa" / "conversation.md")
        en_summary = read_md_file(echo_dir / "en" / "summary.md")
        fa_summary = read_md_file(echo_dir / "fa" / "summary.md")
        en_reflections = read_md_file(echo_dir / "en" / "reflections.md")
        fa_reflections = read_md_file(echo_dir / "fa" / "reflections.md")

        record = {
            "echo_id": meta.get("echo_id", echo_dir.name),
            "date": meta.get("date", ""),
            "title_en": "First Echo: Sending Messages to the Past & the Nature of Time",
            "title_fa": meta.get("title", ""),
            "authors": meta.get("authors", ["Amir Ahmadi"]),
            "ai_model": meta.get("ai_model", "DeepSeek"),
            "tags_en": ["Time", "Quantum", "Causality", "Consciousness", "Free Will"],
            "tags_fa": ["زمان", "کوانتوم", "علیت", "آگاهی", "اراده آزاد"],
            "languages": ["en", "fa"],
            "contact": meta.get("contact", {}),
            "citation": meta.get("citation", {}),
            "open_questions": meta.get("open_questions", []),
            "conversation_en": en_conversation,
            "conversation_fa": fa_conversation,
            "summary_en": en_summary,
            "summary_fa": fa_summary,
            "reflections_en": en_reflections,
            "reflections_fa": fa_reflections
        }
        output.append(record)

    with open("echo-loop.flat.jsonl", "w", encoding="utf-8") as f:
        for rec in output:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    with open("echo-loop.archive.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✅ Created echo-loop.flat.jsonl and echo-loop.archive.json with {len(output)} echoes")
    if os.path.exists("echo-loop.archive.json"):
        size = os.path.getsize("echo-loop.archive.json") // 1024
        print(f"📦 Total size: {size} KB")

if __name__ == "__main__":
    main()

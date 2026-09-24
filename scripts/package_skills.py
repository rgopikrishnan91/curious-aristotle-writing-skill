#!/usr/bin/env python3
"""Build separate upload ZIPs, each containing exactly one SKILL.md."""

import argparse
from io import BytesIO
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("academic-writing", "academic-writing-lite")


def build_archive(name):
    source = ROOT / name
    files = []
    for path in sorted(source.rglob("*")):
        parts = path.relative_to(source).parts
        if any(part.startswith(".") or part == "__pycache__" for part in parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Do not package symbolic links: {path}")
        if path.is_file() and path.suffix != ".pyc":
            files.append(path)

    skill_files = [path for path in files if path.name == "SKILL.md"]
    if skill_files != [source / "SKILL.md"]:
        raise ValueError(f"{name} must contain exactly one SKILL.md at its root")

    entries = {path.relative_to(ROOT).as_posix(): path.read_bytes() for path in files}
    entries[f"{name}/LICENSE"] = (ROOT / "LICENSE").read_bytes()
    buffer = BytesIO()
    with ZipFile(buffer, "w", compression=ZIP_DEFLATED) as archive:
        for filename, content in sorted(entries.items()):
            # Fixed timestamps and permissions make repeat builds identical.
            info = ZipInfo(filename, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = ZIP_DEFLATED
            archive.writestr(info, content)
    return buffer.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if a ZIP is missing or stale")
    args = parser.parse_args()
    for name in SKILLS:
        data = build_archive(name)
        destination = ROOT / "dist" / f"{name}.zip"
        if args.check:
            if not destination.is_file() or destination.read_bytes() != data:
                parser.exit(1, f"{destination.name} is missing or stale; run scripts/package_skills.py\n")
            print(f"Current: {destination.relative_to(ROOT)}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            print(f"Built: {destination.relative_to(ROOT)} ({len(data)} bytes; 1 SKILL.md)")


if __name__ == "__main__":
    main()

from pathlib import Path

from devclean.rules import get_rules


def scan(path):
    p = Path(path)
    files = []
    rule_names = {rule["name"] for rule in get_rules()}
    for file in list(p.iterdir()):
        if file.name in rule_names:
            files.append(
                {
                    "name": file.name,
                    "path": str(file),
                    "size": sum(f.stat().st_size for f in file.rglob("*") if f.is_file()),
                }
            )
            break

    return files


# print(scan("/tmp"))

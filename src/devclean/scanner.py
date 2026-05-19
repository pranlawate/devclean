from pathlib import Path

from devclean.rules import get_rules


def _dir_size(path):
    """Calculate total size of all files in a directory recursively."""
    return sum(f.stat().st_size for f in path.rglob("*") if f.is_file())


def scan(path):
    """Walk a directory tree and return all cruft directories found."""
    root = Path(path)
    rule_names = {rule["name"] for rule in get_rules()}
    results = []
    for dirpath in root.rglob("*"):
        if dirpath.is_dir() and dirpath.name in rule_names:
            results.append(
                {
                    "name": dirpath.name,
                    "path": str(dirpath),
                    "size": _dir_size(dirpath),
                }
            )
    return results

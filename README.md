# devclean

Find and remove development cruft (`__pycache__`, `node_modules`, `.tox`, etc.) across your projects with a single command.

## Installation

```bash
pip install devclean
```

Or install from source:

```bash
git clone https://github.com/plawate/devclean.git
cd devclean
pip install -e .
```

## Usage

### Scan for cruft

```bash
devclean scan              # scan current directory
devclean scan ~/Work       # scan a specific path
```

```
  __pycache__               1.2 KB    /home/user/project/src/__pycache__
  node_modules             48.3 MB    /home/user/webapp/node_modules
  .pytest_cache              100 B    /home/user/project/.pytest_cache

  3 items, 48.3 MB reclaimable
```

### Clean cruft

```bash
devclean clean ~/Work           # interactive confirmation
devclean clean ~/Work -y        # skip confirmation
devclean clean ~/Work -n        # dry run (preview only)
devclean clean ~/Work --dry-run # same as -n
```

## Detected patterns

| Category | Directories |
|----------|-------------|
| Python   | `__pycache__`, `.pytest_cache`, `.mypy_cache`, `.ruff_cache`, `.eggs`, `.tox`, `.nox`, `htmlcov` |
| Node     | `node_modules`, `.next`, `.nuxt` |
| Rust     | `target` |
| Java     | `.gradle`, `.m2` |
| Build    | `build`, `dist` |
| IDE      | `.idea`, `.vscode` |

## Development

```bash
git clone https://github.com/plawate/devclean.git
cd devclean
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## License

MIT

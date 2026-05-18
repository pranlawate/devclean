CRUFT_PYTHON = [
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "*.egg-info",
    ".eggs",
    ".tox",
    ".nox",
    "htmlcov",
    ".coverage",
]
CRUFT_NODE = ["node_modules", ".next", ".nuxt"]
CRUFT_RUST = ["target"]
CRUFT_JAVA = ["target", ".gradle,.m2"]
CRUFT_BUILD = ["build", "dist"]
CRUFT_IDE = [".idea", ".vscode"]

CRUFT = {
    "Python": CRUFT_PYTHON,
    "Node": CRUFT_NODE,
    "Rust": CRUFT_RUST,
    "JAVA": CRUFT_JAVA,
    "BUILD": CRUFT_BUILD,
    "IDE": CRUFT_IDE,
}


def get_rules():
    rules = []
    for category, name in CRUFT.items():  # "Python" : CRUFT_PYTHON
        rules.extend([{"name": eachname, "category": category} for eachname in name])
    return rules


print(get_rules())

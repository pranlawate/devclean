CRUFT_PYTHON = [
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".eggs",
    ".tox",
    ".nox",
    "htmlcov",
]
CRUFT_NODE = ["node_modules", ".next", ".nuxt"]
CRUFT_RUST = ["target"]
CRUFT_JAVA = [".gradle", ".m2"]
CRUFT_BUILD = ["build", "dist"]
CRUFT_IDE = [".idea", ".vscode"]

CRUFT = {
    "Python": CRUFT_PYTHON,
    "Node": CRUFT_NODE,
    "Rust": CRUFT_RUST,
    "Java": CRUFT_JAVA,
    "Build": CRUFT_BUILD,
    "IDE": CRUFT_IDE,
}


def get_rules():
    rules = []
    for category, patterns in CRUFT.items():
        rules.extend([{"name": name, "category": category} for name in patterns])
    return rules

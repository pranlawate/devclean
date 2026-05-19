from devclean.rules import get_rules


def test_get_rules_returns_list():
    rules = get_rules()
    assert len(rules) > 0


def test_get_rules_entry_structure():
    rule = get_rules()[0]
    assert rule["name"] == "__pycache__"
    assert rule["category"] == "Python"


def test_get_rules_no_accumulation():
    """Calling get_rules() twice returns the same count."""
    first = len(get_rules())
    second = len(get_rules())
    assert first == second

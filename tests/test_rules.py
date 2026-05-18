from devclean.rules import get_rules


def test_get_rules_has_data():
    rules = get_rules()
    assert len(rules) > 0


def test_get_rules_has_value():
    rule = get_rules()[0]
    assert rule["name"] == "__pycache__"
    assert rule["category"] == "Python"

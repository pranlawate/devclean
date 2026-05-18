from devclean.rules import get_rules


def test_get_rules_has_data():
    rules = get_rules()
    print(len(rules))
    assert len(rules) > 0


def test_get_rules_has_value():
    rules = get_rules()
    for rule in rules:
        print(rule)
    assert "__pycache__" in rules[0]["name"]
    assert "Python" in rules[0]["category"]

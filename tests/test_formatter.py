import pytest

from devclean.formatter import format_results, format_size


def test_format_size_bytes():
    assert format_size(100) == "100 B"


def test_format_size_kb():
    assert format_size(2048) == "2.0 KB"


def test_format_size_mb():
    assert format_size(5242880) == "5.0 MB"


def test_format_size_mb_rounding():
    assert format_size(1500000) == "1.4 MB"


def test_format_size_gb():
    assert format_size(2147483648) == "2.0 GB"


def test_format_size_wrong_input():
    with pytest.raises(TypeError):
        format_size("Pranav")


def test_format_results_empty():
    assert format_results([]) == "No cruft found."


def test_format_results_single_item():
    items = [{"name": "__pycache__", "path": "/tmp/__pycache__", "size": 100}]
    output = format_results(items)
    assert "__pycache__" in output
    assert "100 B" in output
    assert "1 items" in output


def test_format_results_total_size():
    items = [
        {"name": "__pycache__", "path": "/a", "size": 512},
        {"name": "node_modules", "path": "/b", "size": 512},
    ]
    output = format_results(items)
    assert "2 items" in output
    assert "1.0 KB" in output

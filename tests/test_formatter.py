from devclean.formatter import format_size


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

from devclean.scanner import scan


def test_scan(tmp_path):
    (tmp_path / "__pycache__").mkdir()
    (tmp_path / "src").mkdir()
    (tmp_path / "__pycache__" / "module.pyc").write_bytes(b"x" * 100)
    filelist = scan(tmp_path)
    print(filelist)
    assert "__pycache__" in filelist[0]["name"]
    assert "src" not in filelist[0]["name"]
    assert filelist[0]["size"] == 100


# Multiple Cruft dirs

# Empty Cruft dir

# Nested Cruft dir __pycache__ inside project/src

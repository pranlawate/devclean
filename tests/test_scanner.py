from devclean.scanner import scan


def test_scan_finds_pycache(tmp_path):
    pycache = tmp_path / "__pycache__"
    pycache.mkdir()
    (pycache / "module.pyc").write_bytes(b"x" * 100)
    results = scan(tmp_path)
    assert len(results) == 1
    assert results[0]["name"] == "__pycache__"
    assert results[0]["size"] == 100


def test_scan_ignores_non_cruft(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "README.md").write_text("hello")
    results = scan(tmp_path)
    assert len(results) == 0


def test_scan_finds_multiple_cruft(tmp_path):
    pycache = tmp_path / "__pycache__"
    pycache.mkdir()
    (pycache / "mod.pyc").write_bytes(b"x" * 50)
    node = tmp_path / "node_modules"
    node.mkdir()
    (node / "package.json").write_bytes(b"x" * 200)
    results = scan(tmp_path)
    names = [r["name"] for r in results]
    assert "__pycache__" in names
    assert "node_modules" in names
    assert len(results) == 2


def test_scan_empty_cruft_dir(tmp_path):
    (tmp_path / ".pytest_cache").mkdir()
    results = scan(tmp_path)
    assert len(results) == 1
    assert results[0]["size"] == 0


def test_scan_nested_cruft(tmp_path):
    nested = tmp_path / "project" / "src"
    nested.mkdir(parents=True)
    pycache = nested / "__pycache__"
    pycache.mkdir()
    (pycache / "utils.pyc").write_bytes(b"x" * 300)
    results = scan(tmp_path)
    assert len(results) == 1
    assert results[0]["name"] == "__pycache__"
    assert "project/src/__pycache__" in results[0]["path"]
    assert results[0]["size"] == 300


def test_scan_returns_full_path(tmp_path):
    (tmp_path / "__pycache__").mkdir()
    results = scan(tmp_path)
    assert str(tmp_path) in results[0]["path"]

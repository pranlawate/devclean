from devclean.cleaner import clean


def test_clean_removes_directory(tmp_path):
    pycache = tmp_path / "__pycache__"
    pycache.mkdir()
    (pycache / "mod.pyc").write_bytes(b"x" * 100)
    targets = [{"name": "__pycache__", "path": str(pycache), "size": 100}]
    result = clean(targets)
    assert not pycache.exists()
    assert len(result["deleted"]) == 1
    assert result["deleted"][0]["name"] == "__pycache__"


def test_clean_removes_multiple(tmp_path):
    pycache = tmp_path / "__pycache__"
    pycache.mkdir()
    node = tmp_path / "node_modules"
    node.mkdir()
    targets = [
        {"name": "__pycache__", "path": str(pycache), "size": 0},
        {"name": "node_modules", "path": str(node), "size": 0},
    ]
    result = clean(targets)
    assert not pycache.exists()
    assert not node.exists()
    assert len(result["deleted"]) == 2
    assert len(result["failed"]) == 0


def test_clean_reports_failed(tmp_path):
    targets = [{"name": "gone", "path": str(tmp_path / "gone"), "size": 0}]
    result = clean(targets)
    assert len(result["deleted"]) == 0
    assert len(result["failed"]) == 1


def test_clean_mixed_success_and_failure(tmp_path):
    pycache = tmp_path / "__pycache__"
    pycache.mkdir()
    targets = [
        {"name": "__pycache__", "path": str(pycache), "size": 0},
        {"name": "gone", "path": str(tmp_path / "gone"), "size": 0},
    ]
    result = clean(targets)
    assert not pycache.exists()
    assert len(result["deleted"]) == 1
    assert len(result["failed"]) == 1

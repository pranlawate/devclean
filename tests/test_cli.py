from devclean.cli import build_parser, main


def test_scan_command():
    parser = build_parser()
    args = parser.parse_args(["scan", "/tmp"])
    assert args.command == "scan"
    assert args.path == "/tmp"


def test_scan_default_path():
    parser = build_parser()
    args = parser.parse_args(["scan"])
    assert args.path == "."


def test_clean_command():
    parser = build_parser()
    args = parser.parse_args(["clean", "/tmp"])
    assert args.command == "clean"
    assert args.path == "/tmp"


def test_clean_yes_flag():
    parser = build_parser()
    args = parser.parse_args(["clean", "--yes"])
    assert args.yes is True


def test_clean_dry_run_flag():
    parser = build_parser()
    args = parser.parse_args(["clean", "--dry-run"])
    assert args.dry_run is True


def test_no_command_shows_help(capsys):
    try:
        main([])
    except SystemExit:
        pass
    captured = capsys.readouterr()
    assert "devclean" in captured.out


def test_scan_finds_cruft(tmp_path, capsys):
    pycache = tmp_path / "__pycache__"
    pycache.mkdir()
    (pycache / "mod.pyc").write_bytes(b"x" * 100)
    main(["scan", str(tmp_path)])
    captured = capsys.readouterr()
    assert "__pycache__" in captured.out
    assert "100 B" in captured.out


def test_scan_no_cruft(tmp_path, capsys):
    (tmp_path / "src").mkdir()
    main(["scan", str(tmp_path)])
    captured = capsys.readouterr()
    assert "No cruft found" in captured.out


def test_clean_dry_run(tmp_path, capsys):
    pycache = tmp_path / "__pycache__"
    pycache.mkdir()
    (pycache / "mod.pyc").write_bytes(b"x" * 50)
    main(["clean", str(tmp_path), "--dry-run"])
    captured = capsys.readouterr()
    assert "Dry run" in captured.out
    assert pycache.exists()


def test_clean_with_yes(tmp_path, capsys):
    pycache = tmp_path / "__pycache__"
    pycache.mkdir()
    (pycache / "mod.pyc").write_bytes(b"x" * 50)
    main(["clean", str(tmp_path), "--yes"])
    captured = capsys.readouterr()
    assert not pycache.exists()
    assert "Deleted 1 items" in captured.out


def test_clean_aborted(tmp_path, capsys, monkeypatch):
    pycache = tmp_path / "__pycache__"
    pycache.mkdir()
    monkeypatch.setattr("builtins.input", lambda _: "n")
    main(["clean", str(tmp_path)])
    captured = capsys.readouterr()
    assert pycache.exists()
    assert "Aborted" in captured.out

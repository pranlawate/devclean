import shutil


def clean(targets):
    """Remove cruft directories. Returns dict with 'deleted' and 'failed' lists."""
    deleted = []
    failed = []
    for target in targets:
        try:
            shutil.rmtree(target["path"])
            deleted.append(target)
        except Exception:
            failed.append(target)
    return {"deleted": deleted, "failed": failed}

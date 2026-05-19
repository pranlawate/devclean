def format_size(size):
    """Convert bytes to human-readable size string."""
    if not isinstance(size, (int, float)):
        raise TypeError(f"Expected numeric size, got {type(size).__name__}")
    if size >= 1024**3:
        return f"{size / 1024**3:.1f} GB"
    elif size >= 1024**2:
        return f"{size / 1024**2:.1f} MB"
    elif size >= 1024:
        return f"{size / 1024:.1f} KB"
    return f"{size} B"


def format_results(results):
    """Format scan results as a printable summary."""
    if not results:
        return "No cruft found."
    lines = []
    for item in results:
        lines.append(f"  {item['name']:<20} {format_size(item['size']):>10}    {item['path']}")
    total = sum(r["size"] for r in results)
    lines.append(f"\n  {len(results)} items, {format_size(total)} reclaimable")
    return "\n".join(lines)

def format_size(size):
    try:
        if size / 1024**3 > 1:
            return f"{size / 1073741824:.1f} GB"
        elif size / 1024**2 > 1:
            return f"{size / 1048576:.1f} MB"

        elif size / 1024 > 1:
            return f"{size / 1024:.1f} KB"
        else:
            return f"{size} B"
    except TypeError:
        return "You have entered Wrong input"

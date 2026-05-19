import argparse
import sys

from devclean.cleaner import clean
from devclean.formatter import format_results, format_size
from devclean.scanner import scan


def build_parser():
    parser = argparse.ArgumentParser(
        prog="devclean",
        description="Find and remove development cruft across projects",
    )
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan", help="Scan for cruft directories")
    scan_parser.add_argument("path", nargs="?", default=".")

    clean_parser = subparsers.add_parser("clean", help="Remove cruft directories")
    clean_parser.add_argument("path", nargs="?", default=".")
    clean_parser.add_argument("-y", "--yes", action="store_true", help="Skip confirmation prompt")
    clean_parser.add_argument("-n", "--dry-run", action="store_true", help="Show what would be deleted")

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == "scan":
        results = scan(args.path)
        print(format_results(results))

    elif args.command == "clean":
        results = scan(args.path)
        if not results:
            print("No cruft found.")
            return

        print(format_results(results))

        if args.dry_run:
            print("\n  Dry run -- nothing deleted.")
            return

        if not args.yes:
            answer = input("\n  Delete all? [y/N] ")
            if answer.lower() != "y":
                print("  Aborted.")
                return

        outcome = clean(results)
        deleted_size = sum(r["size"] for r in outcome["deleted"])
        print(f"\n  Deleted {len(outcome['deleted'])} items, freed {format_size(deleted_size)}")
        if outcome["failed"]:
            print(f"  Failed to delete {len(outcome['failed'])} items:")
            for f in outcome["failed"]:
                print(f"    {f['path']}")


if __name__ == "__main__":
    main()

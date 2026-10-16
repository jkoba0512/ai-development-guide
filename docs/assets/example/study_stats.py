"""Summarize study time without external dependencies, storage, or networking."""
import sys


def summarize(values):
    """Return count, total, and average for one or more integers from 0 through 1440."""
    if not values:
        raise ValueError("Provide at least one duration in minutes")
    if any(type(value) is not int or not 0 <= value <= 1440 for value in values):
        raise ValueError("Durations must be integers from 0 through 1440")
    total = sum(values)
    return len(values), total, total / len(values)


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    try:
        values = [int(arg) for arg in args]
        count, total, average = summarize(values)
    except ValueError:
        print("Error: provide one or more integer durations from 0 through 1440 minutes", file=sys.stderr)
        return 2
    print(f"Count: {count} / Total: {total} min / Average: {average:.1f} min")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

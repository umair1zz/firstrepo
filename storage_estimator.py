"""Storage Estimator

Estimates how much disk space a collection of files will need,
based on the number of files and the average size of each file.
"""


def to_kb(size, unit):
    """Convert a size in the given unit (KB or MB) to kilobytes."""
    if unit == "KB":
        return size
    if unit == "MB":
        return size * 1024
    raise ValueError("Unit must be KB or MB")


def main():
    print("=== Storage Estimator ===")

    try:
        count = int(input("Number of files: "))
        avg_size = float(input("Average file size: "))
        unit = input("Unit (KB or MB): ").strip().upper()

        total_kb = count * to_kb(avg_size, unit)
        total_mb = total_kb / 1024

        print("Total size:", total_kb, "KB")
        print("Total size:", total_mb, "MB")
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()

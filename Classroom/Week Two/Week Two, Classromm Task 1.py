
"""Demonstrate Python arithmetic operators."""


def calculate_storage(file_count: int, file_size_mb: float) -> float:
    """Calculate the total storage required for all files."""
    return file_count * file_size_mb


def calculate_average(total_size_mb: float, file_count: int) -> float:
    """Calculate the average size of one file."""
    return total_size_mb / file_count


def split_logs(log_files: int, archive_size: int) -> tuple[int, int]:
    """Return the number of full archives and remaining files."""
    # // gives the number of complete groups.
    full_archives = log_files // archive_size

    # % gives the remainder after complete groups are removed.
    remaining_files = log_files % archive_size

    return full_archives, remaining_files


def calculate_code_combinations(characters: int, code_length: int) -> int:
    """Calculate the number of possible codes when repetition is allowed."""
    # ** raises one number to the power of another.
    return characters ** code_length


def main() -> None:
    """Run the operators demonstration."""

    # File storage calculations
    file_count = 25
    file_size_mb = 8.0
    storage_limit_mb = 250.0

    total_size_mb = calculate_storage(file_count, file_size_mb)
    remaining_storage_mb = storage_limit_mb - total_size_mb
    average_size_mb = calculate_average(total_size_mb, file_count)

    print("LOG STORAGE")
    print(f"Total storage used: {total_size_mb} MB")
    print(f"Storage remaining: {remaining_storage_mb} MB")
    print(f"Average file size: {average_size_mb} MB")

    # Log archive calculations
    log_files = 137
    archive_size = 12

    full_archives, remaining_files = split_logs(
        log_files, archive_size
    )

    print("\nLOG ARCHIVES")
    print(f"Full archives: {full_archives}")
    print(f"Files remaining: {remaining_files}")

    # Code combination calculations
    characters = 10
    code_length = 4

    possible_codes = calculate_code_combinations(
        characters, code_length
    )

    print("\nCODE COMBINATIONS")
    print(f"Possible codes: {possible_codes}")


if __name__ == "__main__":
    main()
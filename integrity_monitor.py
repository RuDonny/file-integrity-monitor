import argparse
import hashlib
import json
from pathlib import Path

DATABASE_FILE = Path("hashes.json")


def calculate_sha256(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def load_database():
    """Load saved file hashes or return an empty database."""
    if DATABASE_FILE.exists():
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return {}


def save_database(database):
    """Save file hashes to the JSON database."""
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(database, file, indent=4)


def create_baseline(file_path):
    """Save the current file hash as the trusted baseline."""
    path = Path(file_path).expanduser().resolve()

    if not path.is_file():
        print("ERROR: File not found.")
        return

    database = load_database()
    database[str(path)] = calculate_sha256(path)
    save_database(database)

    print(f"BASELINE CREATED: {path}")


def check_integrity(file_path):
    """Compare the current hash with the trusted baseline."""
    path = Path(file_path).expanduser().resolve()
    database = load_database()

    if str(path) not in database:
        print("UNKNOWN: No baseline exists for this file.")
        return

    if not path.is_file():
        print(f"DELETED: {path}")
        return

    trusted_hash = database[str(path)]
    current_hash = calculate_sha256(path)

    if current_hash == trusted_hash:
        print(f"UNCHANGED: {path}")
    else:
        print(f"MODIFIED: {path}")
        print(f"Expected: {trusted_hash}")
        print(f"Current:  {current_hash}")


def main():
    parser = argparse.ArgumentParser(
        description="Create and verify SHA-256 file-integrity baselines."
    )
    parser.add_argument(
        "action",
        choices=["baseline", "check"],
        help="Create a baseline or check file integrity.",
    )
    parser.add_argument("file", help="File to monitor.")
    args = parser.parse_args()

    if args.action == "baseline":
        create_baseline(args.file)
    else:
        check_integrity(args.file)


if __name__ == "__main__":
    main()

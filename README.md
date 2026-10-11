# Python File Integrity Monitor

A command-line security tool that detects file modification or deletion by comparing SHA-256 hashes against a trusted baseline.

## Features

- Creates a trusted SHA-256 baseline for a file
- Detects unauthorized file modifications
- Detects deleted monitored files
- Stores trusted hashes in a local JSON database
- Supports Linux file paths
- Uses only the Python standard library

## Security Concept

A cryptographic hash acts as a digital fingerprint. Even a small change to a file produces a dramatically different SHA-256 value. File integrity monitoring uses this behavior to identify unexpected changes to important files.

This project demonstrates a simplified version of the file integrity monitoring used by security platforms such as Wazuh.

## Requirements

- Python 3.10 or newer
- Linux, macOS, or Windows

No third-party Python packages are required.

## Usage

Create a trusted baseline:

```bash
python3 integrity_monitor.py baseline example.txt
```

Check the file later:

```bash
python3 integrity_monitor.py check example.txt
```

Possible results:

```text
UNCHANGED: The file matches its trusted baseline.
MODIFIED: The file content has changed.
DELETED: The monitored file no longer exists.
UNKNOWN: No baseline has been created for the file.
```

## Example Detection

```text
MODIFIED: /path/to/example.txt
Expected: 66551aa25b6174eda638294188e846661fde111465b12e8edd2f6d965ef43af6
Current:  b8b17567ed1ad0b9f4b3d21b600fc7a867905675fb312fd72f46694d424322fc
```

## Skills Demonstrated

- Python functions and command-line arguments
- File handling and path validation
- SHA-256 cryptographic hashing
- JSON data storage
- Defensive security monitoring
- Git version control

## Limitations

This is an educational portfolio project. The local hash database should be protected against unauthorized modification in a production environment.

## Author

Created by [RuDonny](https://github.com/RuDonny) as part of a cybersecurity portfolio.

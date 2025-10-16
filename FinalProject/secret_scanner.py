"""
Final Project: Secret Scanner 
Created by: Samantha Harper

This script is a Python CLI tool that scans files and directories
for potential hardcoded secrets such as API keys, passwords, and tokens.

Features:
- Uses regex patterns (from regex_patterns.py) to detect secrets
- Accepts a file or directory as input
- Logs findings to a log file and prints a formatted report in the terminal
- Includes detailed error handling and logging for transparency

"""

import os
import argparse
import logging
from regex_patterns import PATTERNS  # Import regex patterns from external file

# ----------------------Logging Configuration-----------------------------------
# Creates or appends to "secret_scanner.log"
# Logs both INFO and ERROR messages with timestamps

logging.basicConfig(
    filename="secret_scanner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------Function: scan_file-----------------------------------
def scan_file(filepath):
    """
    Scans a single file line by line for any matches to secret patterns.

    Args:
        filepath (str): The full path of the file to scan.

    Returns:
        list: A list of tuples containing (filename, line number, pattern type, matched text)
    """
    findings = []
    try:
        # Open the file safely with UTF-8 encoding; ignore decoding errors
        with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
            for line_num, line in enumerate(file, start=1):
                # Check each regex pattern for a match in the current line
                for pattern_name, pattern in PATTERNS.items():
                    match_obj = pattern.search(line)
                    if match_obj:
                        match = match_obj.group(0)
                        findings.append((filepath, line_num, pattern_name, match.strip()))
                        logging.info(f"[FOUND] {pattern_name} in {filepath}:{line_num}")
    except Exception as e:
        logging.error(f"Error reading {filepath}: {e}")
    return findings


# -------------------Function: scan_directory--------------------------------------
def scan_directory(directory):
    """
    Scans a directory for secrets in all contained files.

    Args:
        directory (str): Directory path to scan.

    Returns:
        list: A combined list of all findings from scanned files.
    """
    all_findings = []
    # Walk through each subdirectory and file
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            all_findings.extend(scan_file(filepath))
    return all_findings


# --------------------Main Function-------------------------------------
def main():
    """
    Main entry point for the CLI tool.
    Parses command-line arguments, determines whether the target is a file or directory,
    and initiates the scanning process.
    """
    parser = argparse.ArgumentParser(
        description="🔍 Scan files or directories for hardcoded secrets using regex."
    )
    parser.add_argument(
        "path",
        help="Path to a file or directory to scan."
    )
    args = parser.parse_args()

    path = args.path
    logging.info(f"Starting scan on: {path}")

    # Determine if the path is a file or directory
    if os.path.isfile(path):
        findings = scan_file(path)
    elif os.path.isdir(path):
        findings = scan_directory(path)
    else:
        print("Invalid path specified.")
        return

    # -----------------Report Results----------------------------------------
    print("\n=== Secret Scan Report ===")
    if findings:
        for f in findings:
            print(f"File: {f[0]}\nLine: {f[1]}\nType: {f[2]}\nMatch: {f[3]}\n{'-'*40}")
    else:
        print(" No potential secrets found.")

    print("\nScan complete. See 'secret_scanner.log' for detailed logs.")


if __name__ == "__main__":
    main()

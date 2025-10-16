# Secret Scanner CLI Tool -- SDEV 245 Final Project

## Overview
This Python CLI tool scans files and directories for hardcoded secrets using regular expressions.  
It helps developers detect sensitive data such as API keys, passwords, and tokens before committing code.

---

## Features
- Scans files or entire directories 
- Detects common secret patterns:
  - AWS Access Keys
  - AWS Secret Keys
  - Generic API Keys
  - Bearer Tokens
  - Private Keys
  - Passwords
- Outputs a detailed report with file, line number, and matched text
- Logs all findings in `secret_scanner.log`

---

## Dependencies
No external dependencies are required, only Python 3+

## Run Script
- python secret_scanner.py (path)

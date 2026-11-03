# antivirus-demo

# Simple Antivirus Scanner (Demo)

A lightweight file scanner written in Python.

## Features
- Scans all files in a folder
- Detects known malware using SHA-256 hash matching
- Flags suspicious file types (.exe, .bat, .scr, .vbs, .js)

## How to run
1. Install Python 3
2. Create a folder named `test_folder` and add some files
3. Run: `python scanner.py`

## Sample output
```
Safe: notes.txt
Warning (suspicious type): setup.exe
VIRUS: sample.bin
```

## Note
This is a demo version with sample hashes only.
The full version (quarantine, disguised-file detection,
logging, large signature database) is private.
Contact me for access.

## About this project
This is a learning project. I built it with the help of AI and I am studying how each part works.

## About me
Learning cybersecurity and Python.
LinkedIn:https://www.linkedin.com/in/rr-r-9b4828432?utm_source=share_via&amp;utm_content=profile&amp;utm_medium=member_android

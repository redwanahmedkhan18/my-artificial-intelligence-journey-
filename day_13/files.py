"""
Python File Handling: Complete Super-Pro Demonstration
Covers: text files, binary files, CSV, JSON, compression, random access, temp files, concurrency-safe writes
"""

import os
from pathlib import Path
import csv
import json
import gzip
import tempfile
import fcntl  # for Unix file locking, skip on Windows

# -------------------------------
# 1. Paths and Directories
# -------------------------------
base_dir = Path("demo_files")
base_dir.mkdir(exist_ok=True, parents=True)

text_file = base_dir / "example.txt"
binary_file = base_dir / "example.bin"
csv_file = base_dir / "data.csv"
json_file = base_dir / "data.json"
compressed_file = base_dir / "data.txt.gz"
temp_file_path = base_dir / "temp_demo.txt"

# -------------------------------
# 2. Basic Text File Operations
# -------------------------------
print("\n--- Text File Write/Read/Append ---")
with open(text_file, "w") as f:
    f.write("Hello, Python File Handling!\n")
    f.write("This is a second line.\n")

with open(text_file, "a") as f:
    f.write("Appending a new line.\n")

with open(text_file, "r") as f:
    print(f.read())

# -------------------------------
# 3. Binary File Handling
# -------------------------------
print("\n--- Binary File Write/Read ---")
data_bytes = b"\x00\x01\x02\x03\x04PythonBinary"
with open(binary_file, "wb") as f:
    f.write(data_bytes)

with open(binary_file, "rb") as f:
    print(f.read())

# -------------------------------
# 4. CSV File Handling
# -------------------------------
print("\n--- CSV Write/Read ---")
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 30])
    writer.writerow(["Bob", 25])

with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# -------------------------------
# 5. JSON File Handling
# -------------------------------
print("\n--- JSON Write/Read ---")
data = {"name": "Redwan", "skills": ["Python", "ML", "OOP"]}
with open(json_file, "w") as f:
    json.dump(data, f, indent=4)

with open(json_file, "r") as f:
    loaded = json.load(f)
    print(loaded)

# -------------------------------
# 6. File Compression with Gzip
# -------------------------------
print("\n--- Gzip Compression ---")
with open(text_file, "rb") as f_in:
    with gzip.open(compressed_file, "wb") as f_out:
        f_out.writelines(f_in)

with gzip.open(compressed_file, "rt") as f_in:
    print(f_in.read())

# -------------------------------
# 7. Random Access and seek/tell
# -------------------------------
print("\n--- Random Access in File ---")
with open(text_file, "r+") as f:
    f.seek(5)  # move cursor to 6th byte
    f.write("INSERTED")  # overwrite starting here
    f.seek(0)
    print(f.read())

# -------------------------------
# 8. Temporary File
# -------------------------------
print("\n--- Temporary File ---")
with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
    tmp.write("Temporary data for demo.\nAnother line here.")
    tmp.seek(0)
    print(tmp.read())
    print(f"Temp file saved at: {tmp.name}")

# -------------------------------
# 9. Concurrency-Safe File Writing (Unix)
# -------------------------------
print("\n--- Concurrency-Safe File Writing ---")
concurrent_file = base_dir / "shared.txt"
with open(concurrent_file, "a") as f:
    try:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write("Safe write using file lock.\n")
        fcntl.flock(f, fcntl.LOCK_UN)
    except Exception as e:
        print(f"Locking failed: {e}")

with open(concurrent_file, "r") as f:
    print(f.read())

# -------------------------------
# 10. Iterative Read for Large Files
# -------------------------------
print("\n--- Iterative Read for Large Files ---")
with open(text_file, "r") as f:
    for line in f:
        print(f"Line: {line.strip()}")


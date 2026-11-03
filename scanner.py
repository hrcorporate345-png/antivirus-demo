import os, hashlib

SUSPICIOUS_EXT = {".exe", ".bat", ".scr", ".vbs", ".js"}
BAD_HASHES = {"demo_hash_1", "demo_hash_2"}  # demo ke fake hashes

def file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def scan(folder):
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue
        ext = os.path.splitext(name)[1].lower()
        if file_hash(path) in BAD_HASHES:
            print("VIRUS:", name)
        elif ext in SUSPICIOUS_EXT:
            print("Warning (suspicious type):", name)
        else:
            print("Safe:", name)

scan("test_folder")
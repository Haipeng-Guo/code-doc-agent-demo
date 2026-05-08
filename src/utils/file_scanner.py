from pathlib import Path
from typing import List

def scan_code_files(directory: str, extensions: List[str] = None) -> List[Path]:
    if extensions is None:
        extensions = [".py", ".js", ".ts", ".java", ".go"]
    path = Path(directory)
    files = []
    for ext in extensions:
        files.extend(path.rglob(f"*{ext}"))
    # exclude common dirs
    files = [f for f in files if not any(part in f.parts for part in ["__pycache__", "node_modules", ".git"])]
    return files
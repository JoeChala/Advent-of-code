from pathlib import Path
from typing import Iterator

def file_import(day:int) -> Path:
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    DATA_FILE =  PROJECT_ROOT / f"Day{day}" / "data.txt"
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"{DATA_FILE} not found")
    
    return DATA_FILE

def readlines(path: Path) -> Iterator[str]:
    try:
        f = Path(path).open(mode='r',encoding='utf-8')
    except FileNotFoundError:
        raise FileNotFoundError(f"Incorrect file path")
    
    with f:
        for line in f:
            yield line.strip("\n")

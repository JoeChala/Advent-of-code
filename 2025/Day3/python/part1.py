from pathlib import  Path 
from typing import Iterator
from utils.py_utils import file_import,readlines


def largest_jolt(line: str) -> int:
    if not line.isdigit():
        raise ValueError("Invalid line data type. Should be integer")
    
    length: int = len(line)
    left: str = max(line[:length-1])
    left_index:int = line.index(left)

    value:str = left + max(line[left_index+1:])
    return int(value)

if __name__ == "__main__":
    total_jolt: int = 0
    file_path: Path = file_import(day=3)

    for line in readlines(path=file_path):
        total_jolt += largest_jolt(line)
        
    print(f"Part1 : {total_jolt}")



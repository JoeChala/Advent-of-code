from pathlib import  Path 
from typing import Iterator
from utils.py_utils import file_import,readlines


def largest_jolt(digits: str,output_len: int = 12) -> int:
    if not digits.isdigit():
        raise ValueError("Invalid line data type. Should be integer")
    remove = len(digits) - output_len
    stack: list[str] = []

    for d in digits:
        while stack and remove > 0 and stack[-1] < d:
            stack.pop()
            remove -= 1
        stack.append(d)

    if remove > 0:
        stack = stack[:-remove]

    stack = stack[:output_len]
    result = 0
    for d in stack:
        result = result * 10 + (ord(d) - ord("0"))

    return result

if __name__ == "__main__":
    total_jolt: int = 0
    file_path: Path = file_import(day=3)

    for line in readlines(path=file_path):
        total_jolt += largest_jolt(line)
        

    print(f"Part2 : {total_jolt}")



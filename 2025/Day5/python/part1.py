from pathlib import Path
from utils.py_utils import file_import

def merge_ranges(ranges) -> list[tuple[int, int]]:
    ranges.sort()
    merged: list[tuple[int,int]] = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged

def contains(r:tuple[int,int], x:int) -> bool:
    return r[0] <= x <= r[1]



if __name__ == "__main__":
    count:int = 0
    ranges: list[tuple[int,int]] = []
    values: list = []
    file_path: Path = file_import(day=5)

    with Path(file_path).open(mode='r',encoding='utf-8') as f:
        for line in f:
            if "-" in line:
                start,end = list(map(int,line.strip().split("-")))
                ranges.append((start,end))
            try:
                values.append(int(line.strip()))
            except ValueError:
                ranges = merge_ranges(ranges=ranges)

    for val in values:
        for range in ranges:
            if contains(range,val):
                count += 1
                break

    print(count)

    
    
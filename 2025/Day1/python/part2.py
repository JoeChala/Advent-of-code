from pathlib import Path
from typing import Iterator


def readline(path: str) -> Iterator[str]:
    with Path(path).open("r", encoding='utf-8') as f:
        for line in f:
            yield line.strip("\n")

def parse_lines(line: str) -> tuple[str,int]:
    if len(line) < 2 or not line:
        raise ValueError(f"Invalid line: {line!r}")
    
    return line[0], int(line[1:])

def count_crossings_left(cur: int, value: int, max_dial: int) -> tuple[int,int]:
    if cur == 0:
        passes = value // max_dial
    elif value < cur:
        passes = 0
    else:
        passes = ((value - cur) // max_dial) + 1

    new = (cur - value) % max_dial
    return passes, new


def count_crossings_right(cur: int, value: int, max_dial: int) -> tuple[int,int]:
    raw = cur + value
    passes = raw // max_dial
    new = raw % max_dial
    return passes, new



if __name__ == "__main__":
    max_dial: int = 100
    cur_dial: int = 50
    count_zero: int = 0
    
    for line in readline(r"./../data.txt"):
        direction, value = parse_lines(line)
        match direction:
            case "L":
                passes,cur_dial = count_crossings_left(cur_dial, value, max_dial)
                count_zero += passes

            case "R":
                passes,cur_dial = count_crossings_right(cur_dial, value, max_dial)
                count_zero += passes

            case _:
                raise ValueError(f"Unknown direction: {direction!r}")
            
    print(count_zero)

        

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

if __name__ == "__main__":
    max_dial: int = 100
    cur_dial: int = 50
    count_zero: int = 0
    
    for line in readline(r"./../data.txt"):
        direction, value = parse_lines(line)
        match direction:
            case "L":
                move = cur_dial - value
                while move < 0:
                    move += max_dial

                cur_dial = move
                    
                if cur_dial == 0:
                    count_zero += 1

            case "R":
                move = cur_dial + value
                while move >= max_dial:
                    move -= max_dial
                
                cur_dial = move

                if cur_dial == 0:
                    count_zero += 1

            case _:
                raise ValueError(f"Unknown direction: {direction!r}")
            
    print(count_zero)

        

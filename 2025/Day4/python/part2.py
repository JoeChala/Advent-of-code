from utils.py_utils import file_import,readlines
from pathlib import Path

DIRECTIONS: list[tuple[int, int]] = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def remove_weak_rolls(grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    to_remove: list[tuple[int, int]] = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbors = 0
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbors += 1
                        if neighbors >= 4:
                            break  # early exit

            if neighbors < 4:
                to_remove.append((r, c))

    for r, c in to_remove:
        grid[r][c] = '.'

    return len(to_remove)


def remove_rolls(grid: list[list[str]]) -> int:
    total_removed = 0

    while True:
        removed_this_round = remove_weak_rolls(grid)
        if removed_this_round == 0:
            break
        total_removed += removed_this_round

    return total_removed



if __name__ == "__main__":
    GRID: list[list[str]] =[]
    file_path: Path = file_import(day=4)

    for line in readlines(path=file_path):
        GRID.append(list(line))
     
    count = remove_rolls(GRID)
    print(f"Part 2: {count}")


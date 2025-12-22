from utils.py_utils import file_import,readlines
from pathlib import Path

DIRECTIONS: list[tuple[int, int]] = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def count_paper_rolls(grid:list[str],r:int,c:int) -> int:
    rows, cols = len(grid), len(grid[0])
    count = 0

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                count += 1

    return count

if __name__ == "__main__":
    count = 0
    GRID: list[str] = []
    file_path: Path = file_import(day=4)

    for line in readlines(path=file_path):
        GRID.append(line)

    for r in range(len(GRID)):
        for c in range(len(GRID[r])):
            if GRID[r][c] == '@':
                neighbors = count_paper_rolls(GRID, r, c)
                if neighbors < 4:
                    count += 1

    print(f"Part 1: {count}")


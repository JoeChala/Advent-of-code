import csv

def check_valid(num: int) -> bool:
    s : str = str(num)
    n : int = len(s)
    
    if n%2 != 0: 
        return True

    mid = n//2
    return s[:mid] != s[mid:]


if __name__ == "__main__":
    count = 0
    file_name = r"./../data.csv"

    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        data = next(reader)
        for rng in data:
            first, last = map(int, rng.strip().split("-"))
            for num in range(first, last + 1):
                if not check_valid(num):
                    count += num

    print(count)   

import csv


def check_valid(num: int) -> bool:
    original = num

    length = 0
    temp = num
    while temp > 0:
        temp //= 10
        length += 1

    for L in range(1, length):
        if length % L != 0:
            continue 
        temp = original
        block = temp % (10 ** L)

        k = length // L  # number of blocks

        valid = True
        for _ in range(k):
            current = temp % (10 ** L)
            if current != block:
                valid = False
                break
            temp //= 10 ** L

        if valid:
            return False 
    
    return True



if __name__ == "__main__":
    count = 0
    file_name = r"./../data.csv"

    with open(file_name,newline='') as f:
        reader = csv.reader(f,delimiter=',');
        data = reader.__next__()
        for i in data:
            first,last = list(map(int,i.strip().split("-")))
            for i in range(first,last+1):
                if not check_valid(i):
                    count += i 
            
    print(count)
   

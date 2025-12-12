import csv

def check_valid(num: int) -> bool:
    original = num
    length = len(str(num))
    pow10 = [10**i for i in range(length + 1)]
    divisors = []
    for L in range(1, int(length ** 0.5) + 1):
        if length % L == 0:
            if L < length:
                divisors.append(L)
            other = length // L
            if other < length and other != L:
                divisors.append(other)

    for L in divisors:
        block = original % pow10[L]     
        k = length // L

        repeated, multiplier = 0,1 
        for _ in range(k):
            repeated += block * multiplier
            multiplier *= pow10[L]

        if repeated == original:
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
   

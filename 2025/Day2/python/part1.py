import csv

def check_valid(num: int) -> bool:
    temp,i = num,0
    while temp != 0:
        temp = temp // 10
        i += 1
    if i % 2 != 0: return True
    i = 10**(i//2)
    temp = num % i
    num = num // i
    if temp == num:
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
   

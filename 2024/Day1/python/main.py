def main() -> None:
    left, right = [],[]
    with open("./data.txt",'r') as file:
        for line in file:
            nums = list(map(int,line.strip().split()))
            left.append(nums[0])
            right.append(nums[1])
    
    leng = len(left)-1
    quicksort(left,0,leng)
    quicksort(right,0,leng)

    sum = 0
    for i in range(0,leng+1):
        sum += abs(left[i] - right[i])
    print(sum)

def swap(arr:list,a : int,b : int) -> None:
    arr[a],arr[b] = arr[b],arr[a]


def quicksort(arr : list,low : int,high : int) -> None:
    if low < high:
        p = partition(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)

def partition(arr : list,low : int,high : int) -> int:
    pivot = arr[high]
    i = low

    for j in range(low,high):
        if arr[j] <= pivot:
            swap(arr,i,j)
            i += 1
    swap(arr,i,high)
    return i

if __name__ == "__main__":
    main()

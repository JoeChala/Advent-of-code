package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	data, err := os.ReadFile("data.txt")
	if err != nil{
		panic("cannot read file: "+err.Error())
	}

	left := []int{}
	right := []int{}

	lines := strings.Split(strings.TrimSpace(string(data)),"\n")
	for _,line := range lines{
		fields := strings.Fields(line)
	  
		a,_ := strconv.Atoi(fields[0])
		b,_ := strconv.Atoi(fields[1])
		left = append(left,a)
		right = append(right,b)
	}
  quicksort(left,0,len(left)-1)
	quicksort(right,0,len(right)-1)

	sum := 0
	//sum of difference in pairs
	for i := 0; i < len(left); i++ {
		diff := left[i] - right[i]
		if diff < 0 {
			diff = -diff
		}
		sum += diff
	}
	fmt.Println("Part 1:", sum)

	//similarity score, element * freq in right
	simScore := 0
	for _, val := range left {
		count := 0
		for _, r := range right {
			if r == val {
				count++
			}
		}
		simScore += val * count
	}
	fmt.Println("Part 2:", simScore)
}

func quicksort(arr []int,low int,high int) {
	if low<high{
		p := partition(arr,low,high)
		quicksort(arr,low,p-1)
		quicksort(arr,p+1,high)
	}
}

func partition(arr []int,low int,high int) int{
	pivot := arr[high]
	i := low
	for j:=low;j<high;j++ {
		if arr[j] <= pivot{
			arr[i],arr[j] = arr[j],arr[i]
			i += 1
		}
	}
	arr[i],arr[high] = arr[high],arr[i]
	return i
}

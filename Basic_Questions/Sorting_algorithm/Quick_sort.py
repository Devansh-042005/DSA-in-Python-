# Quick sort implementation in Python

numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

def partition (nums , low , high):
    pivot = nums[low]
    i = low
    j = high

    while i < j:
        while nums[i] <= pivot and i <= high-1:
            i+=1
        while nums[j] > pivot and j >= low+1:
            j-=1

        if i < j:
            nums[i],nums[j] = nums[j],nums[i]

        nums[low],nums[j] = nums[j],nums[low]

    return j

def quick_sort(nums,low,high):
    if low < high:
        ind = partition(nums,low,high)
        quick_sort (nums,low,ind-1)
        quick_sort (nums,ind+1,high)
    return nums

print (quick_sort(numbers,0,len(numbers)-1))


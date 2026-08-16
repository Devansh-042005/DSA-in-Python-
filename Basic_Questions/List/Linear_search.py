nums = []
n = int(input("enter how many elements do you want to enter in list : "))
target = int(input("Enter Target value : "))

for i in range(n):
    num = int(input(f"Enter {i+1} integer : "))
    nums.append(num)

def linear_search(nums,target):
    for i in range(0 , n):
        if nums[i] == target :
            return 00[i]
    return -1
print(linear_search(nums,target))
        
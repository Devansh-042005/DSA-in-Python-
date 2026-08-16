# CondN : Unique element at left side and in side any element , doesn't matter how many times it is repeated
nums = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    nums.append(num)
    
def remove_duplicate(nums):
    i = 0
    j = i+1
    n = len(nums)
    if n == 1:
        return 1
    while j < n :
        if nums[i] != nums[j]:
            nums[i+1],nums[j] = nums[j],nums[i+1]
            i += 1
            j += 1
        else: 
            j += 1
    return (i+1),nums

print(remove_duplicate(nums))
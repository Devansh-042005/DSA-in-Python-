numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

def check_sorting(nums):
    inc = True
    dic = True

    if len(nums) > 1 :
        for i in range (0, len(nums)-1):
            if nums[i] > nums[i+1]:
                inc = False
            if nums[i] < nums[i+1]:
                dic = False
            if not inc and not dic:
                break
        
        if (inc and dic):
            return ("Identical")
        elif (inc):
            return ("increasing order")
        elif (dic):
            return ("decreasing order")
        else:
            return("not sorted")
        
    return ("Identical")

print(check_sorting(numbers))
            


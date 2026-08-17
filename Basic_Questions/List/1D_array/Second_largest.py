# Second Largest : 
numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

def second_largest_element(nums):
    largest = float ("-inf")
    second_largest = float ("-inf")

    for i in nums:
        if i > largest:
            second_largest = largest
            largest = i

        if i > second_largest and i != largest :
            second_largest = i

    return second_largest

print(second_largest_element(numbers ))
    
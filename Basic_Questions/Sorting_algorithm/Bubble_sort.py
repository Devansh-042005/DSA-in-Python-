numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

length = len(numbers)

for i in range ((length - 2) , -1 , -1):
    is_swap = False
    for j in range (0 , i+1):
        if (numbers[j] > numbers[j+1]):
            numbers[j] , numbers[j+1] = numbers[j+1] , numbers[j]
            is_swap = True
        if (is_swap == False):
            break

print("Increasing order : ",numbers)

for i in range ((length - 2) , -1 , -1):
    is_swap = False
    for j in range (0 , i+1):
        if (numbers[j] < numbers[j+1]):
            numbers[j] , numbers[j+1] = numbers[j+1] , numbers[j]
            is_swap = True
        if (is_swap == False):
            break

print("Dicreasing order : ",numbers)


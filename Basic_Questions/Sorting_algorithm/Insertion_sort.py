numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

length = len(numbers)

for i in range(1 , length):
    key = numbers[i]
    j = i-1

    while j >= 0 and numbers[j] > key :
        numbers[j+1] = numbers[j]
        j -= 1

    numbers [j+1] = key

print("Increasing order : ",numbers)

for i in range(1 , length):
    key = numbers[i]
    j = i-1

    while j >= 0 and numbers[j] < key :
        numbers[j+1] = numbers[j]
        j -= 1

    numbers [j+1] = key

print("Dicreasing order : ",numbers)
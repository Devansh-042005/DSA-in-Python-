# Return length of number

number = int(input("Enter Number : "))
count = 0
while (number > 0):
    number = number // 10
    count += 1
print("Length of number = ", count)

# Note : Not Valid for negative values and 0
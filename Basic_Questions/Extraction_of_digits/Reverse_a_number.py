# Return Reverse of number

number = int(input("Enter Number : "))
reverse_number = 0
while (number > 0) :
    reverse_number = number % 10 + reverse_number * 10
    number = number // 10
print("Reverse of number = ", reverse_number)
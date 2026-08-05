# Check number is palindrome or not

number = int(input("Enter Number : "))
reverse_number = 0
temp_number = number

while (temp_number > 0):
    reverse_number = temp_number % 10 + reverse_number * 10
    
    temp_number = temp_number // 10
if (number == reverse_number):
    print("Number is palindrome")
else:
    print("Number is not palindrome")
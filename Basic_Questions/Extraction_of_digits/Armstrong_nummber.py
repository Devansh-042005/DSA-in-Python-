# Check Number is armstrong or not

number = int(input("Enter number : "))
temp_number = number
length_of_number = len(str(number))
sum_of_numbers = 0

while (number > 0):
    remainder = number % 10 
    number = number // 10
    sum_of_numbers = (remainder ** length_of_number) + sum_of_numbers

if (sum_of_numbers == temp_number):
    print("Number is an armstrong number.")
else:
    print("Number is not an armstrong number.")
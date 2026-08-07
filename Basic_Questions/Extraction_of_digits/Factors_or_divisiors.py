# Give all factors of a number

number = int(input("Enter a number: "))

root_of_number = int(number ** 0.5)

for i in range (1 , ((root_of_number)+1)):
    if (number % i == 0):
        print(i)
        if ((number//i) != i):
            print(number // i)
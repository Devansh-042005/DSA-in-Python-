nums = [[1,2,3],[4,5,6],[7,8,9]]

rows = len(nums)
cols = len(nums[0])

print("Matrix : ")
for i in range(0,rows):
    for j in range(0,cols):
        print(nums[i][j] , end=" ")
    print( )

print("Upper triangle : ")
for i in range(0,rows):
    for j in range(0,cols):
        if i <= j:
            print(nums[i][j] , end=" ")
        else :
            print("* " ,end = " ")
    print( )

print("Lower triangle : ")
for i in range(0,rows):
    for j in range(0,cols):
        if i >= j:
            print(nums[i][j] , end=" ")
        else :
            print(" *" ,end = " ")
    print( )

print("Diagnol : ")
for i in range(0,rows):
    for j in range(0,cols):
        if i == j:
            print(nums[i][j] , end=" ")
        else :
            print("*" ,end = " ")
    print( )

print("2nd Diagnol : ")
for i in range(0,rows):
    for j in range(0,cols):
        if i + j == 2:
            print(nums[i][j] , end=" ")
        else :
            print("*" ,end = " ")
    print( )
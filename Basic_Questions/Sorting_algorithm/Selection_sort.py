arr = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    arr.append(num)


length = len(arr)

for i in range(0 ,length):
    max = i
    for j in range ( i+1 , length):
        if arr[max] < arr[j]:
            max = j
    arr[i],arr[max] = arr[max],arr[i]

print("Dicrising order : ",arr)

for i in range(0 ,length):

    max = i
    for j in range ( i+1 , length):
        if arr[max] > arr[j]:
            max = j
    arr[i],arr[max] = arr[max],arr[i]

print("Increasing order : ",arr)
        
        
    

numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)



# merge
def merge_sort(left , right):
    result = []
    i=0
    j=0
    n=len(left)
    m=len(right)

    while i < n and j < m:
        if (left[i] <= right[j]):
            result.append(left[i])
            i+=1
        else :
            result.append(right[j])
            j+=1

    if (i < n):
        while i < n:
            result.append(left[i])
            i += 1

    if (j < m):
        while j < m:
            result.append(right[j])
            j += 1
    return result

# Divide

def divide(number):
    length = len(number)

    if (length <= 1):
        return number

    mid = length // 2

    left_arr = number [:mid]
    right_arr = number [mid:]

    left = divide(left_arr)
    right = divide(right_arr)

    return merge_sort(left,right)

print ("Increasing order : ",divide(numbers))

# merge
def merge_sort(left , right):
    result = []
    i=0
    j=0
    n=len(left)
    m=len(right)

    while i < n and j < m:
        if (left[i] >= right[j]):
            result.append(left[i])
            i+=1
        else :
            result.append(right[j])
            j+=1

    if (i < n):
        while i < n:
            result.append(left[i])
            i += 1

    if (j < m):
        while j < m:
            result.append(right[j])
            j += 1
    return result

# Divide

def divide(number):
    length = len(number)

    if (length <= 1):
        return number

    mid = length // 2

    left_arr = number [:mid]
    right_arr = number [mid:]

    left = divide(left_arr)
    right = divide(right_arr)

    return merge_sort(left,right)

print ("Decreasing order : ",divide(numbers))
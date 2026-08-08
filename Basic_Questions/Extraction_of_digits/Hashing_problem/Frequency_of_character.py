# Calculate given Charaters frequecy in an array and store in dictionary 

string = "ayafftttkammk"
given_string = ['a' , 'f' , 'g' , 't' , 'l' , 'k']

frequency_count = {}

for ch in string :
    if ch in given_string:
        if ch in frequency_count :
            frequency_count [ch] += 1
        else :
            frequency_count[ch] = 1

print (frequency_count)


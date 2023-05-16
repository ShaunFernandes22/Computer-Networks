import random

string = input("Enter a string : ")
pri = ""
count = 0
start = 0
end = 0
n = len(string)

while end < len(string):
    i = random.randint(2,9)
    if i > n and n > 0:
        i = n + 1
    n -= i - 1    
    end += i - 1
    pri += str(i) + string[start:end] +'\n'
    start = end 
    count += 1
    
print(pri)    
print(f"Total frames created : {count}")     

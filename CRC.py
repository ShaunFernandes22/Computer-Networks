# binary = "110011001100"
# binary = "1100101011011"
binary1 = input("Enter the binary string ")
m = len(binary1)
binary = list(binary1)

# div = "10101"
div1 = input("Enter the divisor ")
n =len(div1)
div = list(div1)

choice = int(input("Enter :\n1. For generating CRC \n2. For Checking CRC "))
if choice == 1:
    num = 0
    while num < n-1:
        binary.append('0')
        num +=1
    m += n-1    
    
temp=[] # stores part of dividend at a time 
subtr=[] # stores number that would be subtracted as in real division (here divisor or zeroes)

zeroes = []
for i in range(n):
    zeroes += '0'

# copy first n bits (divisor len) in temp 
for j in range(n):
    temp.append(binary[j])

position = n #points to next index of binary
quotient=""
# print(temp)
#XOR DIVISION
while position <= m: # when position == m index bound, so nothing is carried down but its reqd to get last remainder  
    
    # deciding subtr and quotient
    if temp[0] == '1':
        subtr = div
        quotient += '1'
    else:
        subtr = zeroes
        quotient += '0'
  
    # print(subtr)        
    # print("--------------------------------------")

    #loop to perform XOR of all bits
    for i in range(n):
        if (subtr[i] == temp[i]):
            temp[i] = '0'
        else:
            temp[i] = '1'
    
    temp.pop(0) #1st bit is not reqd, starting from 2nd(n-1 bits reqd)
    
    if position < m: # carry next bit down
        temp.append(binary[position])
    position += 1

    # print(temp)    
   
rem = ""
for i in temp:
    rem += i

print("\nThe quotient is",quotient)
print("The remainder is",rem)

if (choice == 1):
    print("The generated CRC is", binary1+rem)

else:
    check = int(str(rem),2)
    if (check == 0):
        print("Acceptable, the correct message is received")
    else: 
        print("Not Acceptable, there is a bit error")        

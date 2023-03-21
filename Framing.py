import PyPDF2
import random

pdfFileObj = open('lorem-ipsum.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
pageObj = pdfReader.pages[0]

string = pageObj.extract_text()
Ascii =''
Binary =''

for char in string:
    Ascii += str(ord(char))
    Binary += str(bin(ord(char))[2:])

with open('ascii.txt', 'w') as f:
    f.write(Ascii)
with open('binary.txt', 'w') as f:
    f.write(Binary)

pri = ''
wri = ''

choice = int(input("Enter choice\n 1.Character count \n 2.Bit Stuffing \n 3.Byte Stuffing\n"))

#   1. Character Count 
if (choice==1):
    count = 0
    start = 0
    end = 0
    n = len(string)
    while end < n:
        i = random.randint(1,8)
        end += 2**i - 1
        wri += str(2**i) + string[start:end] +'\n'
        pri += f"\033[31m{(2**i)}\033[0m" + string[start:end] + ' '
        start = end
        count += 1
    with open('char_count.txt', 'w') as f:
        f.write(wri)
    print(pri)
    print("Total frames created: ", count)

#   2. Bit Stuffing
elif (choice == 2):
    ct = 0 
    start = 0
    end = start + 128
    n = len(Binary)
    padding = 128 - (len(Binary) % 128)
    if (padding != 0):
        Binary = Binary + "1"
        for i in range(0, padding-1):
            Binary = Binary + "0"
    for i in range(len(Binary)//128):
        wri += Binary[start:end] +'0' 
        pri += Binary[start:end] + "\033[31m0\033[0m"
        start = end
        end += 128
        ct +=1 
    with open('bit_stuff.txt', 'w') as f:
        f.write(wri)
    print(pri)
    print("Total frames of 128 bits generated : ", ct)

# 3.    Byte Stuffing
elif(choice==3):
    start = 0
    end = 0
    c = 0
    n = len(string)
    while end < n:
        i = random.randint(0,8)
        end += 2**i
        wri += string[start:end] + 'ESC' + '\n'
        pri += string[start:end] + "\033[31mESC\033[0m" + '\n'
        start = end
        c+=1
    with open('byte_stuff.txt', 'w') as f:
        f.write(wri)
    print(pri)    
    print("Total byte frames " + str(c))   

else:
    print("Invalid choice")    

pdfFileObj.close()


 
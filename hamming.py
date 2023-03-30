#maintained even parity for codeword generation and error correction
# all computations done on string in ascending order p1, p2, d3, ....
# just displayed them in reverse order as per notation 
# for identification the parity bits and corrected bits are integers while rest are chars in list

def main():
# 1.  ------       Codeword generation    ------
    print("CODEWORD GENERATION ")
    # binary = input("Enter a string of 0's and 1's whose codeword you want ")
    char = input("Enter any character i.e size of 1 byte or 8 bits ")
    binary = ""
    for ch in char:
        binary += '0' + bin(ord(ch))[2:]

    # binary = "1011"
    # binary = "01100010"

    # reversing as data bits are assigned in reverse order only
    binary = reverse(binary)
    m = len(binary)
    # calculate r 
    r = 0
    while (2**r < m + r + 1):
        r+=1

    total = m + r

    # created list and stored possible powers of 2
    p =[]
    for i in range(r):
        p.append(2**i)

# displaying format of codeword
    count=0; cp=0
    hamm_disp=[] 
    datastream=[]
    for i in range(1, total+1):
        if i == 2**count:
            hamm_disp.append('P' + str(i))
            datastream.append('P' + str(i))
            count += 1
        else:
            hamm_disp.append('D' + str(i))   
            datastream.append(binary[cp])
            cp += 1
    # print(hamm_disp)
    # print(datastream)
    print(reverse(hamm_disp))

# find parity bits 
    for i in p:
        datastream[i-1] = codeWord(i, datastream, total)
    # count=0
    # for i in range(1, (2**r)):   
    #     if i == 2**count:
    #         datastream[i - 1] = codeWord(i, datastream, total)
    #         count +=1
    # print(datastream)
    print(reverse(datastream))


# #     ------       2.   Error correction hamming code     ------
    print("\nHamming code ERROR CORRECTION ")
    faulty = input("Enter a codeword having 1 bit error ")
    # faulty = "010000011000"
    faulty = reverse(faulty)
    total = len(faulty)
    # calculate r
    r = 0
    while(2**r < total+1):
        r+=1
    p =[]
    for i in range(r):
        p.append(2**i)    
    copy = []
    for i in range(total):
        copy.append(faulty[i])
    # print(copy)    

# checking and storing parity bits which don't match even parity in a list i.e. p1, p2, p4, p8...
    seq =[object() for _ in range(r)]
    
    count = 0
    for i in p:
        seq[count] = errDetect(i, copy, total)
        count += 1
    # count=0
    # for i in range(1, (2**r)):   
    #     if i == 2**count:
    #         seq[count]  = errDetect(i, copy, total)
    #         count +=1
    # print(seq)

    # #reverse the seq as  we want p8, p4, p2, p1..
    seq.reverse()
    # create binary number with list elements
    binr = 0
    for i in range(r):
        binr = binr*10 + seq[i]
    # decimal to binary direct py method available using stringify and int(bin, 2)
    # binr = str(binr)    
    dec = int(str(binr), 2)
    # print(dec)    
    
    # # changing the reqd bit
    if dec!=0:
        print(f"Error present in bit {dec}")
        if (copy[dec-1] == '1'):
            copy[dec-1] = 0
        else:
            copy[dec-1] = 1
        print("Corrected CodeWord :")
        print(reverse(hamm_disp))
        print(reverse(copy))
    else: 
        print("Codeword is correct")

# reverse string or list
def reverse(item):
    return item[::-1]

# loop goes to the reqd data bits for particular parity bit to count no of 1's 
def sumOf(i, list, total):
    sum = 0
    ct = 0
    num = i
    while(num <= total):
        if (num > i and list[num - 1] == '1'):
            sum += 1
        ct += 1
        if (ct == i):
            num += i + 1
            ct = 0
        else:
            num += 1
    return sum                

#  function to generate parity bits
def codeWord(i, datastream, total):
    sum = sumOf(i, datastream, total)
    if sum%2 == 0:      #parity bit
        par = 0 
    else:
        par = 1

    return par  

#  function to detect error (i.e parity bits that don't match the even criteria)
def errDetect(i, copy, total):
    sum = sumOf(i, copy, total)
    if ((sum%2 == 0 and copy[i-1] == '1') or (sum%2!=0 and copy[i-1] == '0')):
        val = 1
    else:
        val = 0

    return val

main()

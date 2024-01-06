def decToBin(num):
    bin = ''
    while(num>0):
        rem = num%2
        if(rem == 1):
            bin+='1'
        else:
            bin+='0'
        num = num//2
    return bin[::-1]

print("Binary Number : "+decToBin(7))
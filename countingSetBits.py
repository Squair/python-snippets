#This program allows you to enter a number n and count the total number of set bits between 1 and n

#Count set bits in an integers
def countBits(n):
    bits = 0
    while(n):
        #AND least significant digit and then shift bits right until loop exits
        bits += n & 1
        n >>= 1
    return bits

def totalSetBits(i):
    #Add 1 to loop range so it hits upper bounds of number entered
    totalBits = 0
    #Start at one rather than 0 as 0 will never have any set bits
    for x in range(1, i + 1, 1):
        print(str(x) + " : " + str(countBits(x)))
        totalBits += countBits(x)
    return totalBits

#Get input for number n and print the result
n = int(input("Enter number n to print number of set bits in numbers 1 to n: "))
print("Total set bits between 1 and " + str(n) + ": " + str(totalSetBits(n))) 
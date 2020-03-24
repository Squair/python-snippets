#Script to check if a number is a palindrome without converting to a string
import math

def isPalindrome(num):
    numList = []
    #Get length of number using log
    digits = math.ceil((math.log10(num))) - 1

    #Descending loop
    for i in range(digits, -1, -1):
        #Floor division using 10 to power i so number is less than 10, then get the modulus of 10
        numList.append((num // (10 ** i)) % 10)

    #Check the reverse of the list matches original
    return True if numList == numList[::-1] else False

#Driver data
print(isPalindrome(892))
print(isPalindrome(1))
print(isPalindrome(121))
print(isPalindrome(12344321))
print(isPalindrome(9991))

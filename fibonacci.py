import datetime

#Recursive fibonacci function
def fib(n):
    if n <= 1:
        return n; 

    #Using memoisation to speed up calculation by storing previously calculated values
    if (not fibArr[n-1] is None and not fibArr[n-2] is None):
        if (not fibArr[n-3] is None): fibArr[n-3] = None #Remove third previous to dealloc memory as fib only needs last two figures
        return fibArr[n-1] + fibArr[n-2]

    return fib(n-1) + fib(n-2); 

#Enter number to calculate fibonacii sequence to
length = int(input("Calculate fibonacci sequence to number: "))
fibArr = [None] * length

#Get datetime before and after calculation to see how long it took to calculate
now = datetime.datetime.now()

for i in range(1, length, 1):
    fibArr[i] = fib(i)

#Print the ending number out and time to calculate
print(fibArr[length -1 ])
print("That took " + str(datetime.datetime.now() - now) + " to process.")
input()


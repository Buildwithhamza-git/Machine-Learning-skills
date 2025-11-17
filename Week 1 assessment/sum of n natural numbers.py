#calculate sum of n natural numbers
n=int(input("Enter a number:"))
if(n==0):
    print("This is not a natural number!")
else:
    sum=int(n*(n+1)/2)
    print("sum of natural number is:", sum)
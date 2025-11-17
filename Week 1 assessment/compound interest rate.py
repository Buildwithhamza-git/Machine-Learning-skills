#calculate compound interest rate
P=float(input("Enter Principl value:" ))
R=float(input("Enter Interest Rate:"))
T=float(input("Enter time duration:"))
CI=(P*(1+R/100)**T-P)
print("The Compund Interest is:", CI)

#calculate cost price and selliong price of item
cost=int(input("Enter purchase cost price of item:"))
sale=int (input("Enter sell price of item:"))
profit=sale-cost
lose=cost-sale
if cost<sale:
    print("The seller gain profit!")
    print("The amount of profit is:",profit)
elif cost>sale:
    print("The seller gain lose!")
    print("The amount of lose is:",lose)
elif cost==sale:
    print("The seller no gain any profit or any lose")
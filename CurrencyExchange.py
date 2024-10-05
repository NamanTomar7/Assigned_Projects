print("\tRATE OF EXCHANGE:-")
print("\t1 Dollars= 84.3 Rupees\n")
f=84.3
user=input("Enter 'd' to convert Rupees into Dollar else 'r' for vice versa: ")
if user=='d':
    rupees=int(input("Enter Rupees: "))
    dollars=rupees/f
    dollars=round(dollars,3)
    print(rupees,"Rupees=",dollars,"Dollars")
elif user=='r':
    dollars=int(input("Enter Dollars: "))
    rupees=f*dollars
    rupees=round(rupees,3)
    print(dollars,"Dollars=",rupees,"Rupees")
else:    
    print("Invalid request")
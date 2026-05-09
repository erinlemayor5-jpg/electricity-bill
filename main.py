# Write a program to calculate the electricity bill.
# The bill is calculated by checking the number of units consumed.
#  Suppose the user is consuming less than 50 units. 
# The per-unit cost will be 2.60, and the tax on that bill will be 25.
#  If a user is consuming more than 50 but less than 100. 
# Then the per-unit cost will be 3.25, and the tax on that bill will be 35 
# If the user is coming more than 100 and less than 200. 
# Then the per-unit cost will be 5.26, and the tax will be 45 And above 200,
#  the cost of the unit is 8.45, and the tax is 75.

unit=float(input("enter the unit cosumed "))
if unit<50:
    print( (unit *2.60)+0.25)
elif unit>50 and unit<100:
    print((unit*3.25)+0.35)
elif unit>100 and unit<200:
    print((unit*5.26)+0.45)
else:
    print((unit*8.45)+0.75)




x = float(input("what is the value of x? "))
y = float(input("what's the value of y? "))

# or we can do this
#z = round(x+y) # round the value of x+y to the nearest integer
#print(f"{z:,}") # print the value of z with commas as thousands separators


z = round(x/y , 2) # round the value of x/y to 2 decimal places
print(z)
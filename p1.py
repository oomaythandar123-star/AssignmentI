x=int(input(" Enter 1st number:"))
y=int(input(" Enter 2nd number:"))

all_x=id(x)
all_y=id(y)

print("Allocation of  1st number:",all_x)
print("Allocation of  2nd number:",all_y)

hex_x=hex(x)
hex_y=hex(y)

print("hex of x:",hex_x)
print("hex of y:",hex_y)

print("Addition:",x+y)

print("Multiplication:",x*y)

if x > y :
    print("Subtraction",x-y)
    print("Division",x/y)
    
elif y > x :
    print("Subtraction",y-x)
    print("Division",y/x)


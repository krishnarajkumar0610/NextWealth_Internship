a = int(input("a : "))
b = int(input("b : "))

try:
    c = a / b
    print(c)
    b = True
except TypeError: 
    b = False
    print(TypeError)
finally:
    if b:
        print("Your calculation is done")
    else:
        print("It has error so can't calculate")
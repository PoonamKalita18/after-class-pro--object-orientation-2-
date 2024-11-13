class expression :
    x= int(input("enter a number "))
    y= int(input("enter another number "))
    o = input("enter an operator")
    if o == "+":
        print(x+y)
    elif o == "-":
        print(x+y)
    elif o == "*":
        print(x+y)
    elif o == "/":
        if y!=0:
            print(x/y)
    else :
        print("invalid")
    
    def __init__(self):
        print('expression created')
    
    def __del__(self):
        print('destructor called, expression deleted')

obj = expression()
del obj    
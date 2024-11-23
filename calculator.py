def calculator():
    a=int(input("Enter a NUMBER1"))
    v=int(input("Enter a number2"))
    print("choose operation: + , -, *, / , **")
    b=input("Enter operation:")
        
    def add(a,v):
        print("The addition is",a+v)
    def sub(a,v):
        print("The subtraction is",a-v)
    def multiply(a,v):
        print("The multiply is",a*v)
    
    def divide(a,v):
        if v==0:
            raise ValueError("syntax error")
        print(a/v)
    def expo(a,v):
        print(f"the power of {a} and {v} is:{a**v}")
    if b=="+":
        add(a,v)
    elif b=="-":
        sub(a,v)
    elif b=="*":
        multiply(a,v)
    elif b=="/":
        try:
            divide(a,v)
        except ValueError as e:
            print(e)
    elif b=="**":
        expo(a,v)
    else:
        print("INVALID OPERATION")
calculator()


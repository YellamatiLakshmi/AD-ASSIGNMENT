#Program - 01
def div(a,b):
    return a/b
div(4,2)

#Program - 02
def div(a,b):
    print(a/b)
    if a<b :
        a,b = b,a
    return a/b
div(2,4)

#Program - 03
def dev_func(func):
    def inner(a,b):
        if a < b :
            a, b = b, a
        return func(a,b)
    return inner
@dev_func
def div(a,b):
    return a/b
print(div(2,4))


 #Program - 04
def smart_Dev(func):
    def inner(a,b):
        if b==0:
            print("Error : Cannot divide by zero")
            return
        if a > b:
            a,b = b,a
        return func(a,b)
    return inner
@smart_Dev
def div(a,b):
    return a/b
print(div(4,0))

#Checking if the two numbers multplication is >20 then perform division
def dev_dec(func):
    def check(a,b):
        if a* b > 20:
            return a/b
        else:
            return a * b
    return check
@dev_dec
def multiply(a,b):
    return a * b 
print(multiply(100,25))
    

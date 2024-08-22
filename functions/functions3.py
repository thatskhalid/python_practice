def add(x, y):
    z = x + y
    return z #z is a local variable for this function
             #this stored value can then be assigned to something else later on
               
def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z 

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

#invoking a function just executes a block of code
#returning a function returns a specific value to where the function was called 
#^it can then further be used for something else
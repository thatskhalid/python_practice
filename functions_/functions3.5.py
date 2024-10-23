def addition(x, y):
    
    total = x + y #total is a local variable for this function
    return total 


answer = addition(3, 4) #here I'm assigning a new variable to whatever the total answer was in the function "addition"
                        #here we're also calling the function addition and sending back arguments to the parameters x and y

print(answer) #we're printing the new variable
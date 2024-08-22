#varying aount of arguments
#"*args" and "**kwargs"



def add (*nums): #we are using the unpacking operator
    total = 0    #unpacking operator is important, parameter can be named anything
    for num in nums:
            total += num
    return total 
        

print(add(1,2,3, 4))
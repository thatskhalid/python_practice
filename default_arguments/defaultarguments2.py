import time

def count(end , start =0): #lets make a default value of zero, but make sure it's AFTER the positional argument
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")
    
    
count(10, 5) #second argument will override the default start value (which is zero)
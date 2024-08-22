#an argument preceded by an identifier, helps with readability, order of arguments doesn't matter!


def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
    
    
#hello("Hello", "Mr.", "Khalid", "Mahmood")

hello(title = "Mr." , first = "Khalid", greeting = "Hello" , last = "Mahmood") #can be out of order as long as keywords are set     
                                                                               #if we're using keywords and position, make sure
                                                                               #the positional arguments are first
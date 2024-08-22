def shipping_label(*args, **kwargs): #need args first if using both
    for arg in args:
        print(arg, end=" ") #the arg gets printed first, then a space to space out the first, middle, last namess
    print()
    #for value in kwargs.values():
    #    print(value, end=" ")
    
    if "apt" in kwargs and "pobox" not in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
        

        
    elif "pobox" in kwargs and "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
        print(f"{kwargs.get('pobox')}")
        
    elif "pobox" in kwargs:
        print(f"{kwargs.get('pobox')}")
        
        
    else:
        print(f"{kwargs.get('street')}")
         #this if statement checks to see if there is a apt # or not, this way "none" doesn't get printed
         
         
         
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Khalid", "Zubair", "Mahmood",
               street = "123 Main St.",
               apt ="#100",
               pobox ="PO BOX: 1001",
               city = "Joliet",
               state = "IL",
               zip = "12345")

#I got rid of Mr. and apt# and this still works
#I kinda mae this more complicated with the if/else statements, but that's only if apt or pobox are present
#rest of the args and kwargs should still work 
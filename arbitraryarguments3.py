#kwargs or keyword arguments

def print_address(**kwargs): #parameter name can be anyhting, but use the ** unpacking operator
    for key, value in kwargs.items(): # <- value is a values method
        print(f"{key}: {value}")


print_address(street="123 Main St", 
              apt = "100", # <- we added this in after we set our kwargs parameters, and it still worked!
              city="Joliet", 
              state="IL", 
              zip="12345", )


#this a dict, so u can print either the key or value
#apt was packed into a dictionary
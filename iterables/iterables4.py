#dictionaries

my_dictionary = {"A": 1 , "B":2 , "C":3 }

#for key in my_dictionary: #so this is for the KEY
#    print(key)            #look below for the value
        
        
        
#for value in my_dictionary.values(): #returns the values in the keys as iterables
#    print(value)                     #for keys and values, look below


for key, value in my_dictionary.items():
    print(f"{key} = {value}") #use a f to make this look better
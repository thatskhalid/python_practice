'''
class Car: #we need a speacial method called a constructor, similar to a function
    def __init__(self, model, year, color, for_sale): # we need this to construct object <-- self means this object rn
        #make sure to set the parameters after self
        
        self.model = model #this is important, once we receive a model, we will assign it to this object
        self.year = year
        self.color = color
        self.for_sale = for_sale
'''
from car import Car #okay so we moved the Class to a new file, make sure new file is lowercase, then import class name
        
car1 = Car("WRX" , 2017, "black" , False) #kinda like a function, we need to give arguments now, and self is already provided, so don't add it!
car2 = Car("Supra", 2020, "white" , False )  
car3 = Car("Viper", 2017, "orange", False) 
  
  
'''        
print(car1.model)       #<- this dot is the attribute access operator, gives us the attribute
print(car1.year) 
print(car1.color) 
print(car1.for_sale) 
'''
#car2.drive()

car3.describe()
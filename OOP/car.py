class Car: #we need a speacial method called a constructor, similar to a function
    def __init__(self, model, year, color, for_sale): # we need this to construct object <-- self means this object rn
        #make sure to set the parameters after self
        
        self.model = model #this is important, once we receive a model, we will assign it to this object
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
#methods are actions that our object can perform
    def drive(self): #self is provided?
        print(f"You drive the {self.color} {self.model}") #self refers to the object we're currently working with
                                             #notice the attribute access operator "."
    def stop(self):
        print(f"You stopped the {self.color} {self.model}")
        
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
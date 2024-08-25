#class variables = shared among all instances of a class
#                  defined outside the constructor
#                  allows you to share data among all objects created from that class 

#instance variables are defined inside the constructor (the def __init__(self, model, year) thing)
#class variables are defined OUTSIDE the constucutor 

#class variables are shared among all instances in a class, like cars having 4 wheels 
#instance variables are specific for each object, like car model

class Student:
    
    graduating_year = 2025
    number_of_students = 0
    
    def __init__(self, name, age): #again, self refers to the object we're currently working with
        self.name = name
        self.age = age
        
        Student.number_of_students +=1 #here we are modifying a class variables, every object will +=1
        
        #^ these instance variables are defined within the constructor
        
                
student1 = Student("Khalid", 24)
student2 = Student("Hummzah", 23)
student3 = Student("Taaha", 22)
student4 = Student("Ali", 23)

print(student1.name)
print(student1.age)

print(Student.graduating_year) #its better to access a class variable by Class Name, not by object

#print(student1.graduating_year) this works too, but it's better to be more clear that graduating_year is a CLASS variable

print(Student.number_of_students)

print(f"My graduating class of {Student.graduating_year} has {Student.number_of_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
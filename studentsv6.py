# A class is a code template for creating objects
# def__init__(self): instance method to initialize a specific object when you create it
# self to store in the current object and it has to come first
# ValueError to create your own exception, their has been an error
# classes can have functions bulid in not just variables or instance variables aka methods
class Student:
    def __init__(self, name, house,):
        self.name = name
        self.house = house
        
# dunder str message   
    def __str__(self):
        return f"{self.name} from {self.house}"
    
# @property decorator allows a function to be accessed like an attribute.
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    @property
    def house(self):
        return self._house
    
# setter decorator
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
        
def main():
        student = get_student()
        print(student)

def get_student():
       name = input("Name: ")
       house = input("House: ")
       
# methods constructor call it constucts a student object
       return Student(name, house,)
   
if __name__ == "__main__": 
    main()

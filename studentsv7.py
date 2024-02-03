# A class is a code template for creating objects
# def__init__(self): instance method to initialize a specific object when you create it
# self to store in the current object and it has to come first
# classes can have functions bulid in not just variables or instance variables aka methods
class Student:
    def __init__(self, name, house,):
        self.name = name
        self.house = house
        
# dunder str message   
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
        
def main():
        student = Student.get()
        print(student)   
if __name__ == "__main__":
    main()

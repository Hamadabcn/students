# A class is a code template for creating objects
# def__init__(self): instance method to initialize empty object when you create it
# self to store in the current object and it has to come first
# ValueError to create your own exception, their has been an error
# classes can have functions bulid in not just variables or instance variables aka methods
class Student:
    def __init__(self, name, house, patronus):
        if not name:
# control over correctness
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff","Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
#  dunder str message   
    def __str__(self):
        return f"{self.name} from {self.house}"
    def charm(self):
        match self.patronus:
            case "stag":
                return "🦌"
            case "Otter":
                return "🐿️"
            case "jack russel terrier":
                return "🐶"
            case _:
                return "🪄"
def main():
        student = get_student()
        print("Expecto Patronum!")
        print(student.charm())

def get_student():
       name = input("Name: ")
       house = input("House: ")
       patronus = input("Patronus: ")
# methods constructor call it constucts a student object
       return Student(name, house, patronus)
   
if __name__ == "__main__": 
    main()
    
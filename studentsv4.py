# A class is a code template for creating objects
# def__init__(self): instance method to initialize empty object when you create it
# self to store in the current object and it has to come first
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
def main():
    student = get_student()
# attributes or instances variables
    print(f"{student.name} from {student.house}" )

def get_student():
    name = input("Name ")
    house = input("House ")
# methods constructor call it constucts a student object
    student = Student(name, house)
    return student
    
if __name__ == "__main__": 
    main()
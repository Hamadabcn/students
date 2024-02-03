def main():
    student = get_student()
    if student ["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}" )

# (name, house) tuple to collect value similar to a list but inmutable
# [name, house] to use a list same idea but mutable
# dictionarys like lists are mutable
# student = [] create a variable and initialize to an empty dictionary
# student["name"] ["house"] = input("name: ") = input("house: ") to set two keys inside of this dictionary
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}
if __name__ == "__main__": 
    main()
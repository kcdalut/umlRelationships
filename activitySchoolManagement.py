class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name: {self.name}\nAge: {self.age}")

person1 = Person("Lanz", 14)
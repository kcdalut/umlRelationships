class Person():
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age

    def display_details(self):
        print(f"Name: {self.name}\nAge: {self.get_age()}")

        # Reflection: Using get_age() is better because it allows controlled access
        # to private data without directly exposing or modifying the attribute.
        # This helps protect the data and maintain encapsulation.

person1 = Person("Lanz", 14)

print(person1.get_age())
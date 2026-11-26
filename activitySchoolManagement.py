class Person():
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age

    def display_details(self):
        return f"Name: {self.name}\nAge: {self.get_age()}"

        # Reflection: Using get_age() is better because it allows controlled access
        # to private data without directly exposing or modifying the attribute.
        # This helps protect the data and maintain encapsulation.

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self):
        return f"{self.name} is studying."
    def role(self):
        return f"{self.name} is a Student"

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def teach(self):
        return f"{self.name} is teaching."
    def role(self):
        return f"{self.name} is a Teacher"

person1 = Person("Khiane", 30)
print(person1.display_details())

student1 = Student("Lanz", 14)
print(student1.display_details())
print(student1.study())
print(student1.role())

teacher1 = Teacher("Dalut", 40)
print(teacher1.display_details())
print(teacher1.teach())
print(teacher1.role())
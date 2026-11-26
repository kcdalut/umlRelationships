from abc import ABC, abstractmethod

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

    @abstractmethod
    def role(self):
        pass

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

class Principal(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def manage_school(self):
        return f"{self.name} is managing the school."
    def role(self):
        return f"{self.name} is the Principal"

class GuidanceCounselor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def assist_students(self):
        return f"{self.name} is assisting students."
    def role(self):
        return f"{self.name} is a Guidance Counselor"
    
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

principal1 = Principal("Mr. X", 55)
print(principal1.display_details())
print(principal1.manage_school())
print(principal1.role())

guidance_counselor1 = GuidanceCounselor("Ms. Y", 45)
print(guidance_counselor1.display_details())
print(guidance_counselor1.assist_students())
print(guidance_counselor1.role())

people = [student1, teacher1, principal1, guidance_counselor1]
for person in people:
    print(person.role())
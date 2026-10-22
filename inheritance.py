class Person:
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age

  def introduce(self):
    print(f"Hello, I am {self.name} and I am {self.age} years old.")


class Student(Person):
  def do_subject(self, subject: str):
    print(f"{self.name} is doing {subject}.")

lara = Student("Lara", 14)
lara.introduce()
lara.do_subject("Math")

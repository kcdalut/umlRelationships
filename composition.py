class Lesson:
  def __init__(self, name: str, code: str):
    self.name = name
    self.code = code

  def __del__(self):
    print(f"Destroyed lesson {self.name}")

class Course:
  def __init__(self, name: str, capacity: int):
    self.name = name
    self.capacity = capacity
    self.lesson = Lesson("Welcome", "001")

  def __del__(self):
    print(f"Destroyed course {self.name}")

math_3 = Course("Math 3", 100)
print(math_3.lesson)

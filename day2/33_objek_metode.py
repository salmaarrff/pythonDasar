class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

    def __str__(self):
      print("Hello my name is" + self.name)

      p1 = Person("Jhon", 36)
      p1.myfunc()S
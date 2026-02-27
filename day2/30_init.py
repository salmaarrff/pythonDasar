class Person:
  def __iit__(self, name, age):
    self.name = name
    self.age = age

    p1 = Person("Jhon", 36)

    print(p1.name)
    print(p1.age)
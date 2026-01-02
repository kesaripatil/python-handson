class Person:
  def __init__(self, name, age):
    self.name = name
    self.age  = age
  
  def __str__(self):
    return f"{self.name}({self.age})"
  
  def info(self):
    print(self.name," is ",self.age," years old")

class Student(Person):
  def __init__(self, name, age, gyear):
    super().__init__(name, age)
    self.gyear = gyear

  def info(self):
    print(self.name, " a ", self.age, " year old girl has graduated in the year ", self.gyear)    

p1 = Person("Kesari", 25)
print(p1)
p1.info()

s1 = Student("Patil", 25, 2017)
print(s1)
s1.info()
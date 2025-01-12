class Parrot:
  species="Bird"

  def _init_(self,name,age):

    self.name=name
    self.age=age

def sing(self,song):
  return "{} sings {} song ".format(self.name,song)

def dance(self):
  return self.name," is dancing now"

p1=Parrot("Rio",2)
print(p1.name, "is a ",p1.species," and is ",p1.age," years old")
print(p1.sing("happy"))
print(p1.dance())

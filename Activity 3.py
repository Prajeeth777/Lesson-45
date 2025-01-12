class Parrot:
  species="Bird"

  def _init_(self,name,age):

    self.name=name
    self.age=age
p1=Parrot("Rio",3)
p2=Parrot("Blu",2)

print(p1.name, " is a ",p1.species)
print(p2.name, " is a ",p2.species)

print(p1.name, " is ",p1.age," years old")
print(p2.name, " is ",p2.age," years old")
    

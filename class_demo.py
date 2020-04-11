class Actor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("in init method"+ self.name)
    def act(self):
        self.name = 'Sona'
        print("actor is acting")
    def __str__(self):
        print("in __str_()")
        return 'Actor:' + self.name
    def __lt__(self, other):
        if self.age < other.age:
            return True
        else:
            return False


a1 = Actor('smi',29)
#a1.name = 'ranveer'
a1.act()
print(a1.name)
a2 = Actor('bala',27)
a2.act()
print(a2.name)

print(id(a1), id(a2))

print(a1)
print(a1<a2)
print(a1>a2)
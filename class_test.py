class Person:
    ''' Person is a base class'''
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lna

    def dance(self):
        print("person with name" + " " + self.first_name + " " + self.last_name + " " + "is a dancer")
    age = 8

class Student(Person):
    ''' student class is child of Person class and inherits its variables and behaviour '''
    def __init__(self,fname,lname,year):
        Person.__init__(self,fname,lname)
        self.birth_year = year

    def biker(self):
        print(self.first_name+" "+ self.last_name+" is a biker")

    def blogger(style:"str")->"None":
        '''simply wrote this for practice purpose'''
        print("he is a blogger of style {}".format(style))

    count = 4



p1 = Person("smi","bala")
print("calling base class" +" " + p1.first_name +" " +p1.last_name)
p2 = Student("bal","smi",1990)
print("calling child class" + " "+ p2.first_name + " "+ p2.last_name +" "+ str(p2.birth_year))
p2.dance()
p2.biker()
#global count
Student.blogger("food")
#print(p2.count)
#Student.count = 3
#print(p2.count)
print(Student.count)
#print(Person.count)
#Student.count = 0
print(Person.age)
print(Student.age)

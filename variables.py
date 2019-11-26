class Student:
    #class variable
    school = 'HIll school'
    def __init__(self, name, age):
        #instance variables
        self.name = name
        self. age = age
    
    #instance method
    def msg(self):
        print(self.name+" "+self.age)

print(Student.school)

s1 = Student("s", '2')
print(s1.name)
print(s1.age)
print(s1.school)
s1.msg()

s2 = Student("d", '3')
print(s2.name)
print(s2.age)
print(s2.school)
s2.msg()

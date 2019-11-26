#instance, class and static methods
class Student: 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    #instance method
    def msg(self):
        print(self.name, self.marks)

    #class method
    @classmethod
    def get_percentage(cls, marks):
        return cls(name,str(int((200/600) * 100))) 

    #static method
    @staticmethod
    def get_age(age):
        if age <= 17:
            print("belong to school")
        else:
            print("too old")

s1 = Student('s', 2)
s2 = Student('w', 4)
s2 = Student.get_percentage(200)
s2.msg()
Student.get_age(17)
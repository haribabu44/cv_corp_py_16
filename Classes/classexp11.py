class Student:
    total=0
    def __init__(self,n,m):
        self.name=n
        self.marks=m
        Student.total=Student.total+1
    def result(self):
        if self.marks>35:
            return "pass"
        else:
            return "fail"
    @classmethod
    def update(cls,nt):
        cls.total=nt
    def grade(self):
        if self.marks>90:
            return "A+"
        elif self.marks>60 and self.marks<90:
            return "B"
        elif self.marks>50 and self.marks<60:
            return "c"
s1=Student("hari",92)
# print(Student.result(s1))
print(s1.grade())



class Student:
    passing_marks=40
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    def result(self):
        if self.marks>35:
            return "pass"
        else:
            return "fail"
    @classmethod
    def update_passing_marks(cls,nm):
        cls.passing_marks=nm
    @staticmethod
    def grade_category(marks):
        if marks>90:
            print("A+")
        elif marks>=80 and  marks<=90:
            print("A")
        elif marks>=60 and marks<80:
            print("B")
        else:
            print("D")
s1=Student("Hari",40)
# print(Student.result(s1))
# Student.update_passing_marks(20)
# print(Student.passing_marks)
Student.grade_category(85)






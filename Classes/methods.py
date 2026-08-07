class Student:
    School = "Chaitanya"
    def __init__(self,n,a,m):
        self.name = n
        self.age = a
        self.marks = m

    def display(self):
        self.show()
        sec = input("Enter Section : ")
        print(f"Section : {sec}")
        print(f"name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Marks : {self.marks}")

    def grade_category(self):
        self.display()
        print("Grade : ",end="")
        if self.marks>90:
            print("A+")
        elif self.marks>=80 and  self.marks<=90:
            print("A")
        elif self.marks>=60 and self.marks<80:
            print("B")
        else:
            print("D")

    @classmethod
    def update(cls,ns):
        if cls.vaild(ns):
            cls.School = ns
            cls.show()
        else:
            print("Invalid School name")

    @classmethod
    def show(cls):
        print(f"School name : {cls.School}")

    @staticmethod
    def vaild(ns):
        return len(ns) > 8


s1 = Student("Sai",21,85)
# s1.sec = "A"
# # s1.display()
# # s1.update("Narayana E-Techno School")
# s1.grade_category()
# Student.grade_category(s1)
print(s1.__dict__)
print(Student.__dict__)


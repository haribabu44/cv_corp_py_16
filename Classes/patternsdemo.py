# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j>=n+1:
#             print(i,end="")
#         else:
#             print(1,end="")
#     print()
# n=int(input())
# a=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if a%4==0:
#             print("*",end=" ")
#         else:
#             print(a,end=" ")
#         a=a+1
#     print()
# class Student:
#
#     college="AEC"
#
#     def __init__(self,name):
#         self.name=name
#
# s1=Student("Hari")
#
# print(Student.college)
# class Student:
#     total = 5
#
#     @classmethod
#     def add(cls):
#         cls.total += 1
# Student.add()
# print(Student.total)
class Student:

    college = "AEC"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def hello():
        print("Hello")

s1 = Student("Hari")

s1.hello()
Student.hello()
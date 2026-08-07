# class Student:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     def eligible(self):
#         if self.age>18:
#             print("eligible")
#         else:
#             print("not eligible")
#     def display(self):
#         print(f'{self.name}:{self.age}')
#         self.eligible()
# s1=Student("hari",15)
# s1.display()
# class Student:
#
#     total = 10
#
#     @classmethod
#     def show_total(cls):
#         print(cls.total)
#
#     def display(self):
#         Student.show_total()
# s1=Student()
# print(Student.__dict__)
# class Student:
#
#     @staticmethod
#     def hello():
#         print("Hello")
#
#     def display(self):
#         self.hello()
# s1=Student()
# s1.display()
# class Student:
#
#     def display(self):
#         print(self.name)
#
#     @classmethod
#     def test(cls):
#         cls.display()
# class Employee:
#     min_exp=5
#     def __init__(self,n,exp,dep):
#         self.name=n
#         self.experience=exp
#         self.department=dep
#     def eligible(self):
#         if self.valid():
#             return self.experience>5
#     @classmethod
#     def update(cls,np):
#         cls.min_exp=np
#     @staticmethod
#     def valid(exper):
#         if exper>5:
#             return True
# e1=Employee("hari",10,"hr")
#
# print(Employee.min_exp)
# print(e1.eligible())
# a=[10,20,30,40,34,23,56]
# a.sort()
# # a.append(70)
# # a.insert(1,23)
# for i in range (len(a)):
#     print(a[i])
# b=int(input())
# a=list(map(int,input().split()))
# print(a)
# b=int(input())
# a=list(map(int,input().split()))
# for i in range(len(a)):
#     fc=0
#     for j in range(1,a[i]+1):
#         if a[i]%j ==0:
#             fc=fc+1
#     if fc==2:
#         print(a[i],end="")
# a=list(map(int,input().split()))
# # print(a)
# # a[2]=50
# # print(a)
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         print(a[i])
a=list(map(int,input().split()))
for i in range(0,len(a)-1,2):
    a[i],a[i+1]=a[i+1],a[i]
print(a)



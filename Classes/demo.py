# class Student:
#     def __init__(self,n,a,s):
#         self.name=n
#         self.age=a
#         self.sec=s
#     def __repr__(self):
#         return f'Student({self.name})'
# s1=Student("hari",23,"A")
# s2=Student("ravi",23,"B")
# print(s1)
# class Student:
#     def __init__(self,m):
#         self.marks=m
#     def __add__(self, other):
#         return self.marks+other.marks
# s1=Student(12)
# s2=Student(13)
# print(s1+s2)





# class Bank:
#     def __init__(self,acc,pin):
#         self.account=acc
#         self.pin=pin
#         self.balance=0
#     def valid(self):
#         p=int(input("enter the pin"))
#         return self.pin==p
#     def __add__(self,other):
#         if other>=0:
#             self.balance=self.balance+other
#             return self.balance
#         else:
#             return "Invalid Money"
#     def __sub__(self,other):
#         if self.valid():
#             if 0<=other<=self.balance:
#                 self.balance=self.balance-other
#                 return self.balance
#             else:
#                 return "Insufficient funds"
#         else:
#             return "Wrong pin"
# b1=Bank(7382,123)
# print(b1+5000)
# print(b1-500)




class Loan:
    c_i=2
    def __init__(self,name,p):
        self.name=name
        self.p=p
    @staticmethod
    def loan_eligibility(sal):
        if sal>10000:
            return "eligible"
    @classmethod
    def update(cls,n_i):
        cls.c_i=n_i
    def total(self):
        if self.loan_eligibility(12000):
            k=self.p+(self.p*self.c_i)
            return k
l1=Loan("hari",20000)
print(l1.total())
l1.update(4)
print(l1.total())








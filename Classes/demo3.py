# n=int(input())
# if n>0:
#     a,b=0,1
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(a,end=" ")
#             c=a+b
#             a=b
#             b=c
#         print()
# p=2
# def np(a):
#     global p
#     count=0
#     c=0
#     while True:
#         fc=0
#         for i in range(1,p+1):
#             if p%i==0:
#                 fc=fc+1
#         if fc==2:
#             c=c+1
#             if c%2==1:
#                 print(p,end="")
#                 count=count+1
#             if count==a:
#                 break
#         p+=1
# n=int(input())
# for i in range(1,n+1):
#     np(i)
# #     print()
# def adding(a,b):
#     return a+b
# def fun2(a,b):
#     return adding (a+b,a-b)
# # print(fun2(10,7))
# def fun4(x):#x=34
#     def fun5():#creating function Object
#         nonlocal x
#         x=x+1
#         print(x)
#         # print(f'a:{a}')
#         # print(f'b:{b}')
#     return fun5
# l=fun4(10)
# l()
# l()
# l()
# # l(12,23)
class Student:
    def __init__(self,i,n,m):
        self.Id=i
        self.name=n
        self.marks=m
    def __gt__(self,other):
        return self.marks>other.marks
    def __le__(self,other):
        return self.marks<other.marks
    def __eq__(self,other):
        return self.marks == other.marks
    def __hash__(self):
        return hash(self.Id)
    def __repr__(self):
        return self.name
s1=Student(25,"hari",100)
s2=Student(23,"mani",13)
s3=Student(26,"raju",78)
s={s1,s2,s3}
print(s)





# def greet():
#     message="hi there "
#     def inner():
#         x="hi hari"
#         print(message)
#     return inner
# say_hi=greet()
# say_hi()
# def valid(fun):
#     def wrapper():
#         print("hi hello this is hari")
#         fun()
#         print("completed")
#     return wrapper
# @valid
# def hello():
#     print("welcome")
# a=hello
# # a()
# def my_decorator(fun):
#     def wrapper():
#         print("function is started")
#         fun()
#         print("function is done")
#     return wrapper
#
# @my_decorator
# def greet():
#     print("hello")
# a=greet
# a()
# def dec(fun):
#     def inner():
#         print("function is started this is inner class")
#         fun()
#     return inner
# @dec
# def greet():
#     print("hello")
# def my_decorator(fun):
#     def wrapper():
#         print("addition of 2 numbers is:",end="")
#         fun(12,13)
#         print("function completed")
#     return wrapper
#
#
# @my_decorator
# def greet(a,b):
#     print(a+b)
# c=greet
# c()
# def mul(*args):
#     total=1
#     for num in args:
#         total=total*num
#     return total
# print(mul(10,20,30,40,50))
# def student(name,age):
#     print(name,age)
# student(name="hari",age=21)
# class Student:
#     branch="batch16"
#     def __init__(self,N,A,B,C):
#         self.Name=N
#         self.Age=A
#         self.Branch=B
#         self.cgpa=C
# S1=Student("hari",22,"ai-ds",8.60)
# print(S1.Name)
# a=int(input())
# b=int(input())
# if a>b:
#     h=a
# else:
#     h=b
# k=h
# while True:
#     if h%a==0 and h%b==0:
#         print(h)
#         break
#     h=h+k
# n1=int(input())
# n2=int(input())
# if n1<=0 and n2<=0:
#     print("Invalid Inputs")
# elif n1<=0:
#     print("Invalid First Input")
# elif n2<=0:
#     print("Invalid Second Input")
# else:
#     a=max(n1,n2)
#     h=a
#     while True:
#         if a%n1==0 and a%n2==0:
#             print(a)
#             break
#         h=h+a
# n1=int(input())
# n2=int(input())
# n3=int(input())
# count=0
# if n1<=0:
#     count=count+1
# if n2<=0:
#     count=count+1
# if n3<=0:
#     count=count+1
# if count>=2:
#     print(" Sorry Invalid Inputs!")
# elif n1<=0:
#     print("Invalid First Input")
# elif n2<=0:
#     print("Invalid Second Input")
# elif n3<=0:
#     print("Invalid Third Input")
# else:
#     h=max(n1,n2,n3)
#     k=h
#     while True:
#         if h%n1==0 and h%n2==0 and h%n3==0:
#             print(h)
#             break
#         h=h+k

# n1=int(input())
# n2=int(input())
# n3=int(input())
# count=0
# if n1<=0:
#     count=count+1
# if n2<=0:
#     count=count+1
# if n3<=0:
#     count=count+1
# if count>=2:
#     print("Invalid Inputs")
# elif n1<=0:
#     print("Invalid First Input")
# elif n2<=0:
#     print("Invalid Second Input")
# elif n3<=0:
#     print("Invalid Third Input")
# else:
#     l=min(n1,n2,n3)
#     for i in range(l,0,-1):
#         if n1%i==0 and n2%i==0 and n3%i==0:
#             print(i)
#             break
# a=int(input())
# d=int(input())
# n=int(input())
# ap=0
# if n>0:
#     ap=(a+(n-1)*d)
#     print(f"Last Term value is :{ap:.3f}.")
# a=int(input())
# r=int(input())
# n=int(input())
# gp=0
# if n>0:
#     total=0
#     for i in range(n):
#         gp=a*(r**i)
#         total=total+gp
#     print(total)
# n=abs(int(input()))
# if n==0:
#     print("Invalid Input")
# else:
#     a,b=0,1
#     for i in range(1,n+1):
#         print(a,end=" ")
#         c=a+b
#         a=b
#         b=c
# n=abs(int(input()))
# if n==0:
#     print("Invalid Input")
# else:
#     a,b=0,1
#     for i in range(1,n+1):
#         print(a)
#         c=a+b
#         a=b
#
#         f=b=c
# n=int(input())
# f=1
# for i in range(n,0,-1):
#     f=f*i
# print(f)
# n=int(input())
# f=1
# if n<=0:
#     print("Invalid Inputs")
# else:
#     count=0
#     total=0
#     for i in range(n,0,-1):
#         f=f*i
#         count=count+1
#         total=total+f
#         if count>1:
#             print("+")
#         print(f)
#     print(f"={total}")
# n=int(input())
# f=1
# count=0
# total=1
# print(1,end="")
# for i in range(1,n+1):
#     # if n<0:
#     f=f*i
#     count=count+1
#     total=total+f
#     if count>0:
#         print(end="+")
#     print(f,end="")
# print(f'={total}')

# n=int(input())
# if n>=0:
#     sum=1
#     count=0
#     f=1
#     print(1,end="")
#     for i in range(1,n+1):
#         f=f*i
#         print(f)
#         sum=sum+f
#         print(sum)
#         count=count+1
#         if count>0:
#             print(end="+")
#         print(f,end="")
#     print(f"={sum}")
# else:
#     print("INvalid INput")
# n=int(input())
# f=1
# count=0
# total=1
# if n<=0:
#     print("Invalid inputs")
# else:
#     print(1,end="")
#     for i in range(1,n+1):
#         f=f*i
#         count=count+1
#         total=total+f
#         if count>0:
#             print(end="+")
#         print(f,end="")
#     print(f'={total}')
# n=int(input())
# count=0
# total=0
# if n>0:
#     a,b=0,1
#     while True:
#         if n<=
#         count=count+1
#         if count>1:
#             print(end=",")
#         print(a,end="")
#         c=a+b
#         a=b
#         b=c
#     print(total)
# n=int(input())
# f=1
# if n>=0:
#     for i in range(n,0,-1):
#         f=f*i
#     print(f)
# else:
#     print("Invalid InPut")

# n1=int(input())
# n2=int(input())
# total=0
# count=0
# if n1>=0 and n2>=0:
#     if n1>n2:
#         n1,n2=n2,n1
#     a,b=0,1
#     pos=0
#     while a<=n2:
#         if a>=n1:
#             pos=pos+1
#             if pos%2==1:
#                 count=count+1
#                 total=total+a
#         c=a+b
#         a=b
#         b=c
#     print(total/count)
#     # print(f'{total/count:.2f}')
# n=abs(int(input()))
# if n==0:
#     print("Invalid Input")
# else:
#     a,b=0,1
#     count=0
#     total=0
#     for i in range(1,n*2+1):
#         if i%2==1:
#             count=count+1
#             total=total+a
#         c=a+b
#         a=b
#         b=c
#     print(total/count)
# a=int(input())
# d=int(input())
# n=int(input())
# hp=0
# if n>0:
#     total=0
#     for i in range(n):
#         hp=1/(a+(i*d))
#         total=total+hp
#     print(f'{total:.2f}')
# else:
#     print("Invalid Input")
# n1=int(input())
# n2=int(input())
# if n1<=0 and n2<=0:
#     print("Invalid inputs")
# elif n1<=0:
#     print("Invalid first input")
# elif n2<=0:
#     print("invalid second input")
# else:
#     l=min(n1,n2)
#     for i in range(l,0,-1):
#         if n1%i==0 and n2%2==0:
#             print(i)
#             break
# n1=int(input())
# n2=int(input())
# n3=int(input())
# count=0
# if n1<=0:
#     count=count+1
# if n2<=0:
#     count=count+1
# if n3<=0:
#     count=count+1
# if count>=2:
#     print("Sorry Invalid Inputs!")
# elif n1<=0:
#     print("InvalId First Input")
# elif n2<=0:
#     print("Invalid Second Input")
# elif n3<=0:
#     print("InvaliD ThirD Input")
# else:
#     h=max(n1,n2,n3)
#     k=h
#     while True:
#         if h%n1==0 and h%n2==0 and h%n3==0:
#             print(h)
#             break
#         h=h+k
# class Students:
#     batch="batch16"
#     def __init__(self,n,a,b):
#         self.name=n
#         self.age=a
#         self.branch=b
#     # def display(self):
#     #     print({self.name,self.age,self.branch})
# s1=Students("Hari",21,"aids")
# print(s1.name)
# class Employee:
#     company="techi";bonus=0.2
#     def __init__(self,n,a,exp,sal):
#         self.name=n
#         self.age=a
#         self.exp=exp
#         self.salary=sal
#     def display_bonus(self,salary):
#         k=self.salary+(self.salary*self.bonus)
#         print(f'total_salary is {k}')
#     def display(self):
#         print(self.name,self.age,self.exp,self.salary)
# e1=Employee("hari",21,1,20000)
# e2=Employee("hari",21,1,20000)
# e2.display_bonus(20000)
# class Students:
#     school_name="Aruna Vidyalayam"
#     def __init__(self,n,a,id):
#         self.name=n
#         self.age=a
#         self.id_no=id
#     def age_validate(self,new_a):
#         self.new_age=new_a
#         if self.new_age>=18:
#             print(f"eligible")
#         else:
#             print("not eligible")
# a1=Students("hari",12,112,)
# print(a1.age)
# a1.age_validate(22)
# print(a1.new_age)
# a1.__dict__['grade']='A'
# print(a1.grade)
# x=12.3
# print(isinstance(x,(int,float)))
# print(isinstance(x,(str,list)))
# def sqrt(n):
#     if not isinstance(n,(int,float)):
#         print("type error")
#     return n**0.5
# print(sqrt("hari"))
# class Student:
#     pass
# S1=Student()
# S2=S1
# print(S1 is S2)
# print(S1)
# print(S2)
# r=abs(int(input()))
# c=abs(int(input()))
# a=0
# if r>0 and c>0:
#     for i in range(1,r+1):
#         for j in range(1,c+1):
#             a=a+1
#             print(a,end=" ")
#         print()
# n=int(input())
# if n>0:
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i==j:
#                 print(i,end=" ")
#             else:
#                 print("0",end=" ")
#         print()
# n=abs(int(input()))
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if i>=j:
#             print(i,end=" ")
#         else:
#             print(j,end="")
#     print()





# a=5
# n=2
# c=0
# v=1
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(n,end=" ")
#         if c>0:
#             if v==1:
#                 n+=1
#             else:
#                 v=0
#         c+=1
#     print()
#     if c>0:
#         if v==1:
#             n+=1
#         else:
#             v=0



# a=5
# n=2
# v=1
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(n,end=" ")
#         if(j<i):
#             n+=2
#     n=n+1
#     print()

# a=5
# n=2
# v=1
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(n,end=" ")
#         n+=2
#     n=n-1
#     print()
# r=int(input())
# c=int(input())
# for i in range(1,r+1):
#     # for j in range(1,c+1):
#     #     print("*",end=" ")
#     print(" * "*c,end=" ")
#     print()
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f'{i,j}',end=" ")
#     print()

# n=int(input())
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(i,end=" ")
#     print()
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(" ",end=" ")
    for j in range(1,n+1):
        print("*",end=" ")
    print()
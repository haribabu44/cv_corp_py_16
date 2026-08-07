# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,oth):
#         return Vector(self.x+oth.x,self.y+oth.y)
#     def __sub__(self,oth):
#         return Vector( self.x-oth.x,self.y-oth.y)
#     def __str__(self):
#         s=f'Vector:{self.x,self.y}'
#         return s
#     def __repr__(self):
#         return f'Vector:{self.x,self.y}'
#
# v1=Vector(7,8)
# v2=Vector(6,7)
# v3=Vector(3,4)
# print(v1+v2+v3)
# v4=v1+v2+v3
# print(v4)
from classmethod1 import cls


# print(v1)
# l=[v1,v2]
# print(l)

# r=int(input())
# c=int(input())
# if r<0 and c<0:
#     print("Invalid Inputs")
# else:
#     for i in range(1,r+1):
#         for j in range(1,c+1):
#             print("*",end=" ")
#         print()
#
# n=int(input())
# if n>0:
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i==j:
#                 print(i,end="")
#             else:
#                 print("0",end="")
#         print()
# n=int(input())
# a=1
# if n>0:
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#                 print(a,end=" ")
#                 if a==1:
#                     a=0
#                 else:
#                     a=1
#         print()
#         if a==0:
#             a=1
#         else:
#             a=0
# r=int(input())
# c=int(input())
# a=1
# for i in range(1,r+1):
#     h=1
#     for j in range(1,c+1):
#         if h>1:
#             print(end="*")
#         print(a,end="")
#         a=a+1
#         h=h+1
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
# n=int(input())
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if i>=j:
#             print(i,end="")
#         else:
#             print(j,end="")
#     print()
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print((n-i+1)*2,end=" ")
#     print()
# n=int(input())
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()
#     And Given Input must be in the range of 1 to 6 either Positive or Negative or else Print Range Exceeded.
# n=abs(int(input()))
# if n==0:
#     print("Invalid Input")
# elif n>=1 and n<=6 :
#     c=65
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(chr(c),end="")
#             c=c+1
#         print()
# n=int(input())
# a=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(a,end="")
#         a=a+1
#     print()
# n=int(input())
# for i in range(1,n+1):
#     print(" "*(i-1),end="")
#     for j in range(1,n-i+2):
#         print("*",end="")
#     print()
# n = int(input())
# if n == 0:
#     print("Invalid Input")
# else:
#     a = 2
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(a, end="")
#             a = a + 2
#         print()
#         a = a - 1
# n=int(input())
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(j,end="")
#     print()
# n=int(input())
# if n>0:
#     for i in range(1,n+1):
#         if i%2==1:
#             for j in range(1,n-i+2):
#                 print(j,end=" ")
#             print()
#         else:
#             for j in range(n-i+1,0,-1):
#                 print(j,end=" ")
#             print()
        #     for j in range(1,n+1):
        #         print(j,end=" ")
        #     print()
        # else:
        #     for j in range(n-1,0,-1):
        #         print(j,end=" ")
        #     print()
# n=int(input())
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(j,end="")
#     print()
# n=int(input())
# if n>0:
#     for i in range(1,n+1):
#         if i%2==1:
#             for j in range(1,n-i+2):
#                 print(j,end="")
#             print()
#         else:
#             for j in range(n-i+1,0,-1):
#                 print(j,end="")
#             print()
# n=int(input())
# if n>0:
#     a=1
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(a,end="")
#             a=a+2
#         print()

# r=int(input())
# s=int(input())
# if r<=0 and s<=0:
#     print("Invalid Inputs")
# elif r<=0:
#     print("Invalid Row Input")
# elif s<=0:
#     print("Invalid Starting Value")
# else:
#     s=1
#     sum=0
#     for i in range(1,r+1):
#         for j in range(1,i+1):
#             print(s,end="")
#             sum=sum+s
#             print(f'-{sum}')
#             s=s+1
#         print()

# n=int(input())
# if n>0:
#     for i in range(n,0,-1):
#         for j in range(i,0,-1):
#             print(j,end="")
#         print()
# r=int(input())
# s=int(input())
# if r>0 and s>0:
#     for i in range(1,r+1):
#         for j in range(1,r-i+2):
#             print(s,end=" ")
#             s=s-1
#         print()
# n=int(input())
# if n>0:
#     a=100
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(a,end=" ")
#             a=a+100
#         print()
# r=int(input())
# s=int(input())
# if r<=0 and s%2==0:
#     print("Invalid Inputs")
# elif r<=0:
#     print("Invalid Row Value")
# elif s%2==0:
#     print("Invalid Starting Value")
# else:
#     for i in range(1,r+1):
#         sum=0
#         for j in range(1,i+1):
#             print(s,end=" ")
#             sum=sum+s
#             s=s+1
#         if sum%2==1:
#             print(f'-{sum}',end="")
#         elif s%2==0:
#             print(f'-{sum}',end="")
#         print()
# r=int(input())
# s=int(input())
# if r<=0 and s<0:
#     print("Invalid Inputs")
# elif r<=0:
#     print("Invalid Starting Value")
# elif s<0:
#     print("Invalid Starting Value")
# else:
#     for i in range(1,r+1):
#         k=s
#         for j in range(1,i+1):
#             print(s,end="")
#         s=s+1
#         print()
# n=abs(int(input()))
# a=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(a,end="")
#         if a==1:
#             a=0
#         else:
#             a=1
#     print()
# n=int(input())
# for i in range(1,n+1):
#     a,b=1,2
#     for j in range(1,i+1):
#         print(a,end=" ")
#         c=a+b
#         a=b
#         b=c
#     print()
# n=int(input())
# if n>0:
#     for i in range(1,n+1):
#         print(" "*(i-1),end="")
#         for j in range(i,n+1):
#             print(j,end="")
# #         print()
# n=int(input())
# if n>0:
#     for i in range(1,n+1):
#         fc=0
#         a=2
#         for j in range(1,i+1):
#             if a%2==0:
#                 fc=fc+1
#         if fc==2:
#             print(a,end="")
#         print()
# n=int(input())
# for i in range(1,n+1):
#     print("  "*(n-i),end="")
#     a=71
# a=int(input())
# if a>0:
#     for i in range(1,a+1):
#         k=i
#         for j in range(1,i+1):
#             print(k,end=" ")
#             k=k+(a-j)
#         print()
# else:
#     print("Invalid Input")
#
#     for j in range(1,i+1):
#         print(chr(a),end=" ")
#         a=a-1
#     print()
# n=int(input())
# if n<=4:
#     print("GIven Value is Not more than 4")
# else:
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(i*j,end="")
#         print()




# n=int(input())
# if n>0:
#     a=1
#     for i in range(1,n+1):
#         for j in range(1,n-i+1):
#             print("  ",end=" ")
#         for j in range(1,i+1):
#             print(f'{a:02d}',end=" ")
#             a=a+1
#         print()
# else:
#     print("Invalid Input")























# a=int(input())
# if a>0:
#     for i in range(1,a+1):
#         k=i
#         for j in range(1,i+1):
#             print(k,end=" ")
#             k=k+(a-j)
#         print()
# else:
#     print("Invalid Input")

# n=int(input())
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     m=1
#     for j in range(1,i+1):
#         print(m,end=" ")
#         m=m*(i-j)//j
#     print()
#     m=m+1
# n=int(input())
# for i in range(1,n+1):
#     print(" "*(i-1),end="")
#     for j in range(1,n-i+2):
#         print("*",end=" ")
# #     print()
# n=int(input())
# for i in range(1,n+1):
#     print(" "*(i-1),end="")
#     for j in range(i,n+1):
#         print(j,end="")
#     for j in range(n-1,i-1,-1):
#         print(j,end="")
#     print()
# list=["hari","mani","ravi","raju"]
# print(list[-1])
# student={
#     "name":"hari",
#     "age":21,
#     "sec":'A'
# }
# for key in student:
#     print(key)
# student["age"]=25
# print(student["age"])
# print(student.keys())
# print(student.pop("sec"))
# # print(student.items())
# l=[1,2,3]
# l.append(3)
# l.extend([7,8])
# print(l)
# l=[1,2,3]
# m=l
# m.append(30)
# print(m)
# print(l)
# import copy
# original=[1,2,[3,4]]
# deep=copy.deepcopy(original)
# deep[2][1]=99
# print(deep)
# print(original)
#
#
# original=[1,2,[3,4]]
# shallow=copy.copy(original)
# shallow[2][1]=99
# print(shallow)
# print(original)

# l=[1,2,3,4,5,6,7,8,9]
# print(l[::-1])
# a=10
# print(isinstance(a,int))
# a="hello"
# b=10
# print(isinstance("hello",int))
# print(a+b)

# def greet(name):
#     print("hello",name)
# greet("hari")
# greet("mani")
# def power(base,exponent):
#     return base**exponent
# print(power(3,3))
# def full_name(first,mid,last):
#     return first+mid+last
# # print("hari","babu","allena")
# def describe (color,size,shape):
#     print(f"A {color} {size} {shape}")
# # describe("red","large","circle")
# def describe(shape,color,size):
#     print(f'A {color} {size} {shape}')
# describe(size="large",color="red",shape="rectangle")
# def greet(name,message="hello"):
#     print(f'{message},{name}')
# greet("hari","namaste sir")
# def add(*args):
#     total=0
#     for num in args:
#         total=total+num
#     return total
# print(add(12,34,56,78))
# def data(**kwargs):
#     print(kwargs)
# data(name="hari",age=21,sec="A",school="aruna")
# def multiply(*num):
#     total=0
#     for i in num:
#         total=i*i
#     return total
# print(multiply(1,2,3,4,5,6,7,8))
# def display_tags(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key}:{value}')
# display_tags(name="hari",age=21,city="hyd")
# def describe_person(name,*hobbies):
#     print(f'{name}:{hobbies}')
# describe_person("hari","playing","reading","watching")
# def create_html_tag(tag,**attributes):
#     print(f'<{tag}',end="")
#     for key,value in attributes.items():
#         print(f'{key}={value}')
# # create_html_tag("a",href='ir9u3r932',target="hsrevfye")
# def greet(name):
#     return f'hello,{name}'
# say_hello=greet
# print(say_hello("hari"))
# def apply(func,value):
#     return func(value)
# def double(x):
#     return x*x
# def square(x):
#     return x*x
# print(apply(double,3))
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# operations={
#     '+':add,
#     '-':sub,
#     '*':mul
# }
# op=input("enter the opearator")
# print(operations[op](5,6))
# def outer(name):
#     print("hello",name)
#
#     def inner(name):
#         print("welcome",name)
#     inner("mani")
# # outer("hari")
# def outer():
#     a=int(input())
#     b=int(input())
#     def inner():
#         print(a+b)
#     inner()
# outer()
# def outer(x):
#     if x>0:
#         pass
#     def inner():
#         print(x*x)
#     inner()
# # outer(34)
# def outer():
#     def inner(*n):
#         if n%2==0:
#             print(n)
#         else:
#             print("odd")
#     inner(int(1,2,3,5,7))
# outer()
# def process(numbers):
#     def is_even(n):
#         return n % 2 == 0
#     return [n for n in numbers if is_even(n)]
# print(process([1, 2, 3, 4, 5, 6])) # [2, 4, 6]
# def outer(numbers):
#     def inner():
#         result=[]
#         for n in numbers:
#             if n%2==0:
#                 result.append(n)
#     return inner()
# print(outer[1,2,3,4,6])
# def outer(numbers):
#
#     def inner():
#         result = []
#
#         for n in numbers:
#             if n % 2 == 0:
#                 result.append(n)
#
#         return result
#
#     return inner()
#
# # print(outer([1, 2, 3, 4, 6]))
# def outer():
#
#     x = 10
#
#     def inner():
#         print(x)
#
#     return inner
#
# f = outer()
#
# f()
# def hello():
#     return print
#
# x = hello()
#
# x("Hari")
# def make_multiplier(factor):
#
#     def multiplier(x):
#         return x * factor
#
#     return multiplier
#
# double = make_multiplier(2)
#
# # print(double(5))
# add=lambda a,b:a+b
# print(add(2,3))
# numbers=[1,2,4,3,6,5]
# numbers.sort(key=lambda x:x)
# print(numbers)
# students=[('alice',5),('ravi',3),('hari',4)]
# students.sort(key=lambda x:x[0])
# print(students)
# numbers=[1,2,3,4,5,6]
# even=(key=lambda x:x%2==0)
# print(even)
# def even(numbers):
#     result=[]
#     for n in numbers:
#         if n%2==0:
#             return result.append(n)
#     return result
# print(even([1,2,3,4,5,6,7,8]))
# def even(*n):
#     result=[]
#     for i in n:
#         if i%2==0:
#              result.append(i)
#     return result
# print(even(1,2,3,4,5,6,7,8))
# cube=lambda x:x**3
# print(cube(2))
# large=lambda x,y:x if x>y else y
# print(large(4,6))
# even=lambda x:x if x%2==0 else "odd"
# print(even(1))
# data=[(1,'banana'),(2,'apple'),(3,'cherry')]
# data.sort(key=lambda x:x[1])
# print(data)
# lis=[1,2,3,4,5,6]
# print(list(map(lambda x:x*2,lis)))
# numbers=[1,2,3,4,5]
# result=[]
# for i in numbers:
#     result.append(i*2)
# print(result)
# data=["hari","mani","ravi"]
# print(list(map(lambda x:x.upper(),data)))
#filter
# numbers=[1,2,3,4,5,6,7,8]
# result=list(filter(lambda x:x%2==0,numbers))
# print(result)
# data=["hari","mani","anitha"]
# result=list(filter(lambda x:x.startswith("a"),data))
# print(result)
# from functools import  reduce
# numbers=[1,2,3,4,5,6]
# res=reduce(lambda x,y:x+y,numbers)
# print(res)
# numbers=[4,5,2,3,1]
# res=sorted(numbers,key=lambda x:x)
# print(res)
# from functools import reduce
# data=[1,9,4,-5,6,8,2,-3]
# result=reduce(lambda x,y:x+y,map(lambda x:x**3,filter(lambda x:x>0,data)))
# print(result)

# reduce(lambda x,y:x+y,data)
# list(map(lambda x:x**3,data))
# sorted(data,key=lambda x:x,reverse=False)
# filter(lambda x:x>0,data)
#
# from functools import reduce
# data=[1,2,9,7,-4,5,3,-1,-5]
# result=list(filter(lambda x:x>0,map(lambda x:x**3,sorted(data,key=lambda x:x,reverse=True,reduce(lambda x,y:x+y,data))
# print(result)
# a=float(input())
# weight=int(a*1000)
# print(f'{weight} Grams')
# n=int(input())
# n1=int(input())
# if n>n1:
#     print("Invalid Range")
# else:
#     for i in range(n,n1+1):
#         if i%2==0:
#             print(i,end="")
# n=int(input())
# n1=int(input())
# sum=0
# if n<n1:
#     for i in range(n,n1+1):
#         sum=sum+i
#     print(sum)
# else:
#     print("Invalid Range")
# n=int(input())
# if 10<n<100:
#     for i in range(n):
#         print("cv corp")
# a=int(input())
# b=int(input())
# c=int(input())
# if a>b and a>c:
#     print(a)
# elif b>c:
#     print(b)
# else:
#     print(c)
# a=498
# if a<100 or a>1000:
#     print("wrong number")
# else:
#     if a%2==0:
#         b=a%3
#         print(b)
#     else:
#         b=a%2
# #         print(b)
# n=int(input())
# n1=int(input())
# for i in range(n,n1+1):
#     if i%11==0:
#         print(i)
# n=int(input())
# n1=int(input())
# c=input()
# if c=='+':
#     print(n+n1)
# elif c=='-':
#     print(n-n1)
# n=int(input())
# n1=int(input())
# sum=0
# c=0
# for i in range(n+1,n1):
#     if i%2==0:
#         c=c+1
#         if c>1:
#             print("+",end="")
#         print(f'{i}',end="")
#         sum=sum+i
# print(f'={sum}')
# n=int(input())
# n1=int(input())
# ac=0
# for i in range(n,n1+1):
#     if i%2==0:
#         ac=ac+1
#         if ac%2==1:
#             print(i)
# n=int(input())
# n1=int(input())
# sum=0
# for i in range(n,n1+1):
#     z=i*i
#     sum=sum+z
# # print(sum)
# n=int(input())
# n1=int(input())
# c=0
# for i in range(n,n1-1,-1):
#     c=c+1
#     if c>1:
#         print(end=",")
#     print(f'{i}@{i-1}',end="")
# n=int(input())
# c=0
# for i in range(1,n+1):
#     c=c+1
#     if c>1:
#         print(end=",")
#     print("A,B",end="")
# n=int(input())
# c=0
# for i in range(1,n+1):
#     c=c+1
#     if c>1:
#
#             print(end=",")
#         print("even",end=",")
#     else:
#         print(i,end="")
# n=int(input())
# c=0
# for i in range(1,n+1,2):
#     c=c+1
#     if c>1:
#         print(end=",")
#     if i%5==0:
#         print("divisible by 5",end="")
#     else:
#         print(i,end="")
# n=int(input())
# c=0
# for i in range(1,n+1):
#     c=c+1
#     if c>1:
#         print(end=",")
#     if i%2==0:
#         print("10",end="")
#     elif i%2==1:
#         print("5",end="")
# a=float(input())
# b=float(input())
# c=0
# while(round(a,1)<=b):
#     c=c+1
#     if c>1:
#         print(end=",")
#     print(f'{a:.1f}^2',end="")
#     a=a+0.2
# print(".")
# n=int(input())
# n1=int(input())
# c=0
# for i in range(n,n1-1,-1):
#     c=c+1
#     if c>1:
#         print(end=",")
#     if i>=0:
#         print(f'{i*5}',end="")
#     else:
#         print(f'({i*5})',end="")
# n=int(input())
# if n>0:
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc=fc+1
#     if fc==2:
#         print("prime number")
#     else:
# #         print("Not a prime Number")
# n=int(input())
# n1=int(input())
# ac=0
# c=0
# if n>0 and n1>0:
#     for i in range(n,n1+1):
#         fc=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 fc=fc+1
#         if fc==2:
#             ac=ac+1
#             if ac%2==1:
#                 c=c+1
#                 if c>1:
#                     print(end=",")
#                 print(i,end="")

# n=int(input())
# n1=int(input())
# sum=0
# c=0
# if n>0 and n1>0:
#     for i in range(n,n1+1):
#         fc=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 fc=fc+1
#         if fc==2:
#             c=c+1
#             if c>1:
#                 print(end=",")
#             print(i,end="")
# n=int(input())
# p=2
# count=0
# while True:
#     b=True
#     for i in range(2,int(p**0.5)+1):
#         if p%i==0:
#             b=False
#             break
#         if b==True:
#             print(p,end="")
#             count=count+1
#             if count==1:
#                 break
#             if count>1:
#                 print(end=",")
#             print(p,end="")
#         p+=1
# n=int(input())
# if n>0:
#     c=0
#     rev=0
#     while n>0:
#         r=n%10
#         rev=rev*10+r
#         c=c+1
#         if c>1:
#             print("+",end="")
#         print(r,end="")
#         n=n//10
# n=int(input())
# t=n
# rev=0
#
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if rev==t:
#     print("palindrome")
# else:
#     print("not a palindrome")
# n=int(input())
# n1=int(input())
# sum=0
# c=0
# ac=0
# for i in range(n,n1+1):
#     t=i
#     rev=0
#     while i>0:
#         r=i%10
#         rev=rev*10+r
#         i=i//10
#     if rev==t:
#         ac=ac+1
#         if ac%2==1:
#             c=c+1
#             sum=sum+rev
# print(sum/c)
# n=int(input())
# n1=int(input())
# dc=0
# for i in range(n,n1+1):
#     t=i
#     dc=arm=0
#     while t>0:
#         r=t%10
#         dc=dc+1
#         t=t//10
#     t=i
#     while t>0:
#         r=t%10
#         arm=arm+(r**dc)
#         t=t//10
#     if arm==i:
#         c=c+1
#         if c==1:
#             print("armstrong numbers in the given range is:")
#         total=total+i
#         if c>1:
#             print(end="+")
#         print(i,end="")
#     if c


# dc=0
# t=n
# while t>0:
#     r=t%10
#     dc=dc+1
#     t=t//10
# arm=0
# t=n
# while t>0:
#     r=t%10
#     arm=arm+(r**dc)
#     t=t//10
# if arm==n:
#     print(n)
#
# n=abs(int(input()))
# if n==0:
#     print("Invalid Input")
# else:
#
#
#     n=abs(n)
#     total=0
#     a,b=0,1
#
#     for i in range(1,n+1):
#         total=total+a
#         c=a+b
#         a=b
#         b=c
# #     print(total)
# n=int(input())
# if n>0:
#     a,b=0,1
#     for i in range(1,n*2+1):
#         total=total+a
#         c=a+b
#         a=b
#         b=c
#     print(total)
#
# n=int(input())
# n1=int(input())
# if n>=0 and n1>=0
#         a,b=0,1
#
#         print(a,end="")
#         c=a+b
#         a=b
#         b=c
# n1=int(input())
# n2=int(input())
# if n1>=0 and n2>=0:
#     if n1>n2:
#         n1,n2=n2,n1
#     a,b=0,1
#     count=0
#     total=0
#     while a<=n2:
#         if a>=n1:
#             count=count+1
#             total=total+a
#         c=a+b
#         a=b
#         b=c
#     print(total/count)
#     if c==0:
#         print("No Fibonacci Series")
# else:
# #     print("Invalid Inputs")
# n=int(input())
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
# n1=int(input())
# if n1>0:
#     for i in  range(1,n1+1):
#         for j in range(1,n1+1):
#             if i==j:
#                 print(j,end="")
#             else:
#                 print("0",end="")
# #         print()
# n=int(input())
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if i>=j:
#             print(i,end="")
#         print(j,end="")
# #     print()
# n=int(input())
# if n>0:
#     for i in range(1,n+1):
#         print(" "*(i-1),end="")
#         for j in range(1,n-i+2):
#             print("*",end="")
#         print()
# n=int(input())
# a=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(a,end="")
#         a=a+2
#     print()
#     a=a-1

# n=int(input())
# if n>0:
#     for i in range(1,n+1):
#         for j in range(n,i-1,-1):
#             print(j,end="")
#         print()
# n=int(input())
# if n>0:
#     for i in range(1,n+1):
#         # if i%2==1:
#         #     for j in range(1,n-i+2):
#         #         print(j,end="")
#         #     print()
#         # else:
#         for j in range(n-i+1,0,-1):
#             print(j,end="")
#         print()
# n=int(input())
# if n>0:
#     for i in range(1,n+1):
#         print(" "*(i-1),end="")
#         for j in range(i,n+1):
#             print(j,end="")
#         print()
# def discount(x):
#     def inner(n):
#         return x*n
#     return inner
# a=discount(2)
# # print(a(4))
# def create_password(password):
#     def check_password(input_password):
#         if input_password==password:
#             print("Access granted")
#         else:
#             print("access denied")
#     return check_password
# auth=create_password("hari123")
# auth("hari1234")
# def movie(movie):
#     def person(name):
#         print(f'{name}:{movie}')
#     return person
# a=movie("devara")
# a("haribabu allena")
# def discount(percent):
#     def product(price):
#         final_rate=price/percent
#         print(final_rate)
#     return product
# a=discount(10)
# a(2000)
# class Student:
#     batch=16
#     def __init__(self,name ,age,section):
#         self.name=name
#         self.age=age
#         self.section=section
#     def valid(self):
#         if self.age>18:
#             return True
#     def eligible(self):
#         if self.valid():
#             print("eligible")
#     def display(self):
#         if self.valid():
#             return f'name:{self.name},age:{self.age}'
#
# s1=Student("hari",19,"spark")
# print(s1.eligible())
# class Employee:
#     company="Techi";bonus=0.2
#     def __init__(self,name,exp,sal):
#         self.name=name
#         self.exp=exp
#         self.sal=sal
#     def final_salary(self):
#         k=self.sal+(self.sal*self.bonus)
#         print(f'final salary:{k}')
#     def change_exp(self,n_v):
#         self.exp=n_v
#         self.display()
#     def display(self):
#         print(f'name:{self.name},exp:{self.exp},sal:{self.sal}')
#
# s1=Employee("hari",3,20000)
# print(s1.exp)
# s1.change_exp(5)
# class Car:
#     wheels=4
#     def __init__(self,m):
#         self.mileage=m
#     def display_specs(self):
#         print(f'mileage:{self.mileage}')
#         print(f'wheels:{self.wheels}')
#     @classmethod
#     def change_specs(cls,n_w):
#         cls.wheels=n_w
# c1=Car(60)
# Car.change_specs(8)
# c1.display_specs()
# class BankAccount:
#     Bank_name="SBI"
#     def __init__(self,holder):
#         self.holder=holder
#         self.balance=0
#     def deposit(self,amount):
#         if self.validate_amount(amount):
#             self.balance+=amount
#     @classmethod
#     def change_bank_name(cls,n_b):
#         cls.Bank_name=n_b
#     @staticmethod
#     def validate_amount(cash):
#         if cash>0:
#             return True
# b1=BankAccount("hari")
# b1.deposit(1000)
# print(b1.balance)
# b1.change_bank_name("union bank")
# print(b1.Bank_name)
# b1.deposit(1000)
# print(b1.balance)

# class Book:
#     total_books=0
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#         Book.total_books+=1
#     @classmethod
#     def from_string(cls,book_str):
#         title,author=book_str.split('-')
#         return cls(title,author)
class Loan:
    c_i=2
    def __init__(self,name,p):
        self.name=name
        self.p=p
    @staticmethod
    def loan_eligibility(sal):
        if sal>10000:
            return True
    @classmethod
    def update(cls,n_i):
        cls.c_i=n_i
    def total(self):
        k=self.p+(self.p*self.c_i)
        return k
l1=Loan("hari",20000)












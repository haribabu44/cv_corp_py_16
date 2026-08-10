#2.insert an element at a specified index in alist
l=[10,20,30,40,50,60,70,80]
print(l)
l.insert(4,30)
print(l)
#3.merge two lists
l1=[12,13,14,15,16]
l.extend(l1)
print(l)
#4.remove a specific element from the list
l.remove(30)
print(l)
#5.remove a element from a list based on index
n=l.pop(1)
print(n)
print(l)
#6.find index of a given element in a list
print(l.index(12))
#7.find count the number of occurance of an element 
l.insert(1,20)
l.insert(4,20)
print(l)
#counting 
print(l.count(20))
#sum of first and last elements
print((l[0]+l[13]))
#sum of list element upto given index
sum=0
for i in range(len(l)):
    sum=sum+l[i]
print(sum) 
#calculate the average of odd numbers in a list
total=0
count=0  
for i in range(len(l)):
    if l[i]%2==1:
        total=total+l[i]
        count=count+1
print(total/count)
#print all the prime numbers in a list
l1=[1,23,33,45,6,3,6,2,11,23]
for n in l1:
    fc=0
    for j in range(1,n+1):
        if n%j==0:
            fc=fc+1
    if fc==2:
        print(n)
#reversing a list
l1.reverse()
print(l1)








































l1=[1,2,3,4,5,6,'hi',12.5]#list can store mutiple values and multiple datatypes and stores duplicates also
l=[10,20,30,40,50,60]
print(l)
print(*l)
print(l[4])
print(l[2])
print(len(l))
#based on element
for i in l:
    print(i)
# based on index
for i in range(len(l)):
    print(l[i])
#list Attributes
#1.append()
l.append(20)
print(l)
print(*l)
#extend
l2=[30,40,60]
l.extend(l2)
print(l)
print(*l)
#by using string
# l.extend("bye")
# print(*l)
#insert()
l.insert(5,70)
l.insert(6,80)
print(*l)
#membership operator #in - not in
l3=[1,34,556,78,9,38]
print(34 in l3)
print(45 not in l3)
# remove() -->it is used to remove the first occurence of the specified element
l4=[10,20,30,40,50,60,50,70]
l4.remove(50)
print(l4)
#remove through loop
l5=[10,20,30,50,56,40]
n=30
if n in l5:
    l5.remove(n)
    print(*l5)
else:
    print("element not found")
#pop()-->it removes at returns the specified index of element
l6=[10,20,30,40,50,70,60]
m=l6.pop(0)
print(m)
print(*l6)
#without mention the index
m=l6.pop()
print(m)
print(*l6)
#index()-->it returns the index of the first occurance of the specified value ,with in range.
#syntax -->index(value,start,end)
l7=[10,20,10,40,50,20,70,50,10]
n=l7.index(10,1,5)
print(n)
print(*l7)
#count()
l7=[10,20,10,40,50,20,70,50,10]
print(l7.count(10))
#sort()
l7=[10,20,10,40,50,20,70,50,10]
l7.sort(reverse=True)
print(l7)
#reverse
l8=[10,20,30,40,50,60,70]
l8.reverse()
print(l8)
#copy()
l7=[10,20,10,40,50,20,70,50,10]
l9=l7.copy()
print(l9)
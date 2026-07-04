from functools import reduce
l=[5,10,15,20,25,30]
z=reduce(lambda x,y:x+y,l)
print(z)
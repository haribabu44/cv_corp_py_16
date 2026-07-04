from functools import reduce
n=[1,2,3,4,5]
m=reduce(lambda x,y:x if x>y else y,n)
print(m)
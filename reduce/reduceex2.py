from functools import reduce
x=['p','y','t','h','o','n']
m=reduce(lambda a,b:a+b,x)
print(m)
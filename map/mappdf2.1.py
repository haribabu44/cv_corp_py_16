nums=[12,15,7,18,20,21,25]
x=list(filter(lambda y: y%3==0 and y%5==0,nums))
print(x)
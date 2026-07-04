l=[12,15,7,18,20,21,25]
m=list(filter(lambda x:(x%3==0) ^ (x%5==0),l))
print(m)
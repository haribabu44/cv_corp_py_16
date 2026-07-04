# from functools import reduce
# nums=[1,2,3,4]
# a=nums.append(10)
# m=reduce(lambda x,y:x+y,nums)
# print(m)
# nums = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda x: x.append(10), nums))
# print("Result:", result)
# print("Nums:", nums)
n=int(input())
n1=int(input())
c=0
if n>n1:
    print("Invalid range")
else:
    for i in range(n,n1+1):
        c=c+i
    print(c)
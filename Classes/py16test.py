
l=[1,2,3,[4,5]]
import copy
m=copy.deepcopy(l)
m[3].append(30)
print(m)

# l=[1,2,3,[4,5]]
# # m=l.copy()
# import copy
# m=copy.copy(l)
# m[3].append(25)
# print(m)



from os import name


class Students:
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    def is_passed(self):
        if self.marks>40:
            return "True"
        else:
            return "false"

s1=Students("hari",40)
print(s1.is_passed())
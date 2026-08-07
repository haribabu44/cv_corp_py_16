class Employee:
    company_name="cvcorp"
    def __init__(self,n):
        self.name=n
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name

        # print(f'{k}')
e1=Employee("Hari")
# print(e1.name)
Employee.change_company("gbcorp")
# print(e1.company_name)
e2=Employee("mani")
print(e1.name,e1.company_name)
print(e2.name,e2.company_name)





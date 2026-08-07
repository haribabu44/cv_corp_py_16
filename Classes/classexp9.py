class BankAccount:
    bank_name="hbbank"
    def __init__(self,h,b):
        self.holder=h
        self.balance=b
    def deposit(self,a):
        self.amount=a
        d=self.balance+self.amount
        return d
b1=BankAccount("hari",1000)
# print(b1.holder,b1.balance)
# b1=BankAccount("hari",2000)
# print(b1.holder,b1.balance)
# b1.deposit(200)
print(b1.deposit(5000))
print(b1.balance)

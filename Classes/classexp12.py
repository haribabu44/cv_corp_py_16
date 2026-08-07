class Product:
    base_tax_rate=4
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
    def final_price(self):
        if self.valid(self.base_price):
            k=self.base_price+(self.base_price*Product.base_tax_rate)/100
            return k
    @classmethod
    def update(cls,nbt):
        cls.base_tax_rate=nbt
    @staticmethod
    def valid(price):
        if price>500:
            return True
        else:
            return False
p1=Product("mobile",1000)
print(Product.valid(200))
Product.update(5)
# print(Product.base_tax_rate)
print(Product.final_price(p1))


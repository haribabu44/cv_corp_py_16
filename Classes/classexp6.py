class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(celsius):
        f=(celsius*1.8)+32
        print(f'fahrenheit is {f}')
    def show_conversion(self):
        print("celsius:",self.celsius)
        t1.to_fahrenheit(self.celsius)
t1=Temperature(40)
t1.show_conversion()
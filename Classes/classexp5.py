class Mathops:
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
        else:
            return False
print(Mathops.is_even(15))
n1=Mathops()
print(n1.is_even(8))
# Mathops.is_even()
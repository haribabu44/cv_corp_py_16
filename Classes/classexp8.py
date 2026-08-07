class Course:
    total_students=20
    def __init__(self,n):
        self.name=n
        Course.total_students=Course.total_students+1
    @staticmethod
    def is_eligible(age):
        if age>18:
            return True
        else:
            return False
    @classmethod
    def show_total(cls):
        print(f" total students:{cls.total_students}")
s1=Course("hari")
s1.is_eligible(19)
s2=Course("mani")
Course.show_total()



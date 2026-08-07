class Book:
    total_books=0
    def __init__(self,n,a):
        self.name=n
        self.author=a
        Book.total_books+=1
    @classmethod
    def creation(cls,ta):
        t,a = ta.split("-")
        if cls.valid(t):
            return cls(t,a)
        else:
            print("Title is too short")
    @classmethod
    def update(cls,new_total):
        cls.total_books=new_total
        print(f"total_books:{cls.total_books}")

    @staticmethod
    def valid(t):
        return len(t) >= 5
cls=Book
b1=Book.creation("theauthorspov-author")
if b1:
    print(b1.name)
    print(b1.author)
else:
    print("Object Not created")




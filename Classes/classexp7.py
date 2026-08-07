class Book:
    total_books=5
    def __init__(self,t,a):
        self.title=t
        self.author=a
        Book.total_books=Book.total_books+1
    @staticmethod
    def is_valid(t):
        return len(t)>3
    @classmethod
    def from_string(cls,book_str):
        t,a=book_str.split("-")
        if cls.is_valid(t):
            return Book(t,a)
        else:
            print("Invalid Title")
b1=Book.from_string("t-h")
# b1.is_valid("the shaswkash demptioj")
# print(b1.is_valid("haruabhcvce"))
# print(b1.from_string("thehw-hdgcdv",))
if b1:
    print(b1.title,b1.author,sep="\n")
else:
    print("nothing in the object")

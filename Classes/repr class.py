class Facebook:
    usernames={}
    def __init__(self,name,age,username,gender):
        self.name=name
        self.age=age
        self.username=username
        self.gender=gender
        self.friends_list=[]
        self.logged=False
        Facebook.usernames[username]=self
    @classmethod
    def signup(cls):
        name=input("enter your name")
        while True:
            username=input("enter your username")
            if username in cls.usernames:
                print("username already exits ")
                continue
            break
        age=int(input("enter your age"))
        gender=input("enter your gender")
        return cls(name, age, username, gender)
    def login(self):
        if self.logged:
            print("already login ")
        else:
            username=input("enter your username")
            password=input("enter your password")
            if username==self.username and password==self.password:
                self.logged=True
                print("login sucessfully")
            else:
                print("Invalid details")
    def logout(self):
        if self.logged:
            self.logged=False
            print("logout sucessfully")
    def validate_age(self):






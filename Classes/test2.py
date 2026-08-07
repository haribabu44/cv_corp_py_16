# from functools import reduce
# sales=[
#     {"item":"pen","price":10,"qty":5},
#     {"item":"bag","price":500,"qty":0},
#     {"item":"book","price":120,"qty":10},
# ]
# grand_total=reduce(lambda x,y:x+y,map(lambda x:x["price"]*x["qty"],filter(lambda x:x["qty"]>0,sales)))
# print(grand_total)
# a=list(map(lambda x:x["price"]*x["qty"],sales))
# print(a)=
# a=list(filter(lambda x:x["qty"]>0,sales))
# print(a)
# a=list(reduce(lambda x,y:x+y,sales))
def registration():
    username=input("enter username")
    password=input("enter password")
    print(f"{username} registered sucessfully!")
def login():
    username=input("enter username")
    password=input("enter password")
    print(f"welcome {username}!")
def profile():
    print("Name: Hari")
    print("Role:user")
    print("status :active")
operations={
    1:registration,
    2:login,
    3:profile,
}
while True:
    print("1.Registration")
    print("2.login")
    print("3.profile")
    print("4.exit")

    try:
        choice=int(input("enter your choice"))

        if choice ==4:
            print("thank you")
            break
        elif choice in operations:
            operations[choice]()
    except ValueError:
        print("Please enter only numbers.")




    # def login():
    #     profile():




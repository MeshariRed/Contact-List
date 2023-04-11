"""
Hi There,

This Program Just For Make A Small Idea How Make Contact List In Your Phone, 

I hope it is understandable enough,

All The Best

"""

# This Is A Dictionary Have A List Of Contact By Default
Contact = {
    "Amal": 1111111111,
    "Mohammed": 2222222222,
    "Khadijah": 3333333333,
    "Abdullah": 4444444444,
    "Rawan": 5555555555,
    "Faisal": 6666666666,
    "Layla": 7777777777,
    "Mark": 8888888888,
    "Jon": 9999999999
}

# While => Make System Running Without Stop, If Have A Error Will Be Stop
while True:
    print("""
1 - Show Phone Number By Name
2 - Show Name By Phone Numbers 
3 - Add A New Person To Contact List
4 - Exit
    """)
    num = input("\nEnter the numbers: ")

    if num == '1':
        a = input("\nName : ")
        print("Phone: ", Contact[a], "\n")

    elif num == '2':
        b = input("\nPhone : ")
        for x, y in Contact.items():
            if y == int(b):
                print("Name: ", x, "\n")

    elif num == '3':
        a2 = input("Name : ")
        b2 = input("Phone: ")

        Contact.update({f"{a2}": int(b2)})
        print("--------------------\nAdd sussccfly")

    elif num == '4':
        exit()

    else:
        print("Sorry This Illegal")
        exit()

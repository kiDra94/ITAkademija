menuShowProduct = 1
menuBuyProduct  = 2
menuExitProgram = 3
productName     = "iPhone"
productPrice    = 180
userBalance     = int(input("Enter balance: "))
userCommand     = int(input("Enter command: "))
if(userCommand==1):
    print("Name: ", productName)
    print("Price: ", productPrice)
if(userCommand==2):
    if(userBalance>=productPrice):
        print("You bought the product")
    if(userBalance<productPrice):
        print("You don't have enough balance")
if(userCommand==3):
    print("Good bye")

    







    
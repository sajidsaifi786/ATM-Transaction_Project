#ATM Transaction Record Project
balance=10000 #Use String
transaction=[] #Use List to store transaction history
def deposite(amount):
    global balance
    balance+=amount
    transaction.append(f"Deposited :{amount}")
    print(f"{amount} Deposited Successfully !")
def withdraw(amount):
    global balance
    if(amount>balance):
        print("Insufficient Balance !")
    else:
        balance-=amount
        transaction.append(f"Withdraw :{amount}")
        print(f"{amount} Withdraw Successfully !")
def show_balance():
    print(f"Current Balance :{balance}")
def show_history():
    print("\n Transaction History")
    for t in transaction:
        print("-",t)

#Main Menu
while True:
    print("\n----ATM MENU----")
    print("1.Check Balance")
    print("2.Deposite Money")
    print("3.Withdraw Money")
    print("4.Transaction History")
    print("5.Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        show_balance()
    elif choice==2:
        atm=int(input("Enter amount to deposite :"))
        deposite(atm)
    elif choice==3:
        atm=int(input("Enter amount to withdraw :"))
        withdraw(atm)
    elif choice==4:
        show_history()
    elif choice==5:
        print()
        print("Thank You for using ATM !")
        break
    else:
        print("Invalid Choice ! Please Try again with valid choice !")
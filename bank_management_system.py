print("***Bank management system***")
names=[]
balances=[]
while True:
    print("1.Create account")
    print("2.View accounts")
    print("3.Search account")
    print("4.Deposit money")
    print("5.Withdraw money")
    print("6.Delete account")
    print("7.Exit")

    choice=input("Enter your choice:")
    if choice=="1":
        print("Create account:")
        name=input("Enter your name:")
        balance=int(input("Enter your initial bank balance:"))
        names.append(name)
        balances.append(balance)
    elif choice=="2":
        print("View accounts")
        for i in range(len(names)):
            print(names[i],"- $",balances[i])
    elif choice=="3":
        print("Search account:")
        name=input("Enter holder account name:")
        if name in names:
            index=names.index(name)
            print(name,"- $",balances[index])
        else:
            print("Account not found!")
    elif choice=="4":
        print("Deposit money:")
        name=input("Enter account holder name:")
        money=int(input("Enter deposit money:"))
        if name in names:
            index=names.index(name)
            balances[index]+=money
            print("Amount deposited successfully!")
        else:
            print("Account not found!")
    elif choice=="5":
        print("Withdraw money:")
        name=input("Enter account holder name:")
        if name in names:
            money=int(input("Enter your withdraw money:"))
            index=names.index(name)
            if money<=balances[index]:
                balances[index]-=money
                print("Withdraw successfully!")
            else:
                print("Required amount not found!")
        else:
            print("Account not found!")
    elif choice=="6":
        print("Delete account:")
        name=input("Enter account name:")
        if name in names:
            names.remove(name)
            index=names.index(name)
            balances.pop[index]
            print("Account deleted successfully!")
        else:
            print("Account not found!")
    elif choice=="7":
        print("Thank you!")
        break
    else:
        print("In-valid syntax")

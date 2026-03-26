# expense tracker

Expenseslist=[]
print("Welcome to Expense Tracker: ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. EXIT ")

    choice=int(input("Please Enter your choice:"))

# 1. Add Expense

    if(choice==1):
        date=input("Date of Expense? : ")
        category=input("Type of Expense? (books, travel,food, makeup ): ")
        description= input("Give more detail: ")
        Amount=float(input("Enter the Amount: "))

        expense= {
            "date":date,
            "category": category,
            "description": description,
            "Amount": Amount
        }

        Expenseslist.append(expense)
        print("\n DONE BRO. Expense is Added Succesfully")

# 2. View All Expenses

    elif(choice == 2):
        if (len(Expenseslist) == 0 ):
            print("=== No Expense Added ===")
        else:
            print(" === That's your total Expense === ")
            count = 1 
            for eachexpense in Expenseslist:
                print(f"expense number{count} -> {eachexpense["date"]}, {eachexpense["category"]}, {eachexpense["description"]},{eachexpense["Amount"]}")
                count = count+1

#3. VIEW TOTAL SPENDING
    elif(choice == 3):
        total = 0
        for eachexpense in Expenseslist:
            total = total + eachexpense["Amount"]

        print("\n Total Expense =", total)

# 4. EXIT

    elif(choice==4):
        print("THANKS FOR USING OUR SYSTEM")
        break
    else:
        print("INVALID CHOICE. TRY AGAIN :( ")

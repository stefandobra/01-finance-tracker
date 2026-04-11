def display_menu():
    print("\n --- Budget Tracker ---")
    print("1. Add regular income")
    print("2. Add one-off income")
    print("3. Add regular spending")
    print("4. Add one-off spending")
    print("5. View summary")
    print("6. Quit")

def monthly(frequency, amount):
    if frequency == "1":
        return amount * 30
    elif frequency == "2":
        return amount * 52 / 12
    else:
        return amount

regular_incomes = []
oneoff_incomes = []

regular_spendings = []
oneoff_spendings = []

while True:
    display_menu()

    option = input("Please select one option: ")

    if option == "1":
        income_category = input("What category is this regular income? ")
        income_description = input("Describe income: ")
        income_amount = float(input("Please enter income amount: "))
        while True:
            frequency = input("How often do you receive this income?\n1. Daily\n2. Weekly\n3. Monthly\nPlease enter frequency: ")
            if frequency not in ("1","2","3"):
                print("Invalid Selection!")
            else:
                break

        monthly_income = monthly(frequency, income_amount)

        regular_income = {
            "category" : income_category, 
            "income_description" : income_description, 
            "monthly_income" : monthly_income
            }
        regular_incomes.append(regular_income)

    elif option == "2":
        income_category = input("What category is this one off income? ")
        income_description = input("Describe income: ")
        income_amount = float(input("Please enter income amount: "))

        oneoff_income = {
            "category" : income_category, 
            "income_description" : income_description, 
            "income_amount" : income_amount, 
            }
        oneoff_incomes.append(oneoff_income)

    elif option == "3":
        spending_category = input("What category is this regular spending? ")
        spending_description = input("Describe spending: ")
        spending_amount = float(input("Please enter spending amount: "))

        while True:
            frequency = input("How often do you pay this?\n1. Daily\n2. Weekly\n3. Monthly\nPlease enter frequency: ")
            if frequency not in ("1","2","3"):
                print("Invalid Selection!")
            else:
                break
        
        monthly_spending = monthly(frequency, spending_amount)

        regular_spending = {
            "category" : spending_category, 
            "spending_description" : spending_description, 
            "monthly_spending" : monthly_spending
        }        

        regular_spendings.append(regular_spending)

    elif option == "4":
        spending_category = input("What category is this one off spending? ")
        spending_description = input("Describe spending: ")
        spending_amount = float(input("Please enter spending amount: "))

        oneoff_spending = {
            "category" : spending_category, 
            "spending_description" : spending_description, 
            "spending_amount" : spending_amount
        }

        oneoff_spendings.append(oneoff_spending)

    elif option == "5":
        print("Regular incomes: ", len(regular_incomes))

        regular_income_total = 0

        for income in regular_incomes:
            regular_income_total += income["monthly_income"]

        print(f"Monthly regular income: {regular_income_total:,.2f}")

        oneoff_income_total = 0

        for income in oneoff_incomes:
            oneoff_income_total += income["income_amount"]

        print("Total oneoff income: ", oneoff_income_total)

        print("Total regular and oneoff income: ", regular_income_total + oneoff_income_total)

        print("Regular spendings: ", len(regular_spendings))

        regular_spending_total = 0
        oneoff_spending_total = 0

        for spending in regular_spendings:
            regular_spending_total += spending["monthly_spending"]

        print(f"Monthly regular spending: {regular_spending_total:,.2f}")

        for spending in oneoff_spendings:
            oneoff_spending_total += spending["spending_amount"]
        
        print("Total oneoff spending: ", oneoff_spending_total)
        print("Total regular and oneoff spending: ", regular_spending_total + oneoff_spending_total)

        print(f"Monthly money left after regular spending: {(regular_income_total-regular_spending_total):,.2f}")
        print(f"Monthly money left after total spending {(regular_income_total-(regular_spending_total + oneoff_spending_total)):,.2f}")


    elif option == "6":
        print("Quitting program....")
        break

    else:
        print("Invalid Selection!")

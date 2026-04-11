def display_menu():
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
oneoff_spending = []



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
        income_category = input("What category is this regular income? ")
        income_description = input("Describe income: ")
        income_amount = float(input("Please enter income amount: "))

        oneoff_income = {
            "category" : income_category, 
            "income_description" : income_description, 
            "income_amount" : income_amount, 
            }
        oneoff_incomes.append(oneoff_income)

    elif option == "5":
        print("Regular incomes: ", len(regular_incomes))

    
        regular_income_total = 0

        for income in regular_incomes:
            regular_income_total += income["monthly_income"]

        print("Monthly regular income: ", regular_income_total)

    elif option == "6":
        break

    else:
        print("Invalid Selection!")

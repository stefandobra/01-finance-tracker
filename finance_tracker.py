import json
import os
from anthropic import Anthropic
from dotenv import load_dotenv


load_dotenv()
client = Anthropic(
    api_key=os.getenv("FINANCE_TRACKER_API_KEY")
)

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
    
def save_data(regular_incomes, oneoff_incomes, regular_spendings, oneoff_spendings):
    data_to_output = {
        "regular_incomes" : regular_incomes,
        "oneoff_incomes" : oneoff_incomes,
        "regular_spendings" : regular_spendings,
        "oneoff_spendings" : oneoff_spendings,
    }
    with open("data.json", "w") as file:
        json.dump(data_to_output, file)

def load_data():
    try:
        with open("data.json", "r") as file:
            data_to_load = json.load(file)

        regular_incomes = data_to_load["regular_incomes"]
        oneoff_incomes = data_to_load["oneoff_incomes"]
        regular_spendings = data_to_load["regular_spendings"]
        oneoff_spendings = data_to_load["oneoff_spendings"]

        return regular_incomes, oneoff_incomes, regular_spendings, oneoff_spendings
    
    except FileNotFoundError:
        print("No saved data found, starting fresh")

        regular_incomes = []
        oneoff_incomes = []
        regular_spendings = []
        oneoff_spendings = []

        return regular_incomes, oneoff_incomes, regular_spendings, oneoff_spendings

def generate_AI_summary(regular_incomes, oneoff_incomes, regular_spendings, oneoff_spendings):
    message = client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"Please summarise this financial information. there are 2 types of income, regular which is expressed in monthly amounts and one off. same for spending. each of the 4 have both a category and a description of what the income or spending was for. The data is  named accordingly: regular_incomes {regular_incomes}, oneoff_incomes {oneoff_incomes}, regular_spendings {regular_spendings} and oneoff_spendings {oneoff_spendings}. Each of these types of income and spendings have items attached to them: regular_incomes has a number of regular_income items that each have category, income_description and monthly_income. oneoff_incomes has a number of oneoff_income items that each have category, income_description and income_amount. regular_spendings has a number of regular_spending items that each have category, spending_description and monthly_spending. oneoff_spendings has a number of oneoff_spending items that each have category, spending_description and spending_amount. I need you to act like a financial advisor and give me a summary that includes : total number of regular incomes and spendings and total monthly incomes and spendings, total one offs and total one off + regular income and spendings. also need a total monthly left after regular spending and total left after all spending"
            }

        ],
        model="claude-sonnet-4-6",
    )

    return message
    
regular_incomes, oneoff_incomes, regular_spendings, oneoff_spendings = load_data()

# regular_incomes = []
# oneoff_incomes = []
# regular_spendings = []
# oneoff_spendings = []

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

        print(f"Total oneoff income: {oneoff_income_total:,.2f}")

        print(f"Total regular and oneoff income: {(regular_income_total + oneoff_income_total):,.2f}")

        print(f"Regular spendings: ", len(regular_spendings))

        regular_spending_total = 0
        oneoff_spending_total = 0

        for spending in regular_spendings:
            regular_spending_total += spending["monthly_spending"]

        print(f"Monthly regular spending: {regular_spending_total:,.2f}")

        for spending in oneoff_spendings:
            oneoff_spending_total += spending["spending_amount"]
        
        print(f"Total oneoff spending: {oneoff_spending_total:,.2f}")
        print(f"Total regular and oneoff spending: {(regular_spending_total + oneoff_spending_total):,.2f}")

        print(f"Monthly money left after regular spending: {(regular_income_total-regular_spending_total):,.2f}")
        print(f"Monthly money left after total spending {(regular_income_total-(regular_spending_total + oneoff_spending_total)):,.2f}")

        try:
            AI_summary = generate_AI_summary(regular_incomes, oneoff_incomes, regular_spendings, oneoff_spendings).content[0].text
            print(AI_summary)
        except IndexError:
            print("AI returned empty response")
        except AttributeError:
            print("AI response didn't contain readable text")

    elif option == "6":
        save_data(regular_incomes, oneoff_incomes, regular_spendings, oneoff_spendings)
        print("Quitting program....")
        break

    else:
        print("Invalid Selection!")

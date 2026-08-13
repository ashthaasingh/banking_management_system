from src.account import Account
from src.storage import load_accounts, save_accounts

def create_account():
    accounts = load_accounts()

    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))
    phone = input("Enter Your Phone Number: ")
    account_type = input("Enter Account Type (Savings/Current): ")

    account_number = 1001 + len(accounts)

    account = Account(
        account_number,
        name,
        age,
        phone,
        account_type
    )

    accounts.append(account.to_dict())

    save_accounts(accounts)

    print("\nAccount Created Successfully!")
    print("Your Account Number is:", account_number)


def view_accounts():
    accounts = load_accounts()

    if not accounts:
        print("\n No accounts found!")
        return

    print("\n =============== All Accounnts ================") 

    for account in accounts:
        print("===================================")
        print("Account Number:", account["Account_Number"])
        print("Name:", account["Name"])
        print("Age:", account["Age"])
        print("Phone Number:", account["Phone"])
        print("Account Type:", account["Account_Type"])
        print("Balance:", account["Balance"])

        print("===================================")    


def search_account():
    accounts = load_accounts()

    if not accounts:
        print("\nNo accounts found!")
        return

    account_number = int(input("Enter Account Number to search: "))

    for account in accounts:
        if account["Account_Number"] == account_number:
            print("\n========== Account Found ==========")
            print("Account Number:", account["Account_Number"])
            print("Name:", account["Name"])
            print("Age:", account["Age"])
            print("Phone Number:", account["Phone"])
            print("Account Type:", account["Account_Type"])
            print("Balance:", account["Balance"])
            print("===================================")
            return

    print("\nAccount not found!")        


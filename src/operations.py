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


def deposit_money():
    accounts = load_accounts()

    if not accounts:
        print("\n No accounts found!")
        return

    account_number = int(input("Enter Account Number to deposit money:"))
    amount = float(input("Enter Amount to Deposit:"))

    if amount <= 0:
        print("\n Amount should be greater than zero")
        return

    for account in accounts:
        if account["Account_Number"] == account_number:
            account["Balance"] += amount
            transaction = {
                "Type" : "Deposit",
                "Amount" : amount
            }   

            account["Transactions"].append(transaction)

            save_accounts(accounts)

            print("\n Amount Deposited Successfully!")
            print("Deposited Amount:" , amount)
            print("New Balance:", account["Balance"])    
            return
    print("\n Account not found!")                    


def withdraw_money():
    accounts = load_accounts()

    if not accounts:
        print("\nNo accounts found!")
        return

    account_number = int(input("Enter Account Number: "))
    amount = float(input("Enter Amount to Withdraw: "))

    if amount <= 0:
        print("\nAmount must be greater than 0!")
        return

    for account in accounts:
        if account["Account_Number"] == account_number:

            if amount > account["Balance"]:
                print("\nInsufficient Balance!")
                print("Available Balance:", account["Balance"])
                return

            account["Balance"] -= amount

            transaction = {
                "Type": "Withdraw",
                "Amount": amount
            }

            account["Transactions"].append(transaction)

            save_accounts(accounts)

            print("\nWithdrawal Successful!")
            print("Withdrawn Amount:", amount)
            print("Remaining Balance:", account["Balance"])
            return

    print("\nAccount not found!")

def transfer_money():
    accounts = load_accounts()

    if not accounts:
        print("\nNo accounts found!")
        return

    from_account_number = int(input("Enter Your Account Number: "))
    to_account_number = int(input("Enter Recipient's Account Number: "))
    amount = float(input("Enter Amount to Transfer: "))

    if amount <= 0:
        print("\nAmount must be greater than 0!")
        return

    from_account = None
    to_account = None

    for account in accounts:
        if account["Account_Number"] == from_account_number:
            from_account = account
        elif account["Account_Number"] == to_account_number:
            to_account = account

    if not from_account:
        print("\nYour account not found!")
        return

    if not to_account:
        print("\nRecipient's account not found!")
        return

    if amount > from_account["Balance"]:
        print("\nInsufficient Balance!")
        print("Available Balance:", from_account["Balance"])
        return

    from_account["Balance"] -= amount
    to_account["Balance"] += amount

    transaction = {
        "Type": "Transfer",
        "Amount": amount,
        "To_Account": to_account_number
    }

    from_account["Transactions"].append(transaction)

    save_accounts(accounts)

    print("\nTransfer Successful!")
    print("Transferred Amount:", amount)
    print("Remaining Balance:", from_account["Balance"])
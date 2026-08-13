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

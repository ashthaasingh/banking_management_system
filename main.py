from src.menu import menu
from src.account import Account
from src.operations import (
    create_account,
    view_accounts,
    search_account,
    deposit_money,
    withdraw_money
)


while(True):
    menu()

    choice = int(input("Enter Your Choice: "))

    match choice:
        case 1: 
            create_account()
        case 2:
            view_accounts()
        case 3:
            search_account()
        case 4:
            deposit_money()
        case 5:  
            withdraw_money()
        case 6:
            transfer_money()
        case 7:
            transaction_history()  
        case 8:
            delete_account()
        case 9:
            print("Thank You! For using Banking Management System.")
            break  
        case _:  
            print("Invalid Choice! Please try again")                        
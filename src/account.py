class Account:
    def __init__(self, account_number, name, age, phone, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.age = age
        self.phone = phone
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def to_dict(self):
        return{
           "Account_Number" : self.account_number,
           "Name" : self.name,
           "Age" : self.age,
           "Phone" : self.phone,
           "Account_Type" : self.account_type,
           "Balance" : self.balance,
           "Transactions" : self.transactions
        }



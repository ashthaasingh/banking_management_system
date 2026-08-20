# 🏦 Banking Management System

A console-based **Banking Management System** developed using Python.
This project allows users to create and manage bank accounts, perform transactions, and store account information using JSON file storage.

The project is built using **Object-Oriented Programming (OOP)** concepts and Python file handling.

---

## 📌 Features

### Account Management

* Create a new bank account
* View all accounts
* Search for an account
* Delete an account

### Banking Operations

* Deposit money
* Withdraw money
* Transfer money between accounts
* View transaction history

### Data Management

* Store account information in JSON
* Load account information from JSON
* Automatically update account balance after transactions
* Store transaction records for each account

### Validation

* Prevent negative or zero deposits
* Prevent negative or zero withdrawals
* Prevent withdrawal when the balance is insufficient
* Prevent transfers when the sender has insufficient balance
* Prevent transferring money to the same account
* Handle account-not-found situations

---

## 🛠️ Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**
* **JSON**
* **File Handling**
* **Git & GitHub**

---

## 📂 Project Structure

```text
banking_management_system/
│
├── main.py
│
├── data/
│   └── accounts.json
│
├── src/
│   ├── account.py
│   ├── menu.py
│   ├── operations.py
│   └── storage.py
│
├── .gitignore
│
└── README.md
```

### File Description

| File            | Purpose                                          |
| --------------- | ------------------------------------------------ |
| `main.py`       | Main entry point of the application              |
| `account.py`    | Contains the `Account` class                     |
| `menu.py`       | Displays the banking menu                        |
| `operations.py` | Contains banking operations                      |
| `storage.py`    | Handles saving and loading JSON data             |
| `accounts.json` | Stores account data locally                      |
| `.gitignore`    | Prevents sensitive/local files from being pushed |

---

## ⚙️ How the Project Works

The application follows a simple flow:

```text
Start Application
       ↓
Display Menu
       ↓
Select Operation
       ↓
Perform Operation
       ↓
Update Account Data
       ↓
Save Data to JSON
       ↓
Return to Menu
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <https://github.com/ashthaasingh/banking_management_system.git>
```

### 2. Open the Project

```bash
cd banking_management_system
```

### 3. Run the Application

```bash
python main.py
```

If `python` does not work on Windows, try:

```bash
py main.py
```

---

## 📋 Main Menu

The application provides the following options:

```text
========== BANKING MANAGEMENT SYSTEM ==========

1. Create Account
2. View Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Transfer Money
7. Transaction History
8. Delete Account
9. Exit
```

---

## 💳 Account Creation

When creating an account, the user provides:

* Name
* Age
* Phone number
* Account type

A unique account number is generated automatically.

Example:

```text
Enter Your Name: Astha
Enter Your Age: 20
Enter Your Phone Number: 9876543210
Enter Account Type: Savings

Account Created Successfully!
Your Account Number is: 1001
```

---

## 💰 Deposit Money

Users can deposit money into an existing account.

Example:

```text
Enter Account Number: 1001
Enter Amount to Deposit: 5000

Deposit Successful!
Deposited Amount: 5000
New Balance: 5000
```

The transaction is also stored in the account's transaction history.

---

## 💸 Withdraw Money

Users can withdraw money if sufficient balance is available.

Example:

```text
Enter Account Number: 1001
Enter Amount to Withdraw: 1000

Withdrawal Successful!
Withdrawn Amount: 1000
Remaining Balance: 4000
```

If the withdrawal amount is greater than the available balance:

```text
Insufficient Balance!
Available Balance: 4000
```

---

## 🔄 Transfer Money

Money can be transferred from one account to another.

Example:

```text
Enter Sender Account Number: 1001
Enter Receiver Account Number: 1002
Enter Amount to Transfer: 2000

Transfer Successful!
Transferred Amount: 2000
Remaining Balance: 2000
```

The transaction is recorded for both accounts.

---

## 📜 Transaction History

Users can view the transaction history of an account.

Example:

```text
========== Transaction History ==========

Transaction Type: Deposit
Amount: 5000

Transaction Type: Withdraw
Amount: 1000

Transaction Type: Transfer Sent
Amount: 500
```

---

## 🔍 Search Account

Users can search for an account using the account number.

```text
Enter Account Number to search: 1001
```

The system displays the account details if the account exists.

---

## 🗑️ Delete Account

Users can delete an existing account after confirmation.

```text
Are you sure you want to delete this account? (yes/no): yes

Account deleted successfully!
```

---

## 💾 Data Storage

Account information is stored locally in:

```text
data/accounts.json
```

The application uses Python's built-in `json` module to save and retrieve account information.

Example data:

```json
[
    {
        "Account_Number": 1001,
        "Name": "Astha",
        "Age": 20,
        "Phone": "9876543210",
        "Account_Type": "Savings",
        "Balance": 4000,
        "Transactions": [
            {
                "Type": "Deposit",
                "Amount": 5000
            },
            {
                "Type": "Withdraw",
                "Amount": 1000
            }
        ]
    }
]

---

## 🧠 Concepts Learned

This project demonstrates several Python programming concepts:

* Classes and Objects
* Constructors
* Methods
* Encapsulation
* Lists and Dictionaries
* Functions
* Loops
* Conditional Statements
* Pattern matching using `match-case`
* Exception/error handling
* JSON serialization
* File handling
* Modular programming
* Git and GitHub

---

## 🔮 Future Improvements

The project can be extended with more advanced features:

* 🔐 PIN-based authentication
* 🔑 Login system
* 🧾 Unique transaction IDs
* 🕒 Transaction date and time
* 📄 Bank statement generation
* 📊 Expense analysis
* ⚠️ Low-balance alerts
* 💳 Daily transaction limits
* 🛡️ Account freeze/unfreeze
* 👨‍💼 Admin dashboard
* 💰 Interest calculation
* 🗄️ MySQL database integration
* 🌐 Convert the CLI application into a web application using Flask

---

## 🎯 Project Goal

The main goal of this project is to build a practical banking application while improving understanding of **Python, OOP, file handling, data management, and software development practices**.

---

## 👩‍💻 Author

**Astha**

Computer Engineering Student

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

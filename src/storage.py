import json
import os

FILE_PATH = "data/account.json"

def load_accounts():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_accounts(data):
    os.makedirs("data", exist_ok=True)

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)            
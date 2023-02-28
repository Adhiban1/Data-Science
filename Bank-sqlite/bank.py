import sqlite3
import pandas as pd

db = sqlite3.connect('bank.db')
cursor = db.cursor()

def reset():
    cursor.execute('DELETE FROM transactions')
    cursor.execute('DELETE FROM users')
    cursor.execute("UPDATE bank_data set value = 0 WHERE variable = 'balance'")
    cursor.execute("UPDATE bank_data set value = 100000 WHERE variable = 'account_no'")
    db.commit()

def db_to_csv():
    transactions = pd.read_sql('select * from transactions', db)
    transactions.to_csv('csv/transactions.csv', index=False)
    users = pd.read_sql('select * from users', db)
    users.to_csv('csv/users.csv', index=False)    

class Bank:
    def __init__(self):
        cursor.execute("SELECT value FROM bank_data WHERE variable = 'balance'")
        self.balance = cursor.fetchone()[0]
        cursor.execute("SELECT value FROM bank_data WHERE variable = 'account_no'")
        self.account_no = cursor.fetchone()[0]

    def trans(self, from_, to_, amount):
        cursor.execute('INSERT INTO transactions VALUES ({}, {}, {})'.format(from_, to_, amount))
        db.commit()

    def add_users(self, amount):
        cursor.execute('INSERT INTO users VALUES ({}, {})'.format(self.account_no, amount))
        db.commit()
        self.balance += amount
        self.trans(self.account_no, 1, amount)
        self.account_no += 1

    def get_balance(self, account_no):
        cursor.execute(f'''
        SELECT balance from users
        WHERE account_no = {account_no}''')
        result = cursor.fetchone()[0]
        return result

    def load_balance(self, account_no, balance):
        cursor.execute(f'''
        UPDATE users
        SET balance = {balance}
        WHERE account_no = {account_no}''')
        db.commit()

    def deposit(self, account_no, amount):
        balance = self.get_balance(account_no)
        balance += amount
        self.load_balance(account_no, balance)
        self.trans(account_no, 1, amount)
        self.balance += amount

    def withdraw(self, account_no, amount):
        balance = self.get_balance(account_no)
        if balance >= amount:
            balance -= amount
            self.load_balance(account_no, balance)
            self.trans(1, account_no, amount)
            self.balance -= amount

    def update_bank_data(self):
        cursor.execute(f"UPDATE bank_data set value = {self.balance} WHERE variable = 'balance'")
        cursor.execute(f"UPDATE bank_data set value = {self.account_no} WHERE variable = 'account_no'")
        db.commit()

    def transaction(self, from_, to_, amount):
        from_balance = self.get_balance(from_)
        if from_balance >= amount:
            from_balance -= amount
            self.load_balance(from_, from_balance)
            to_balance = self.get_balance(to_)
            to_balance += amount
            self.load_balance(to_, to_balance)
            self.trans(from_, to_, amount)

if __name__ == '__main__':
    reset()
    bank = Bank()
    bank.add_users(1000)
    bank.add_users(1000)
    bank.add_users(1000)
    bank.deposit(100000, 400)
    bank.withdraw(100000, 1000)
    bank.transaction(100000, 100001, 200)
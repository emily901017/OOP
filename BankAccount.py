# 1. 銀行帳戶管理系統
# 需求：

# 設計一個 BankAccount 類別，包含：

# 屬性：帳戶名稱（name）、帳戶餘額（balance）

# 方法：deposit(amount)、withdraw(amount)、get_balance()
# 目標：練習屬性與方法的封裝與操作。

class BankAccount:

    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance  

    def deposit(self,amount):  #不能縮排，會被定義在init裡面
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount 

    def get_balance(self): #(self）需定義參數
        return self.balance
    
acct = BankAccount("Emily",1000)
acct.deposit(500)
acct.withdraw(100)
print(f"{acct.name}  帳戶餘額： {acct.get_balance()}") #{name}沒被定義 >>> {acct.name}



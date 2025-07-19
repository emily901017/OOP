# 5. 員工薪資系統
# 需求：

# 建立 Employee 父類別，屬性為姓名與基礎薪資，方法為 calculate_salary()

# 子類別 FullTimeEmployee 固定薪資，PartTimeEmployee 時薪乘以工作時數

# 透過 list 處理不同員工，統一列出每人的薪資
# 目標：練習繼承、方法覆寫（override）、多型

class Employee:
    def __init__(self,name,basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self): #已經在 __init__ 中把 name 存進 self.name，所以之後只要用 self.name 就能存取員工名字，不需要再透過參數傳進來
        return self.basic_salary
    
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.basic_salary

class PartTimeEmployee(Employee):
    def __init__(self,name,hourly_wage,hours_worked):
        super().__init__(name, 0) #因為繼承自 Employee，所以它需要呼叫 Employee 的 __init__() 來初始化共同屬性（像是 name）。否則 self.name 在後面就不能用了，會報錯。「basic_salary 對兼職來說不重要」，給 0 就好，只是為了符合父類別 __init__() 的參數結構
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_salary(self):
          return self.hourly_wage * self.hours_worked

employees = [
    FullTimeEmployee("Alice", 50000),
    PartTimeEmployee("Bob", 200, 60),
    FullTimeEmployee("Charlie", 60000),
    PartTimeEmployee("Diana", 180, 40)
]

for employee in employees:
    print(f"{employee.name}為 {employee.calculate_salary()}元")
# 6. 交通工具資訊系統
# 需求：

# 父類別 Vehicle：屬性為品牌、型號、價格

# 子類別 Car 和 Bike，各自加入不同的屬性

# 撰寫函式能印出所有交通工具的完整資訊
# 目標：多型 + 類別結構設計

class Vehicle:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def get_info(self):
        return f"品牌：{self.brand} 型號：{self.model} 價錢：{self.price}" #多型要每個類別都寫一個 get_info() 方法來印出自己該有的完整資訊
    
class Car(Vehicle):
    def __init__(self,brand,model,price,color):
        super().__init__(brand,model,price)  #叫父類別的 __init__ 方法
        self.color = color

    def get_info(self):
        basic_info =super().get_info() #叫父類別的 get__info() 方法
        return f"{basic_info} 顏色：{self.color}" #再補上自己特有的資訊

class Bike(Vehicle):
    def __init__(self, brand, model, price,color,type):
        super().__init__(brand, model, price)
        self.color = color
        self.type = type
    
    def get_info(self):
        basic_info = super().get_info()
        return f"{basic_info} 顏色：{self.color} 類型：{self.type}"
    
def show_list(vehicle:Vehicle):
    return vehicle.get_info()



Vehicle1 = Car("Tesla","ModelX","200萬","Black")
Vehicle2 = Bike("Giant","XYZ","3萬","White","公路車")

print(show_list(Vehicle1))
print(show_list(Vehicle2))
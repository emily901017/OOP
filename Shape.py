# 7. 幾何圖形面積計算
# 需求：

# 父類別 Shape：方法 get_area()、get_name()

# 子類別 Circle、Rectangle、Triangle，分別實作面積計算

# 撰寫函式接收 Shape，統一呼叫方法計算並輸出
# 目標：抽象設計、方法覆寫、多型應用

from abc import ABC, abstractmethod
import math 

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    def get_name(self):
        return self.__class__.__name__ #self.__class__：這個物件所屬的類別，self.__class__.__name__：該類別的名稱

    def __str__(self):
        return f"{self.get_name()}面積為：{self.get_area()}"

class Circle(Shape):
    #name = "圓型" 若想把名稱改為中文可以加這行
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius **2 
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width 
        self.height = height 

    def get_area(self):
        return self.width * self.height
      
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
      

    def get_area(self):
        return self.base * self.height /2 
    
Shape1 = Circle(5)
Shape2 = Rectangle(2,4)
Shape3 = Triangle(6,8)

print(Shape1)
print(Shape2)
print(Shape3)
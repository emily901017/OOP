# 動物叫聲系統
# 請你設計一個抽象類別 Animal，裡面包含抽象方法 make_sound()。然後建立兩個子類別：

# Dog，輸出 "汪！"

# Cat，輸出 "喵～"

# 要求：
# 使用 from abc import ABC, abstractmethod

# 強制所有子類都必須實作 make_sound

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return f"woof!"
    
    def __str__(self):
        return self.make_sound()
    
class Cat(Animal):
    def make_sound(self):
        return f"喵喵～"
    
    def __str__(self):
        return self.make_sound()

a1 = Cat()
a2 = Dog()
print(a1)
print(a2)
        
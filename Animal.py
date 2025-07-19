# 動物叫聲模擬器
# 需求：

# 建立一個 Animal 父類別，具有方法 make_sound()

# 建立 Dog、Cat 等子類別，分別實作不同叫聲

# 撰寫一個函式 play_sound(animal: Animal)，傳入任何子類別物件都能正確叫聲
# 目標：練習繼承與多型（polymorphism）

class Animal:
    def __init__(self,name):
        self.name = name
    def make_sound(self):
        print("animal sound")

class Dog(Animal):
    def make_sound(self):
        return(f"woof!") #用print的話 一樣會有woof! 只是因為函式本身沒有用 return 回傳任何值 所以會出現 None 

class Cat(Animal):
    def make_sound(self):
        return(f"喵～～") 

def play_sound(animal:Animal):
    return(f"{animal.name}的聲音：{animal.make_sound()}") 

a1 = Dog("熊仔")
a2 = Cat("努努")

print(play_sound(a1))
print(play_sound(a2))
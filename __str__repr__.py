# 請定義一個 Student 類別，包含：

# name（姓名）

# scores（分數列表，例如 [90, 80, 100]）

# 請實作：

# __str__()：輸出格式為「小明的平均分數是：90.0 分」

# __repr__()：輸出格式為 Student(name='小明', scores=[90, 80, 100])

class Student:
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores

    def average_score(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"{self.name}的平均分數是：{self.average_score()}分"
    
    def __repr__(self):
        return f"Student(name ={self.name}, scores={self.scores})"
    
Student1 = Student("小明",[90, 80, 100])

print(Student1)
print(repr(Student1))

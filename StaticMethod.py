# 計算圓面積
# 請你完成一個 CircleTool 類別，它不用建立任何物件，只要提供一個工具函式 area(radius)，回傳該半徑的圓面積（面積 = π × r²）。

# 要求：
# 使用 @staticmethod

# 不需要 self、不需要物件

# 輸入半徑為 5 時，請印出面積
import math

class CircleTool:
    @staticmethod #不用建物件，也不用self
    def area(radius):
        return math.pi * radius ** 2

print(CircleTool.area(5))

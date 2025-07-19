# 2. 簡單購物車系統
# 需求：

# 建立一個 Product 類別，有產品名稱與價格

# 建立一個 ShoppingCart 類別，能夠：

# 加入商品

# 顯示所有商品

# 計算總金額
# 目標：練習多個類別的協作（composition）、封裝、清楚的物件行為。

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class ShoppingCart:
    def __init__(self):
        self.items = []  # 初始化一個空的商品清單

    def add_product(self,product):
        self.items.append(product)
    
    def show_products(self):
        for item in self.items:
            print(f"商品名稱：{item.name} 商品價格：{item.price}") #self.items 是購物車裡「已加入的所有商品」你只需要從這個清單 for item in self.items 迴圈印出每個商品的內容，不需要多餘的 product 參數

    def total_amount(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
    
product1 = Product("西瓜",100)
product2 = Product("草莓",200)

cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)

print("商品購物清單：")
cart.show_products()
print(f"總金額：{cart.total_amount()}")

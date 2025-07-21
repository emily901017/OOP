# 建立不同帳號類型的使用者
# 請你完成一個 User 類別，讓它可以透過 class method 建立以下兩種帳號：

# admin_user(name) → 會產生一個名稱為 name、角色是 "admin" 的使用者

# guest_user() → 會產生一個名稱為 "Guest"、角色是 "guest" 的使用者

# 要求：
# 使用 @classmethod >>> 為了操作整個類別本身（而不是單一物件），讓你能夠建立新的物件方式、處理整體設定，或者提供與「這個類別」有關的功能

# 顯示產生的使用者名稱與角色

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod #要縮排在class User 裡面，這樣它們才是 User 類別的方法
    def admin(cls, name):
        return cls(name, role="admin")

    @classmethod
    def guest_user(cls):
        return cls(name="Guest", role="guest")

U1 = User.admin("Emily")
U2 = User.guest_user()


print(U1.name, U1.role)  
print(U2.name, U2.role)  

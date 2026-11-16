zll = 27
if not (0 <= zll <= 20):
    print(f"{zll} 在0-20之间")
    print(f"欢迎您进入")
    print(f"欢迎您进入2")
else:
    print(f"{zll} 不在0-20之间")
    print(f"欢迎您出去")
    print(f"欢迎您出去2")
print("ddd\n")

account_database = "123"
password_database = "456"

account = input("请输入账号：")
password = input("请输入密码：")

if account == account_database and password == password_database:
    print(f"账号：{account}欢迎您----")
    print("您非常棒")
else:
    print(f"账号：{account}输入的密码不正确--v--")
    print("请您重新输入")

year = int(input("请输入年份："))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year}是瑞年")
elif (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0):
    print(f"{year}是瑞年2")
else:
    print("结束")

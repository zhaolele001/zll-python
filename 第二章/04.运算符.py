# 第术运算待:
print("10 + 4 =", 10 + 4)  # 加
print("10 - 4 =", 10 - 4)  # 藏
print("10 * 4 =", 10 * 4)  # 乘
print("10 / 4 =", 10 / 4)  # 除 小数
print("10 // 4 =", 10 // 4)  # 整除(结果为整数) 2
print("10 % 4 =", 10 % 4)  # 取余/建频 2
print("10 ** 4 =", 10 ** 4)  # 器指数,10的4次方 10000

# 算术预算的优先级---> ** ->
f = 0.1 + 10 / 4 ** 2
print(f)
print(type(f))

# 案类： 输入两个数计算加和减

x = float(input("请输入x:"))
y = float(input("请输入y:"))

print("x + y = ", x + y)
print("x - y = ", x - y)
# x + y =  0.9
# x - y =  0.09999999999999998 --->精度损失


# ---------------------------------------------------------------
# 赋值运算符
num = 85

num -= 10  # num = num - 10

print("num -= 10 后,num=", num)

num *= 10  # num = num * 10

print("num *=10后,num=", num)

num /= 10  # num= num /10

print("num/=10后，num=", num)

num //= 10  # num = num // 10

print("num//=10 后,num=", num)

num %= 3  # num = num % 3

print("num%=3后,num=", num)

num **= 3  # num = num ** 3

print("num **= 3后，num=", num)


#比较预算符
# == !=  > >= < <=

#逻辑运算符


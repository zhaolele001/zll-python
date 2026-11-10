# 常见数据类型 type(num)
from types import NoneType

print("hello python")
print(type("hello python"))

num = 3
print(type(num))

num = "211"
print(type(num))

num = True
print(type(num))

num = 3.14
print(type(num))

num = None
print(type(num))

# hello python
# <class 'str'>
# <class 'int'>
# <class 'str'>
# <class 'bool'>
# <class 'float'>
# <class 'NoneType'>
# isinstance(123, int) 返回bool值
print(isinstance(123, int))
print(isinstance(3.14, float))
print(isinstance("123", str))
print(isinstance(True, bool))
print(isinstance(None, NoneType))

# 字符串
# 定义字符串的三种方式
# 双引号
s1 = "hello"
# 单引号
s2 = 'python'
# 三引号
s3 = """  #555
    hello
    python
    欢迎入坑Java
"""
print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))

# 转义字符 It's very interesting
# 转义字符 \' \" \n \t
s4 = 'It\'s very interesting'

# 字符串拼接
s5 = "人生苦短"  "," "我用java"
print(s5)
s6 = "人生苦短"
s7 = "我用java"
age = 18
print("赵乐乐说：" + s6 + "," + s7)
# + 号可以用来拼接两个字符串，无法将非字符串与字符串进行拼接
print(str(age) + "岁的赵乐乐说:" + s6 + "," + s7)

# 字符串格式化
# %s占位符
print("赵乐乐说：%s, gingham：%s，多少：%s" % (s6, s7, age))
# f"内容{变量表达式}"  企业开发当中使用
print(f"赵乐乐说：{s6}，啥办法：{s7},多少：{age}")






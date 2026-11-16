day = input("请输入星期（1-7）")
match day:
    case "1":
        print("星期1")
    case "2" if 2 == 3:# 并且满足if条件
        print("星期二")
    case "3":
        pass #啥也不干，空语句，占位的作用
    case "6" | "7":
        print("星期天")
    case _: #匹配其他所有情况
        print("输入有误")
"""
    普通闰年 = 可被4除，但不能被100除
    实际闰年 = 可被400整除

    输入年份，如果该年份是闰年输出 True 否则输出 False
"""

# 执行无限循环
while True:

    # 提供用户输入年份，赋值给 year
    year = int(input("请输入年份： "))

    # 判断如果 year 的值为 0， 则退出循环
    if year == 0:
        print()
        print("Goodbyeeee....")
        print()
        # 跳出循环程序，只能用在 for 和 while 循环
        break
    
    # 判断如果 year 的值大于等于 10000 或者 小于等于 1000，提示年份有误，重新输入
    if year >= 10000 or year <= 1000:
        print("Sorry, year incorrect...\nPlease try again...")
        # 继续循环程序
        continue

    # 计算用户输入的年份
    is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    # 输出结果 True or False
    # True = 闰年
    # False = 不是闰年
    print(is_leap)
from random import randint

# 执行无限循环
while True:

    # 随机号码
    num = randint(1, 6)

    # 如果号码为 1， 则打扫房间
    if num == 1:
        activity = "打扫房子"
    # 如果号码为 2， 则洗衣煮饭
    elif num == 2:
        activity = "洗衣煮饭"
    # 如果号码为 3， 则吃喝拉撒
    elif num == 3:
        activity = "吃喝拉撒"
    # 如果号码为 4， 则东奔西跑
    elif num == 4:
        activity = "东奔西跑"
    # 如果号码为 5， 则约会看戏
    elif num == 5:
        activity = "约会看戏"
    # 如果号码为 6， 则在家休息
    elif num == 6:
        activity = "在家休息"
    
    # 输出号码的结果
    print(activity)

    # 选择是否继续执行程序，将字母转换小写
    choice = input("是否继续？(Y/N)").lower()
    # 如果choice的值是 "n"，则退出循环程序 
    if choice == "n":
        print("Goodbyeee....")
        break
    # 否则，继续循环程序
    else:
        continue

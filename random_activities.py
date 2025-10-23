from random import randint

activities = {1: "吃饭", 2: "约会",3: "打扫",4: "睡觉",5: "玩游戏",6: "耍废"}

num = randint(1, 6)

print(activities[num])

"""
    百分制成绩转等级制成绩
    90分以上    --> A
    80分-89分   --> B
    70分-79分   --> C
    60分-69分   --> D
    60分以下    --> E
"""

grade = ""

score = float(input("请输入成绩： "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif 0 <= score <= 59:
    grade = "E"
else:
    print("你输入的成绩不正确，请重新输入")


print(f"成绩等级是: {grade}")
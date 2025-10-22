"""
    练习2：输入圆的半径计算计算周长和面积
    周长公式：2*pi*r
    面积公式：pi*r*r
"""

import math

radius = float(input("请输入圆的半径： "))
perimeter = math.pi * 2 * radius
area = math.pi * radius * radius

print(f"周长 = {perimeter:.2f}")
print(f"面积 = {area:.2f}")
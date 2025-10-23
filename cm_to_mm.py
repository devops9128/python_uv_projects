"""
    英寸转换厘米
    1 inch = 2.54 cm

    输入：长度 value 与 单位 unit
    输出：另外一类的长度与单位
"""

value = float(input("请输入长度： "))
unit = input("请输入想转换的单位(in/cm)： ")

# 如果输入的是厘米
if unit == "cm" or unit == "厘米":
    output_value = value / 2.54
    print(f"{value:.1f}厘米 = {output_value:.1f}英寸")
elif unit == "in" or unit == "英寸":
    output_value = value * 2.54
    print(f"{value:.1f}英寸 = {output_value:.1f}厘米")
else:
    print("请输入有效单位")
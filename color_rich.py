from rich import print
from rich import pretty
from rich.console import Console

console = Console()

pretty.install()

console.print([1, 2, 3])

# 蓝色字体 + 底线
console.print("[blue underline]Looks like a link")

# 打印locals内置方法
console.print(locals())

# 白色字体，红色字体背景
console.print("FOO", style="white on red")

# 用日志形式输入 Hello world，有时间显示
console.log("Hello world")

console.print("Hello world!!", style='blink')


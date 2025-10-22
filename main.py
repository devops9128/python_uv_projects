from rich import print
from rich.progress import track
from rich.console import Console
from rich.syntax import Syntax
import time

my_code = """
def iter_first(values: Iterable[T]): -> Iterable[Tuple[bool. bool. T]]]:
    try:
        previous_value = next(iter_values)
    except StopIteration:
        return
    first = True
    for value in iter_values:
        yield first, False, previous_value
        first = False
        previous_value = value
    yield first, True, previous_value
"""

def main():
    print("[bold magenta]Hello from practice![/bold magenta]")
    print("[bold cyan]Hello World![/bold cyan]")
    print("This is a code!\n:smiley:")

def test_rich():
    for step in track(range(100)):
        print(step)
        time.sleep(0.1)




if __name__ == "__main__":
    main()
    test_rich()
    syntax = Syntax(my_code, "Python", theme="monokai", line_numbers=True)
    console = Console()
    console.print(syntax)
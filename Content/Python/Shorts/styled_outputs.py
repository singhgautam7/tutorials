# Known as ANSI escape sequences
# Allows you to style terminal o/p
# O/p can be different for each terminal
my_color_code = '\033[35m'
end = '\033[0m'
print(f"{my_color_code}Namaste World{end}")


class Style:
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    THANOS = '\033[35m'
    END = '\033[0m'

print(f"{Style.THANOS}Namaste World{Style.END}")

# pip install rich
from rich.console import Console
c = Console()
c.print("Namaste World, it's Rich!", style="bold red")

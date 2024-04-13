import sys
import random
from pyfiglet import Figlet

fig = Figlet()
fonts = fig.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
    fig.setFont(font = f)
    x = str(input("Input: "))
    print("Output: ")
    print(fig.renderText(x))
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and (sys.argv[2] in fonts):
    fig.setFont(font = sys.argv[2])
    x = str(input("Input: "))
    print("Output: ")
    print(fig.renderText(x))
else:
    sys.exit("Invalid Usage")
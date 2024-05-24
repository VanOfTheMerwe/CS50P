import random
from pyfiglet import Figlet
import sys

figlet = Figlet()
figlet.getFonts()

if len(sys.argv) == 1:
    isRandom = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandom = False
else:
    print('Invalid Usage')
    sys.exit(1)

if isRandom == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print('Invalid Usage')
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

txt = input("Give Input:")
print('Output:',figlet.renderText(txt))


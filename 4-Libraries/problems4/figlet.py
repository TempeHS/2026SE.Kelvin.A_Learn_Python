from pyfiglet import Figlet
figlet = Figlet()

figlet.getFonts()

user = input("Enter font name: ").strip().split(maxsplit=2)

if len(user) < 3 or user[0] != ("-f" or "--font"):
    print("Invalid Usage")
    exit(1)

f = user[1]
s = user[2]

if f in figlet.getFonts():
    figlet.setFont(font=f)
    print(figlet.renderText(s))
else:
    print("???/")
    exit(1)



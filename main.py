import os
from colorama import Fore, Style
from ui import banner, loader

os.system("clear")

# Loading Animation
loader.loading("Starting GCS Toolbox")

# Banner
print(Fore.RED + """
██████╗  ██████╗███████╗
██╔════╝ ██╔════╝██╔════╝
██║  ███╗██║     ███████╗
██║   ██║██║     ╚════██║
╚██████╔╝╚██████╗███████║
 ╚═════╝  ╚═════╝╚══════╝

GHOST CYBER SQUAD HACK TOOL BOX
Developers: ZORRO X ZADEX
""" + Style.RESET_ALL)

# Menu
print(Fore.GREEN + """
[1] Information Gathering
[2] Web Security Tools
[3] Password Tools
[4] Network Tools
[5] Wireless Tools
[6] Exploit Learning
[7] Malware Simulator
[8] OSINT Tools
[9] Social Engineering Simulator
[10] AI Assistant 🤖
[0] Exit
""" + Style.RESET_ALL)

c = input("GCS> ")

if c == "1":
    os.system("python3 info_gathering/menu.py")
elif c == "2":
    os.system("python3 web_security/menu.py")
elif c == "10":
    os.system("python3 ai/assistant.py")
elif c == "0":
    print("Exiting...")
    exit()
else:
    print("Invalid Option!")

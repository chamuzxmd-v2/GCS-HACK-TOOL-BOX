from colorama import Fore, Style
from ui import banner, loader
import os

loader.loading("Starting GCS Toolbox")

print(Fore.RED + """
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

if c=="10":
    os.system("python ai/assistant.py")

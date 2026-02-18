import os

os.system("clear")

print("""
██████╗  ██████╗███████╗
██╔════╝ ██╔════╝██╔════╝
██║  ███╗██║     ███████╗
██║   ██║██║     ╚════██║
╚██████╔╝╚██████╗███████║
 ╚═════╝  ╚═════╝╚══════╝

GHOST CYBER SQUAD HACK TOOL BOX
Developers: ZORRO X ZADEX
""")

print("""
1. Information Gathering
2. Web Security Tools
3. Password Tools
4. Network Tools
5. Wireless Tools
6. Exploit Learning
7. Malware Simulator
8. OSINT Tools
9. Social Engineering Simulator
10. Misc Tools
0. Exit
""")

c = input("Select Category: ")

if c == "1":
    os.system("python info_gathering/menu.py")
elif c == "2":
    os.system("python web_security/menu.py")
elif c == "0":
    exit()

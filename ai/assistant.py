from colorama import Fore, Style

print(Fore.CYAN + "🤖 GCS AI Assistant v1 (Offline)" + Style.RESET_ALL)
print("Type 'exit' to quit\n")

knowledge = {
"ip scanner": "IP Scanner එකක් IP ගැන Country, ISP, City වගේ info දෙන tool එකක්.",
"port scanner": "Port Scanner එකක් server open ports හොයාගන්න භාවිතා කරන tool එකක්.",
"ethical hacking": "Ethical hacking කියන්නේ legal permission එකෙන් system test කිරීම.",
"gcs": "GCS TOOLBOX Developed by ZORRO X ZADEX"
}

while True:
    q = input("You> ").lower()
    if q=="exit":
        break
    
    found = False
    for k in knowledge:
        if k in q:
            print("AI>", knowledge[k])
            found = True
    
    if not found:
        print("AI> Sorry, I am learning... Ask about hacking tools or GCS.")

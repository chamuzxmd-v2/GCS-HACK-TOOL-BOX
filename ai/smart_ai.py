import random

responses = [
"Interesting question!",
"Ethical hacking is fun 😎",
"You should learn Python for hacking.",
"Always hack legally.",
"GCS TOOLBOX is powerful 🔥"
]

while True:
    q = input("AI Chat> ")
    if q=="exit":
        break
    print("AI>", random.choice(responses))

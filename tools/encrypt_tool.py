import base64

msg = input("Text: ")
enc = base64.b64encode(msg.encode()).decode()
print("Encrypted:", enc)

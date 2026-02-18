import requests

API_KEY = "AIzaSyChcrMOLeEcyDnPYi4aJwIvX8aJSSbso50"

print("🤖 GCS Cyber Security AI Guide")
print("Type 'exit' to quit\n")

while True:
    q = input("You> ")
    if q.lower() == "exit":
        break

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
    
    data = {
        "contents":[{"parts":[{"text":f"You are a cybersecurity teacher. Explain ethically: {q}"}]}]
    }

    r = requests.post(url, json=data)
    res = r.json()

    try:
        print("\nAI>", res["candidates"][0]["content"]["parts"][0]["text"], "\n")
    except:
        print("AI> Error or API limit reached")

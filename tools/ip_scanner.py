import requests

ip = input("Enter IP: ")
data = requests.get(f"http://ip-api.com/json/{ip}").json()

print("Country:", data.get("country"))
print("City:", data.get("city"))
print("ISP:", data.get("isp"))

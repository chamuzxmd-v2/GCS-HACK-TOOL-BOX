p = input("Password: ")

score = 0
if len(p)>8: score+=1
if any(c.isdigit() for c in p): score+=1
if any(c.isupper() for c in p): score+=1
if any(c in "@#$%" for c in p): score+=1

print("Strength Level:", score, "/4")

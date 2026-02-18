chars = "abc123@#"
length = 4

def gen(prefix, l):
    if l==0:
        print(prefix)
        return
    for c in chars:
        gen(prefix+c, l-1)

gen("", length)

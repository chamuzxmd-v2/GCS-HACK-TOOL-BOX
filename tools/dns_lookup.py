import dns.resolver

domain = input("Domain: ")
for r in dns.resolver.resolve(domain, "A"):
    print("A Record:", r)

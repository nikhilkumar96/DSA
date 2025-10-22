
def subdomainVisits(cpdomains):
    a = {}
    for domain in cpdomains:
        temp = domain.split(" ")
        count = temp[0]
        subdomain = temp[1].split(".")
        for i in range(len(subdomain)):
            if ".".join(subdomain[i:]) not in a:
                a[".".join(subdomain[i:])] = int(count)
            else:
                a[".".join(subdomain[i:])] += int(count)

    res = []
    for key, value in a.items():
        res.append(str(value)+" "+key)
    return res


print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
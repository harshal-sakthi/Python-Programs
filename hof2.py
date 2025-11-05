def emai_builder(domain):
    def build_email(username):
        return f"{username}@{domain}"
    return build_email

gmail = emai_builder("gmail.com")
#print(type(gmail))
ymail = emai_builder("ymail.com")
hotmail = emai_builder("hotmail.com")

print(gmail("Harshal"))
print(ymail("Kaniyan"))
print(hotmail("Nikithan"))
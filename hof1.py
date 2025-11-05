def gmail(user_name, domain="gmail.com"):
    return f"{user_name}@{domain}"
def ymail(user_name, domain="ymail.com"):
    return f"{user_name}@{domain}"
def hotmail(user_name, domain="hotmail.com"):
    return f"{user_name}@{domain}"
def build_email(user_name, email_function):
    return email_function(user_name)
print(build_email("Harshal", gmail))
print(build_email("Kaniyan", ymail))
print(build_email("Nikithan", hotmail))
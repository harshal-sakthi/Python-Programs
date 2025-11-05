def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
create_profile(name="Harshal", age=9)
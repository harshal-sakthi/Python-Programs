class Employee:
    company = "Microsoft"

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

Employee.change_company("Google")
print(Employee.company)
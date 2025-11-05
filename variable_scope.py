#L - E - G - B
#L - Local
from dis import disco


def order():
    product = "Laptop"
    print(f"Your Order is: {product}")
order()
#I comment 8th line because local variable means we create one function we can use that variable inside that function only we cannot use outside the function
#print(product)

#E - Enclosing
def cart():
    discount = 10
    def checkout():
        print(f"Applying Discount: {discount}")
    checkout()
cart()

#G - Global
user_id = "HSRNBF"
def homepage():
    print(f"Welcome: {user_id}")
def profilepage():
    print(f"Welcome to profile page: {user_id}")
homepage()
profilepage()


#B - Built-in variables and functions
#Variable
print(__file__)
#Function
print("HSNBRF".lower())
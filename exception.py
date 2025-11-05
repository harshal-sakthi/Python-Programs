try:
    a=int(input("Enter number 1: "))
    b=int(input("Enter number 2:"))
    c=a/b
    print(c)

except ValueError:
    print("Value Error")
finally:
    print("_______________")
"""except ZeroDivisionError:
    print("ZeroByDivisionError")
except Exception:
    print("Exception")"""


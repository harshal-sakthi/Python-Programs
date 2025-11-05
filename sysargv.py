"""import sys

full_name = sys.argv[1]

email = full_name.lower().replace(' ', '.') + "@company.com"

print("\n ---Your Profile---")
print("Name:", full_name)
print("Generated Email:", email)"""

import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <Full Name>")
    sys.exit(1)

full_name = "".join(sys.argv[1:])

email = full_name.lower().replace(' ', '.') + "@company.com"

print("\n---Your Profile---")
print("Name:", full_name)
print("Generated Email:", email)

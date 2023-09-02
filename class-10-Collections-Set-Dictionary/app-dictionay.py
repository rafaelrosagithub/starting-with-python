# Dictionary
months = {"Jan": "January", "Feb": "February", "Marc": "March"}

print(months)
print(months["Feb"])
print(months.get("Marc"))
print(months.get("abc", "Default"))
print(months.get("Jan", "Default"))
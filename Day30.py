import re

text = """
My name is Sajid.
My email is mahmadsajidshaik@gmail.com.
My phone number is 7842830165.
I have 25 books and 10 pens.
"""

emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
phones = re.findall(r"\b[6-9]\d{9}\b", text)
numbers = re.findall(r"\b\d+\b", text)

print("Emails:", emails)
print("Phone Numbers:", phones)
print("Numbers:", numbers)
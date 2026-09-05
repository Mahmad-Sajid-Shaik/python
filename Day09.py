#String Methods Program:
s = input("Enter a string: ")

print("Capitalize:", s.capitalize())
print("Title:", s.title())
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Swapcase:", s.swapcase())
print("Startswith:", s.startswith("A"))
print("Endswith:", s.endswith("a"))
print("Strip:", s.strip())
print("Count:", s.count("a"))
print("Find:", s.find("a"))
print("Index:", s.index("a") if "a" in s else -1)
print("Replace:", s.replace("a", "A"))
print("Split:", s.split())
print("Is Alpha:", s.isalpha())
print("Is Digit:", s.isdigit())
print("Is Alnum:", s.isalnum())
print("Is Space:", s.isspace())
print("Is Lower:", s.islower())
print("Is Upper:", s.isupper())
print("Is Title:", s.istitle())
print("Is Identifier:", s.isidentifier())

words = s.split()

print("\nList:", words)

words.append("Python")
print("Append:", words)

words.insert(0, "Hello")
print("Insert:", words)

if "Python" in words:
    words.remove("Python")
print("Remove:", words)

if len(words) > 0:
    words.pop()
print("Pop:", words)

words.extend(["Java", "C"])
print("Extend:", words)

print("Count:", words.count("Java"))
print("Index:", words.index("Java"))

words.reverse()
print("Reverse:", words)

words.sort()
print("Sort:", words)

copy_list = words.copy()
print("Copy:", copy_list)

words.clear()
print("Clear:", words)
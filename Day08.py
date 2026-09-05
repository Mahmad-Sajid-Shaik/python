numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

print("\nList Operations")

print("Indexing:", numbers[0])
print("Negative Indexing:", numbers[-1])
print("Slicing:", numbers[1:4])
print("Concatenation:", numbers + [60, 70])
print("Repetition:", numbers * 2)
print("Membership:", 30 in numbers)
print("Not Membership:", 100 not in numbers)

print("\nList Functions")

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))

print("\nList Methods")

numbers.append(60)
print("Append:", numbers)

numbers.insert(2, 25)
print("Insert:", numbers)

numbers.extend([70, 80])
print("Extend:", numbers)

numbers.remove(30)
print("Remove:", numbers)

numbers.pop()
print("Pop:", numbers)

print("Count:", numbers.count(20))
print("Index:", numbers.index(40))

numbers.sort()
print("Sort:", numbers)

numbers.reverse()
print("Reverse:", numbers)

new_list = numbers.copy()
print("Copy:", new_list)

numbers.clear()
print("Clear:", numbers)
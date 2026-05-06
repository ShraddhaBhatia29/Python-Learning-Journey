# LIST: mutable / changeable
names = ["ram", "shyam", "sonu"]

print(names[0])

names[1] = "shraddha"
print(names)

# Add to end
names.append("ramu")
print(f"names are {names}")

# Remove
names.remove("ramu")
print(f"names are {names}")

# Length of list
print(f"length of list is {len(names)}")

# Last item
print(names[-1])

# Slicing
print(names[1:3])

names.insert(2, "Bhatia")
print(names)

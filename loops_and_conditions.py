# IF ELSE
greeting = "Good Morning"
if greeting == "Morning":
    print("condition matched")
else:
    print("condition not matched")

print("if else code is completed")

print("*************************")

# FOR LOOP
values = [2, 5, 7, 8, 9]
for i in values:
    print(i)

print("*************************")

# Sum of first 5 natural numbers
total = 0
for i in range(1, 6):
    total = total + i

print(f"sum of first 5 natural numbers is {total}")

print("*************************")

# Print odd numbers from 1 to 10
for i in range(1, 10, 2):
    print(i)

print("*************************")

# range example (default starts from 0)
for i in range(10):
    print(i)

print("*************************")

# WHILE LOOP
a = 6
while a > 2:
    print(a)
    a = a - 1

print("*************************")

# WHILE LOOP (skip 4)
a = 6
while a > 2:
    if a != 4:
        print(a)
    a = a - 1

print("*************************")

# BREAK example
print("BREAK example")
it = 4
while it > 1:
    if it == 3:
        break
    print(it)
    it = it - 1

print("while loop execution is done")

print("*************************")

# CONTINUE example
print("CONTINUE example")
it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1

print("while execution done")
``

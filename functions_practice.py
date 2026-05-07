# Function is a group of related statements to perform a specific task.

# Function Declaration
def GreetMe():
    print("Hello Shraddha! You are learning well")

# Function Call
GreetMe()

print("Another Program Output")

# Send parameters in function
def GreetMe(name):
    print(f"Hello Shraddha! You are learning well {name}")

# Function Call
GreetMe("Shraddha Bhatia")

print("Another Program Output")
print("SUM OF 2 INTEGERS")

def sum(a, b):
    print(f"Sum is {a + b}")

sum(4, 2)

# Practice Exercises

# Create a list of numbers: [1, 4, 7, 10]
# Print each number multiplied by 3
values = [1, 4, 7, 10]
for i in values:
    print(i * 3)

print("Another Program Output")

user = [10, 15]
for i in user:
    if i > 5 and i < 11:
        print("Good Morning")
        print("Greeting code has completed.")
    elif i > 12 and i < 17:
        print("Good Afternoon")
        print("Greeting code has completed.")
    elif i > 18 and i < 21:
        print("Good Evening")
        print("Greeting code has completed.")
    else:
        print("Good Night")
        print("Greeting code has completed.")

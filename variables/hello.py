# Ask user for their name
name = input("What's your name? ").strip().title()

# split users name into first name and last name
first, last = name.split(" ")

# Say hello to user
print("Hello,", name)
print(f"Hello, {first}")

# use an escape character
print("hello, \"friend\"")



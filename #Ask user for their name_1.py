#Ask user for their name
name = input("what's your name ? ").strip().title()

# Split the user's name into first and last name
first , last = name.split(" ")

#Say hello to user
print(f"hello, {first}")
print("20 days are " + str(50) + " minutes")
# but this one is better:
print(f"20 days are {50} minutes")
# the letter "f" stands for format

# variables are containers for strong values. here's how to make a variable

# turn this into...
print(f"20 days are {50 * 24 * 60 * 60} seconds")

# this!
toSeconds = 24 * 60 * 60
print(f"20 days are {50 * toSeconds} seconds")

nameOfUnit = "seconds"
print(f"20 days are {50 * toSeconds} {nameOfUnit}")



# that was messy. what about functions instead of variables?


def days_to_units(days):
    print(f"{days} days are {days * toSeconds} {nameOfUnit}")

# functions only run when they are called, shown below


days_to_units(35)
days_to_units(10)
days_to_units(100)
days_to_units(35)

# much cleaner!


# we can also add in multiple data types and also.... CUSTOMIZE!


def days_to_units(days, custom_message):
    print(f"{days} days are {days * toSeconds} {nameOfUnit}")
    print(custom_message)


days_to_units(200, "custom message :)")
days_to_units(12, "this is a diff custom message :)")
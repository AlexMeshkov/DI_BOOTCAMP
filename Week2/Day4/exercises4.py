# def display_message (Alex):
#     display_message('Alex')
#     print(f.("Hello everyone, ma name is{name} Im study in Developers institute"))


# def display_message():
#     print("I am learning programming in this course.")


# # Calling the function to display the message
# display_message()


# Exercise2
# def favorite_book(title):
#     print("One of my favorite books is " + title)


# # Example usage
# favorite_book("Alice in Wonderland")

# Exercise 3


# def describe_city(city="Munich", country="Germany"):
#     print(city + " is in " + country)


# describe_city()
# describe_city("Berlin")
# describe_city("Guangzhou", "China")
# describe_city("Moscow", "Russia")
# describe_city("Kiev", "Ukraine")


# Exercise4

# import random


# def compare_numbers(user_number):
#     random_number = random.randint(1, 100)

#     if user_number == random_number:
#         print("Success! The numbers match.")
#     else:
#         print("Fail! The numbers don't match.")
#         print("User number:", user_number)
#         print("Random number:", random_number)


# compare_numbers(42)  # Replace 42 with the user's input

# Exercise 5


# def make_shirt(size="medium", text="I'm love CSS"):
#     print(f"The size of shirt is {size} and text is {text}")


# make_shirt("L", "'The world is yours'")
# make_shirt("XXXL", "'I love Python'")
# make_shirt("Medium", "I love H.T.M.L")
# make_shirt()
# make_shirt(text="The some text")

# Exercise 6

# magician_names = ["Harry Houdini", "David Blaine", "Cris Angel"]


# def show_magicians(magician_names):
#     for magician in magician_names:
#         print(magician)


# def make_great(magician_names):
#     great_magicians = []

#     while magician_names:
#         magician = magician_names.pop()
#         great_magician = magician + " the Great"
#         great_magicians.append(great_magician)

#     for great_magician in great_magicians:
#         magician_names.append(great_magician)


# show_magicians(magician_names)

# print("\n")
# make_great(magician_names)
# show_magicians(magician_names)

# Exercise 7

# from random import randint


# def get_random_temp():
#     temp = randint(-10, 40)
#     return temp


# print(type(get_random_temp()))


def main():
    rand_temp = get_random_temp()
    print(f"Now a temperature is{rand_temp}Celsius")
    main()

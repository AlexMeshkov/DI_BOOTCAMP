# #

# all_colors = ["red", "blue", "yellow"]
# user_answer = input("Which position of the color?")
# list_answer = user_answer.split("-")

# all_colors.insert(int(list_answer[0]), list_answer[1])
# print(all_colors)

# list of 15 numbers
# if the number is odd --> the number -- is odd
# if the number is even --> the number --is even


# for number in range(0, 15):
#     if number % 2 == 0:
#         print(f"number {number} is even")
# else:
#     print(f"number {number} is odd")

bank_amount = 10000
computer_price = 2000

if bank_amount >= computer_price:
    bank_amount -= computer_price
else:
    print("Please save more money")

# name = "John Doe"
# len_name = len(name)
# if len_name > 20:
#     print(f"Name {name} is more than 20 chars long")
# elif len_name > 15:
#     print(f"Name {name} is more than 15 chars long")
# elif len_name > 10:
#     print(f"Name {name} is more than 10 chars long")
# elif len_name >= 8:
#     print(f"Name {name} is 8, 9 or 10 chars long")
# else:
#     print(f"Name {name} is a short name")
name = "John Doe"
len_name = len(name)
if len_name > 20:
    print(f"Name {name} is more than 20 characters")
elif len_name > 15:
    print(f"Name {name} is more than 15 characters")
elif len_name > 10:
    print(f"Name {name} is more than 10 characters")
elif len_name >= 8:
    print(f"Name {name} is 8, 9 or 10 characters")
else:
    print(f"Name {name} is a short name")

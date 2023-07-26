# Exercise1


# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age


# cat1 = Cat(cat_name="Mary", cat_age=9)
# cat2 = Cat(cat_name="Woody", cat_age=7)
# cat3 = Cat(cat_name="Tommy", cat_age=4)


# def oldest_cat(cat_list: list[Cat]):  # method
#     if len(cat_list) == 0:
#         return None
#         # print(f"{self.cat_name} - The oldest cat!")
#     oldest_cat = cat_list[0]
#     for cat in cat_list:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat

#     return oldest_cat


# oldest = oldest_cat([cat1, cat2, cat3])
# print(f"{oldest.name} is oldest cat with age of {oldest.age}")

# Exercise2


# class Dog:
#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height


# Dog1 = Dog("Kasper", 50)


# def bark():
#     print(f"{self.dog_name} + Woof!!!")


# def jump(self):
#     if self.height == 50:
#         print(f"{self.name} jumps {dog.height} cm high!")
#     else:
#         print(f"{self.name} jumps with {self.legs} legs")


# bark(jump)


# Exercise 4
animals = ["Baboon", "Bear", "Cat", "Cougar", "Eel", "Emu", "Ape"]

# {1: ['Ape'], 2: ['Baboon', 'Bear'], 3: ['Cat', 'Cougar'], 4: ['Eel', 'Emu']}

animals_sorted = sorted(animals)

# ['Ape', 'Baboon', 'Bear', 'Cat', 'Cougar', 'Eel', 'Emu']

print(animals_sorted)

animals_groups = {}

# Creating initial reference
animal_check = animals_sorted[0]  # Ape, first animal
group = 1  # first group

animals_groups[group] = [
    animal_check
]  # adding initial group with the initial animal into the dictionary
# {1: ['Ape']}

for animal in animals_sorted[1:]:  # Cat
    if animal_check[0] == animal[0]:  # B == C
        animals_groups[group].append(animal)
    else:
        group += 1  # 3
        animals_groups[group] = [
            animal
        ]  # {1: ['Ape'], 2: ['Baboon', 'Bear'], 3: {'Cat'}}
        animal_check = animal  # Cat

print(animals_groups)

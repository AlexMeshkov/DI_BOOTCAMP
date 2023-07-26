# class A:
#     def __init__(self) -> None: #method
#         pass

# objectA = A()
# objectA.color = "RED"
# print(objectA.color)
num1 = 2
# multiply_by_two = lambda num: num * 2

# print(multiply_by_two(num1))

a_list = [n for n in range(10)]

b_list = list(map(lambda num: num * 2, a_list))

print(b_list)

c_list = list(filter(lambda num: True if num % 2 == 0 else False, b_list))
print(c_list)

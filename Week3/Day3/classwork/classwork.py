# class Test:
#     def __bool__(self):
#          return False

# test = Test()

# if test:
#     print("Hello World")

# else:
#     print('2-nd variant')

class employee:
    def __init__(self, firstname, lastname, age, job,salary ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary

emp1 = employee( 'Leah', 'Smith', 30, 'developer', 20000)
emp2 = employee('David', 'Shwartz', 20, 'teacher', 17000)

def get_fullname(self):
    return f"{self.firstname} {self.lastname}"


def __gt__(self, other_employee):
    if self.salary > other_employee.salary:
        return self
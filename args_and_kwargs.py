def sum_all(*args):
    return sum(args)

print(sum_all(2, 4, 6))
print(sum_all(10, 20, 30, 40))

def print_greetings(*names):
    for name in names:
        print(f"Hello, {name}!")

print_greetings("Haz", "Ben", "Sara")


def display_info(**kwargs):
    for key,value in kwargs.items():
        print( f"{key}: {value}")
display_info(name="Haz", age=25, city="New York")

def multipy_or_default(a, b=1):
    return a * b

print(multipy_or_default(5))
print(multipy_or_default(5, 3))  

def describe_person(name, **details):
    print(f"Name: {name}")
    for key, value in details.items():
        print(f"{key}: {value}")

describe_person("Alice", age=30, city="Kathmandu")
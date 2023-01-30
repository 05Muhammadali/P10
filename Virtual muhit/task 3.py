with open("planets.txt", "r+") as file:
    read = file.readlines()


def func():
    for i in range(0, len(read) + 1, 5):
        result = read[i].split("\n")[0][7:]
        yield result


my_func = func()

print(next(my_func))
print(next(my_func))
print(next(my_func))
print(next(my_func))

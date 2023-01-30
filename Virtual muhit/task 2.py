with open("test.txt", "r+") as file:
    read = file.read()


def func():
    for i in read:
        yield i


my_generator = func()

for x in range(1, len(read) + 1):
    print(next(my_generator))

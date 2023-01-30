def get_func():
    for i in range(1, 21):
        if i % 2 == 0:
            yield -i
        else:
            yield i


my_generator = get_func()

for i in range(1, 21):
    print(next(my_generator))

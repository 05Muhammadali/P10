def get_next_multiple(num):
    a = num
    for i in range(1, 5):
        yield num + a
        a = num + a


generator = get_next_multiple(2)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
def get_next_prime():
    i = 2
    while True:
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            yield i
        i += 1


prime_generator = get_next_prime()

for a in range(1, 169):
    print(next(prime_generator))

def main_func(dec_func):
    def little_func(a, b):
        return dec_func(a, b)

    return little_func


@main_func
def decorater(a, b):
    return (a + b) * 2


print(decorater(2, 5))
print(decorater(10, 2))
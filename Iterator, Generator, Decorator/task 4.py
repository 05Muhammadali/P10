# ====================================== 1 ======================================

# def only_even_parameters(dec_func):
#     def little_func(a, b):
#         for i in range(1, 3):
#             if a % 2 == 0:
#                 if b % 2 == 0:
#                     return dec_func(a, b)
#                 else:
#                     return "Please add only even numbers!"
#             else:
#                 return "Please add only even numbers!"
#
#     return little_func
#
#
# @only_even_parameters
# def add(a, b):
#     return a + b
#
#
# print(add(2, 8))  # 14
# print(add(1, 4))  # Please add only even numbers!

# ====================================== 2 ======================================

def only_even_parametrs(dec_func):
    def little_func(*args):
        q = 0
        for i in args:
            if i % 2 == 0:
                q += 1
                continue
            else:
                return "Please enter multple only even numbers!"
        if q >= 4:
            return dec_func(*args)

    return little_func


@only_even_parametrs
def multiply(a, b, c, d, s):
    return a * b * c * d * s


print(multiply(2, 6, 4, 8))  # 384
print(multiply(1, 2, 2, 8))  # Please enter multple only even numbers!

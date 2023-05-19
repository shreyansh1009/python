
from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lcm(lst[0], lcm_list(lst[1:]))


lcm_7_6_5_4 = lcm_list([7, 6, 5, 4])


print("The man has", lcm_7_6_5_4, "apples.")

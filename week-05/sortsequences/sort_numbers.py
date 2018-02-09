from datastubs import NUMBER_LIST


def reverse_numerical_order():
    """
    Sort the list of numbers but in reverse order
    """
    return sorted(NUMBER_LIST, reverse=True)


def numerical_order():
    """
    Sort the list of numbers in numerical order
    """
    return sorted(NUMBER_LIST)

    # fill it out

def as_absolute_value():
    """
    The absolute value of a number `n` is its value
    regardless of positive or negative sign
    """
    return sorted(NUMBER_LIST, key=abs)
    # fill it out


def as_inverse_number():
    """
    An inverse of a number `n` is defined as: `1/n`
    The bigger the number, the smaller its inverse, and vice versa
    """
    def inverse(k):
        return 1/k
    sorted(NUMBER_LIST, key=inverse)
    # fill it out


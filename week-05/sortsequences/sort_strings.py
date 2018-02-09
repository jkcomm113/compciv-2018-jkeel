from datastubs import STRING_LIST


def reverse_alpha():
    """
    return the list of strings sorted in
    reverse alphabetical order.
    """

    return sorted(STRING_LIST, reverse=True)


def alpha_case_insensitive():
    """
    return the list of strings sorted in
    alphabetical order, but without regard to
    capitalization
    """
    return sorted(STRING_LIST, key=lambda s: s.lower())
    # fill it out



def by_longest_length():
    """
    Sort in descending order of length of strings
    """
    return sorted(STRING_LIST, key=len)
    # fill it out


def filter_and_sort_number_strings():
    """
    Filter the original list for strings that
    contain numbers. Then sort that list of number
    strings but as strings (i.e. alphaebtical order)
    """
    newList = []
    for s in STRING_LIST:
       if s.isnumeric():
           newList.append(s)
    return sorted(newList)
    # fill it out


def filter_and_sort_number_strings_as_numbers():
    """
    Filter the list for strings that contain numbers
    and then sort that list of strings in *numerical* order
    """
    newerList = []
    for p in STRING_LIST:
        if p.isnumeric():
            newerList.append(p)
    return sorted(newerList, key=int)
    # fill it out



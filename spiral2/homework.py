def spiralize(size, n=1):
    if size != 1:
        return_value = (4 * size * size) - (6 * size) + 6 + spiralize(size - 2, n)

    else:
        return_value = n + 1

    return return_value

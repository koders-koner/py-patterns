def pattern_1(n):
    """Simple triangle
    For n=4:
    *
    **
    ***
    ****
    """
    # TODO: Implement simple right triangle
    result = []
    for i in range(1, n + 1):
        result.append('*' * i)
    return '\n'.join(result)

def pattern_2(n):
    """Number line
    For n=4:
    1 2 3 4
    """
    # TODO: Implement single line of numbers
    return ' '.join(str(i) for i in range(1, n + 1))

def pattern_3(n):
    """Square of stars
    For n=4:
    ****
    ****
    ****
    ****
    """
    # TODO: Implement n x n square
    return '\n'.join('*' * n for _ in range(n))

def pattern_4(n):
    """Reverse triangle
    For n=4:
    ****
    ***
    **
    *
    """
    # TODO: Implement reverse right triangle
    result = []
    for i in range(n, 0, -1):
        result.append('*' * i)
    return '\n'.join(result)

def pattern_5(n):
    """Number column
    For n=4:
    1
    2
    3
    4
    """
    # TODO: Implement vertical numbers
    return '\n'.join(str(i) for i in range(1, n + 1))

def pattern_6(n):
    """Centered triangle
    For n=4:
       *
      ***
     *****
    *******
    """
    # TODO: Implement centered pyramid
    result = []
    for i in range(n):
        result.append(' ' * (n - i - 1) + '*' * (2 * i + 1))
    return '\n'.join(result)

def pattern_7(n):
    """Number pyramid
    For n=4:
       1
      1 2
     1 2 3
    1 2 3 4
    """
    # TODO: Implement number pyramid
    result = []
    for i in range(1, n + 1):
        result.append(' ' * (n - i) + ' '.join(str(j) for j in range(1, i + 1)))
    return '\n'.join(result)

def pattern_8(n):
    """Reverse number pyramid
    For n=4:
    1 2 3 4
     1 2 3
      1 2
       1
    """
    # TODO: Implement reverse number pyramid
    result = []
    for i in range(n, 0, -1):
        result.append(' ' * (n - i) + ' '.join(str(j) for j in range(1, i + 1)))
    return '\n'.join(result)

def pattern_9(n):
    """Diamond pattern
    For n=4:
       *
      ***
     *****
    *******
     *****
      ***
       *
    """
    # TODO: Implement diamond shape
    result = []
    for i in range(n):
        result.append(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for i in range(n - 1):
        result.append(' ' * (i + 1) + '*' * (2 * (n - i - 1) - 1))
    return '\n'.join(result)

def pattern_10(n):
    """Number square
    For n=4:
    1 2 3 4
    1 2 3 4
    1 2 3 4
    1 2 3 4
    """
    # TODO: Implement number square
    return '\n'.join(' '.join(str(i) for i in range(1, n + 1)) for i in range(n))

def pattern_11(n):
    """Pascal's triangle
    For n=4:
       1
      1 1
     1 2 1
    1 3 3 1
    """
    # TODO: Implement Pascal's triangle
    result = []
    prev_row = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        result.append(' ' * (n - i - 1) + ' '.join(map(str, row)))
        prev_row = row
    return '\n'.join(result)

def pattern_12(n):
    """Hollow triangle
    For n=4:
    *
    **
    * *
    ****
    """
    # TODO: Implement hollow right triangle
    result = []
    for i in range(n):
        if i == n - 1:
            result.append('*' * n)
        elif i == 0:
            result.append('*')
        else:
            result.append('*' + ' ' * (i - 1) + '*')
    return '\n'.join(result)

def pattern_13(n):
    """Hollow square
    For n=4:
    ****
    *  *
    *  *
    ****
    """
    # TODO: Implement hollow square
    result = []
    for i in range(n):
        if i == 0 or i == n - 1:
            result.append('*' * n)
        else:
            result.append('*' + ' ' * (n - 2) + '*')
    return '\n'.join(result)

def pattern_14(n):
    """Number diamond
    For n=4:
       1
      2 2
     3   3
    4     4
     3   3
      2 2
       1
    """
    # TODO: Implement number diamond
    result = []
    for i in range(1, n + 1):
        if i == 1:
            result.append(' ' * (n - i) + '1')
        else:
            result.append(' ' * (n - i) + str(i) + ' ' * (2 * (i - 1) - 1) + str(i))
    for i in range(n - 1, 0, -1):
        if i == 1:
            result.append(' ' * (n - i) + '1')
        else:
            result.append(' ' * (n - i) + str(i) + ' ' * (2 * (i - 1) - 1) + str(i))

    return '\n'.join(result)

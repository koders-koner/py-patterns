def pattern_1(n):
    """Simple triangle
    For n=4:
    *
    **
    ***
    ****
    """
    # TODO: Implement simple right triangle
    string = ""
    for x in range(1,n+1):
        for y in range(x):
            string += "*"
        if x != n:
            string += "\n"
    return string

def pattern_2(n):
    """Number line
    For n=4:
    1 2 3 4
    """
    # TODO: Implement single line of numbers
    string = ""
    for x in range(1,n+1):
        string += str(x)
        string += " "
    return string[:-1]

def pattern_3(n):
    """Square of stars
    For n=4:
    ****
    ****
    ****
    ****
    """
    # TODO: Implement n x n square
    string = ""
    for x in range(1, n+1):
        for y in range(1, n+1):
           string += "*"
        if x != n:
            string += "\n"
    return string

def pattern_4(n):
    """Reverse triangle
    For n=4:
    ****
    ***
    **
    *
    """
    # TODO: Implement reverse right triangle
    string = ""
    for x in range(n, 0, -1):
        for y in range(x):
            string += "*"
        if x != 1:
            string += "\n"
    return string

def pattern_5(n):
    """Number column
    For n=4:
    1
    2
    3
    4
    """
    # TODO: Implement vertical numbers
    string = ""
    for x in range(1, n+1):
        string += str(x)
        if x != n:
            string += "\n"
    return string

def pattern_6(n):
    """Centered triangle
    For n=4:
       *
      ***
     *****
    *******
    """
    # TODO: Implement centered pyramid
    string = ""
    space = n-1
    for x in range(1, n+1):
        string += " "*space
        space -= 1
        for y in range((x*2)-1):
            string += "*"
        if x != n:
            string += "\n"
    return string

def pattern_7(n):
    """Number pyramid
    For n=4:
       1
      1 2
     1 2 3
    1 2 3 4
    """
    # TODO: Implement number pyramid
    string = ""
    space = n-1
    for x in range(1, n+1):
        string += " "*space
        space -= 1
        for y in range(1,x+1):
            string += f"{y}"
            if y != x:
                string += " "
        if x != n:
            string += "\n"
    return string

def pattern_8(n):
    """Reverse number pyramid
    For n=4:
    1 2 3 4
     1 2 3
      1 2
       1
    """
    # TODO: Implement reverse number pyramid
    string = ""
    space = 0
    for x in range(n, 0, -1):
        string += " "*space
        space += 1
        for y in range(1,x+1):
            string += f"{y}"
            if y != x:
                string += " "
        if x != 1:
            string += "\n"
    return string

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
    string = ""
    space = n-1
    for x in range(1, n+1):
        string += " "*space
        space -= 1
        for y in range((x*2)-1):
            string += "*"
        string += "\n"
    space += 1
    for x in range(n-1, 0, -1):
        space += 1
        string += " "*space
        for y in range((x*2)-1):
            string += "*"
        if x != 1:
            string += "\n"
    return string

def pattern_10(n):
    """Number square
    For n=4:
    1 2 3 4
    1 2 3 4
    1 2 3 4
    1 2 3 4
    """
    # TODO: Implement number square
    string = ""
    for x in range(n):
        for y in range(1,n+1):
            string += f"{y}"
            if y != n:
                string += " "
        if x != n-1:
            string += '\n'
        
        
    return string

def pattern_11(n):
    """Pascal's triangle
    For n=4:
       1
      1 1
     1 2 1
    1 3 3 1
    """
    # TODO: Implement Pascal's triangle
    import math
    
    string = ""
    count = n - 1
    space = " "
    for x in range(n):
        string += space*count
        count-=1
        for i in range(x + 1):
            string += str(math.comb(x, i))
            if i != x:
                string += " "
        if x != n-1:
            string += "\n"
    return string
    

def pattern_12(n):
    """Hollow triangle
    For n=4:
    *
    **
    * *
    ****
    """
    # TODO: Implement hollow right triangle
    string = ""
    for x in range(1,n+1):
        
        for y in range(x):
            if x == 1 or x == 2 or x == n:
                string += "*"
            else:
                if y == 0 or y == x-1:
                    string += "*"
                else:
                    string += " "
                
        if x != n:
            string += "\n"
        
    return string


def pattern_13(n):
    """Hollow square
    For n=4:
    ****
    *  *
    *  *
    ****
    """
    # TODO: Implement hollow square
    string = ""
    for x in range(1, n+1):
        for y in range(1, n+1):
            if x == 1 or x == n:
                string += "*"
            else:
                if y == 1 or y == n:
                    string += "*"
                else:
                    string += " " 
        if x != n:
            string += "\n"
    return string

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
    string = ""
    space = n-1
    for x in range(1, n+1):
        string += " "*space
        space -= 1
        for y in range(1, x+1):
            if x == 1 or x ==2:
                string += f"{x}"
                if y != x:
                    string += " "
            else:
                if y == 1 or y == x:
                    string += f"{x}"
                    if y != x:
                        string += " "
                else:
                    string += " "
                    if y != x:
                        string += " "
        string += "\n"
    space += 1
    for x in range(n-1, 0, -1):
        space += 1
        string += " "*space
        for y in range(x, 0, -1):
            if x == 1 or x == 2:
                string += f"{x}"
                if y != 1:
                    string += " "
            else:
                if y == 1 or y == x:
                    string += f"{x}"
                else:
                    string += " "
                if y != 1:
                    string += " "
        if x != 1:
            string += "\n"
    return string

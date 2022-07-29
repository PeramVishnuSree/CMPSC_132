#Lab #0
# More information on pass statement:
#    https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement
def sumSquares(numList):
    """
        >>> sumSquares([1,5,-3,5.5,359,8,14,-25,1000])
        1129171.25
        >>> sumSquares([14,5,-3,5,9.0,8,14,7,-846])
        586.0
        >>> sumSquares([-8,-4,1,2,3,4,5,6])
        132

        To verify output is being returned, not printed
        >>> output = sumSquares([1,5,-3,5,45.5,8.5,-5,500,6.7,-25])
        >>> output
        252187.39
    """
    sum = 0
    if len(numList) == 0:
        return None

    for num in numList:
        if num > 5 and num < 500:
            sum += num**2
        elif num%4 == 0:
            sum += num**2
    return sum

if __name__ == "__main__":
    import doctest
    doctest.testmod()
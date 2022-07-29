def average(num_list):
    """ Compute the average of a all numbers in a list of integers
    
        >>> average([1,4,5,78,19])
        21
        >>> average([1,4.6,5,78.08,19])
        21.0
        >>> average([175.9,4.6,5,78.08,19])
        56.0
        >>> average([17, 76, 7, 4, 1, 2, 3, 4, 5, 6])
        12
    """
    total = 0
    count = len(num_list)
    for x in num_list:
        total = total + x
    return total // count   # Integer division
    

# Run doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()

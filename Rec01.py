# Recitation Activity 1

def translate(translation, msg):
    """
        >>> translate({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} , '1 UP 2 down left right forward')
        '2 down 2 up right left forward'
        >>> translate({'a':'b', 'candy':'three cookies'}, 'We are in a house of CANDY')
        'we are in b house of three cookies'
    """

    msg = msg.lower()
    msg = msg.split(' ')
    solution = ''
    for word in msg:
        trans_word = translation.get(word,word) #translates the word or sets the word itself as the value of translated word
        solution += trans_word+' '
    solution = solution.strip(' ')
    return solution
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
# Lab #1
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

def isValid(txt):
    '''
        >>> isValid('qwertyuiopASDFGHJKLzxcvbnm')
        True
        >>> isValid('hello there, fall is here!')
        False
        >>> isValid('123456yh')
        False
        >>> isValid('POIUYTqwerASDFGHlkjZXCVBMn')
        True
        >>> isValid('POIUYTqwerASDFGHlkjZXCVBnn')
        False
        >>> isValid('12aaaaaaaaaaa6543212345678')
        False
    '''

    chars = list(txt) # list contains all the characters in the string
    if len(chars) != 26 or ' ' in chars: # checks the length condition
        return False
    # capitalize all the characters and check if it already exists
    for i in range(len(chars)):
        if chars[i].isalpha() is False:
            return False
        chars[i] = chars[i].capitalize()
        if chars[i] in chars[:i]:
            return False
    return True
    pass

def get_words(filename):
    '''
        Complete the current implementation to work as directed in the handout. No more than 3 lines are required

        .txt file for this doctest is available on Canvas and must be saved in the same directory as your .py file
        >>> get_words('contents.txt')
        ['week', 'bat', 'aquatic', 'eggs', 'threatening', 'crash', 'educated', 'adjoining', 'bent', 'mice', 'belief', 'adjustment', 'blood', 'smooth', 'kaput', 'mountain', 'digestion', 'enchanted', 'wandering', 'fresh']
        >>> len(get_words('contents.txt'))
        20
    '''

    output = []
    with open(filename) as text: # Open, read and close file
        for line in text:        # text contains the entire content of the .txt file
            line = line.strip()
            output.append(line)
        return output
        pass

def get_histogram(words):
    '''
        >>> get_histogram(['hello', 'there', 'spring', 'is', 'here'])
        {5: 2, 6: 1, 2: 1, 4: 1}
        >>> list_of_words = get_words('contents.txt')
        >>> get_histogram(list_of_words)
        {4: 4, 3: 1, 7: 1, 11: 1, 5: 4, 8: 2, 9: 4, 6: 2, 10: 1}
    '''

    hist = {}
    for word in words:
        if len(word) not in hist: # if the key doesn't exist, we add it and set the value to 1
            hist[len(word)] = 1
        else:
            hist[len(word)] = hist[len(word)] + 1 # if the key exists, we increment the value by 1

    return hist
    pass

def removePunctuation(aString):
    '''
        >>> removePunctuation("Dots...................... many dots..X")
        ('Dots                       many dots  X', {'.': 24})
        >>> data = removePunctuation("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
        >>> data[0]
        'I like chocolate cake      It s the best flavor      for real'
        >>> data[1]
        {'!': 4, '(': 1, "'": 1, '.': 3, ';': 1, '$': 1}
        
    '''

    sol1 = ''
    sol2 = {}
    lst = list(aString)
    for char in lst:
        if char.isalpha() is not True:
            sol1 += ' ' # if it's not an alphabet, we add blank space
            if char in sol2:
                sol2[char] +=1
            else:
                if char == ' ':
                    continue
                sol2[char] = 1
        else:
            sol1 += char

    return sol1,sol2
    pass

if __name__ == "__main__":
    import doctest
    doctest.run_docstring_examples(get_words, globals(), name='LAB1',verbose=True)   ## Uncomment this line if you want to run doctest by function. Replace get_words with the name of the function you want to run
    doctest.testmod() ## Uncomment this line if you want to run the docstring in all functions

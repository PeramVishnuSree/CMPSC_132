# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    for number in range(int(area)) :    # No parameter of the rectangle is going to be grater than its area
        a = number * (perimeter/2-number)    # area
        p = 2*(number+(perimeter/2-number))    # perimeter

        if a == area and p == perimeter:
            if int(number) == number and int(perimeter/2-number) == (perimeter/2-number):    # only integers
                return int(max(number,perimeter/2-number))
            else:
                return False

    return False

def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara','00000':'Alex'})
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    inverted = {}
    duplicates = []    # once a value is found to be a duplicate, we append it here and check for every other element

    for key, value in d.items():
        if value not in inverted and value not in duplicates:
            inverted[value] = key
        elif value in inverted:
            del inverted[value]
            duplicates.append(value)
        elif value in duplicates:
            continue

    return inverted

def successors(file):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    with open(file) as f:
        contents = f.read()

    lst = contents.strip().split()
    contents = ['.']

    for word in lst:  # filter the words in lst by splitting the necessary words by non alphanumeric characters
        j = 0
        if word.isalnum() is False:  # only when there is a non alphanumeric character in th word

            for i in range(len(word)):
                if word[i].isalnum() is False:
                    contents.append(word[j:i])
                    contents.append(word[i])
                    j = i + 1
                elif i == len(word) - 1:
                    contents.append(word[j:i + 1])
                    j = 0
        else:
            contents.append(word)

    final = {}  # final will be the dictionary which contains our solution
    for i in range(len(contents)):

        if i == len(contents) - 1:
            break

        if contents[i] in final:
            if contents[i + 1] in final[contents[i]]:  # goes back to the starting of the loop if the word is not unique
                continue
            else:
                final[contents[i]].append(contents[i + 1])
        else:
            final[contents[i]] = [contents[i + 1]]

    return final

def getPosition(num, digit):
    """
        >>> getPosition(1495, 5)
        1
        >>> getPosition(1495, 1)
        4
        >>> getPosition(1495423, 4)
        3
        >>> getPosition(1495, 7)
        False
    """
    position = 0
    r = -1
    while num != 0 :
        r = num%10
        num = int(num//10)
        position += 1
        if r == digit:
            return position

    return False

def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    solution = []
    while num != 1:
        solution.append(num)
        if num % 2 == 0:
            num = int(num/2)
        else:
            num = int((3*num)+1)
    solution.append(1)

    return solution

def largeFactor(num):
    """
        >>> largeFactor(15)
        5
        >>> largeFactor(80)
        40
        >>> largeFactor(13)
        1
    """
    limit = int(num//2)
    factor = -1
    for number in range(1,limit+1):
        if num % number == 0:
            factor = number
    return factor
    pass

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(largeFactor, globals(), name='HW1',verbose=True)
#replace rectangle for the function name you want to test
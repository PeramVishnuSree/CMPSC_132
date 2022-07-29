# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        if self.top is None:
            return True
        return False

    def __len__(self): 
        count = 1
        if self.top is None:
            return 0
        else:
            cur = self.top
            while cur.next is not None:
                cur = cur.next
                count += 1
            return count

    def push(self,value):
        if self.top is None:
            self.top = Node(value)
        else:
            cur = self.top
            self.top = Node(value)
            self.top.next = cur
     
    def pop(self):
        if self.top is None:
            return None
        else:
            ans = self.top.value
            self.top = self.top.next
            return ans


    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.value


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        try:
            x = float(txt)
            return True
        except:
            return False

    def _getPostfix(self, txt):
        '''
            >>> x=Calculator()
            >>> x._getPostfix('7 ^ 2 ^ 3')
            '7.0 2.0 3.0 ^ ^'
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            'Invalid expression'
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            'Invalid expression'
            >>> x._getPostfix('2    5')
            'Invalid expression'
            >>> x._getPostfix('25 +')
            'Invalid expression'
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            'Invalid expression'
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            'Invalid expression'
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
            'Invalid expression'
        '''

        postfixStack = Stack()
        precedence = {'-': 1, '+': 1, '*': 2, '/':2, '^': 3, '(': 0}
        postfix = ''
        infix = txt.split(' ')
        operands = ['+', '-', '*', '^', '/']
        for j in range(len(infix)):
            if infix[j] == '(' or infix[j] == ')':
                continue
            try:
                if infix[j] in operands:
                    if infix[j-1] == '(' or infix[j-1] == ')' or self._isNumber(infix[j-1]) is True:
                        if infix[j+1] == '(' or infix[j+1] == ')' or self._isNumber(self._isNumber(infix[j+1])) is True:
                            continue
                        else:
                            return "Invalid expression"
                    else:
                        return "Invalid expression"
            except:
                return "Invalid expression"

        try:
            for i in range(len(infix)):
                if self._isNumber(infix[i]) is True:
                    if postfix == '':
                        postfix = str(float(infix[i]))
                        continue
                    postfix += ' ' + str(float(infix[i]))
                else:
                    if infix[i] == '(':
                        postfixStack.push(infix[i])
                        continue

                    elif infix[i] == ')':
                        while postfixStack.peek() != '(':
                            postfix += ' ' + str(postfixStack.pop())
                        postfixStack.top = postfixStack.top.next
                        continue

                    if infix[i] != '^':
                        while postfixStack.peek() is not None and precedence[infix[i]] <= precedence[postfixStack.peek()]:
                            x = postfixStack.pop()
                            postfix += ' ' + str(x)
                        postfixStack.push(infix[i])
                    else:
                        while postfixStack.peek() is not None and precedence[infix[i]] < precedence[postfixStack.peek()]:
                            x = postfixStack.pop()
                            postfix += ' ' + str(x)
                        postfixStack.push(infix[i])

                if i == len(infix)-1 and postfixStack.peek() is not None:
                    while postfixStack.peek() is not None:
                        postfix += ' ' + str(postfixStack.pop())

            if postfixStack.top is not None:
                postfix += ' ' + str(postfixStack.pop())
            return postfix

        except:
            return 'Invalid expression'


    @property
    def calculate(self):
        '''
            
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( ( ( 10 - 2 * 3 ) ) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('( 3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5 ) - 15 + 85 ( 12 )') 
            >>> x.calculate
            >>> x.setExpr("( -2 / 6 ) + ( 5 ( ( 9.4 ) ) )") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()
        postfixexpr = self._getPostfix(self.__expr.strip(' '))
        postfixexpr = postfixexpr.split(' ')
        try:
            if postfixexpr == 'Invalid expression':
                return

            for i in range(len(postfixexpr)):
                if self._isNumber(postfixexpr[i]) is True:
                    calcStack.push(postfixexpr[i])
                else:
                    c = str(postfixexpr[i])
                    x = float(calcStack.pop())
                    y = float(calcStack.pop())
                    if c == '*':
                        sol = y*x
                    elif c == '/':
                        sol = y/x
                    elif c == '^':
                        sol = y**x
                    elif c == '+':
                        sol = y + x
                    elif c == '-':
                        sol = y-x
                    calcStack.push(sol)
            return calcStack.pop()
        except:
            return


#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        if word[0].isalpha() is True and word.isalnum() is True:
            return True
        return False
        pass
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''

        expr = expr.strip(' ').split(' ')
        operators = ['+','-','/','*','^','(',')']
        for i in range(len(expr)):
            if expr[i] not in operators and expr[i].isnumeric() is False and expr[i] not in self.states:
                return

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        pass

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(AdvancedCalculator._isVariable, globals(), name='HW3',verbose=True)
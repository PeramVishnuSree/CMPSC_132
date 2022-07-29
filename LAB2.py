# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

import random

class Fibonacci:
    """
        >>> fib_seq = Fibonacci()
        >>> fib_seq
        <Fibonacci object>, value = 0
        >>> fib_seq.next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next().next()
        <Fibonacci object>, value = 3
        >>> fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
        >>> other_fib_seq = Fibonacci()
        >>> other_fib_seq
        <Fibonacci object>, value = 0
        >>> other_fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
    """

    def __init__(self):
        self.start = 0
        self.prev = 0


    def next(self):
        if self.start == 0:
            self.start = 1
        else:
            n = self.start
            self.start = self.start + self.prev
            self.prev = n
        return Fibonacci()
        pass


    def __repr__(self):
        return f"<Fibonacci object>, value = {self.start}"


class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10'
        >>> east_machine.cancelTransaction()
        'Take your $10 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''

    def __init__(self):
        self.Stock = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        self.Balance = 0
        pass


    def purchase(self, item, qty=1):

        n = False
        for i in self.Stock:
            if (self.Stock[i])[1] != 0:
                n = False
                break
            else:
                n = True

        if item not in self.Stock:
            return 'Invalid item'

        elif n is True:
            return 'Machine out of stock'

        elif self.Stock[item][1] == 0:
            return 'Item out of stock'

        elif self.Stock[item][1] < qty:
            return f'Current {item} stock: {self.Stock[item][1]}, try again'

        elif self.Balance < self.Stock[item][0]*int(qty):

            remaining = self.Stock[item][0]*int(qty)-self.Balance
            return f'Please deposit ${remaining}'

        elif self.Stock[item][0]*int(qty)-self.Balance == 0:

            self.Stock[item][1] -= int(qty)
            self.Balance = 0
            return 'Item dispensed'

        elif self.Balance - self.Stock[item][0]*int(qty) > 0:

            if int(self.Balance - self.Stock[item][0]*int(qty)) == self.Balance - self.Stock[item][0]*int(qty):
                remaining = int(self.Balance - self.Stock[item][0]*int(qty))
            else:
                remaining = self.Balance - self.Stock[item][0]*int(qty)
            self.Stock[item][1] -= int(qty)
            self.Balance = 0
            return f'Item dispensed, take your ${remaining} back'

    def deposit(self, amount):
        n = False
        for i in self.Stock:
            if (self.Stock[i])[1] != 0:
                n = False
                break
            else:
                n = True

        if n is True:
            return f'Machine out of stock. Take your ${amount} back'
        else:
            self.Balance += amount
            return f'Balance: ${self.Balance}'


    def _restock(self, item, stock):

        if item not in self.Stock:
            return 'Invalid item'
        else:
            self.Stock[item][1] += int(stock)
            return f'Current item stock: {self.Stock[item][1]}'

    @property
    def isStocked(self):

        n = False
        for i in self.Stock:
            if (self.Stock[i])[1] != 0:
                n = False
                break
            else:
                n = True
        if n is True:
            return False
        else:
            return True

    @property
    def getStock(self):
        return self.Stock
        pass


    def cancelTransaction(self):
        if self.Balance > 0:
            k = self.Balance
            self.Balance = 0
            return f'Take your ${k} back'

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = 4*line1
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
    '''
    def __init__(self, point1, point2):
        self.p1x = float(point1.x)
        self.p2x = float(point2.x)
        self.p1y = float(point1.y)
        self.p2y = float(point2.y)
        if self.p2x - self.p1x == 0:
            self.slope = float('Infinity')
        else:
            self.slope = round(((self.p2y - self.p1y)/(self.p2x - self.p1x)), 3)
        if self.slope == float('Infinity'):
            self.intercept = self.p1x
        else:
            self.intercept = round(self.p2y - (self.p2x*self.slope),3)
        pass

    @property
    def getDistance(self):
        dist = round((((self.p2x - self.p1x)**2 + (self.p2y - self.p1y)**2)**(1/2)),3)
        return dist
        pass

    @property
    def getSlope(self):
        return self.slope

    def __str__(self):
        if self.slope == float('Infinity'):
            return 'Undefined'
        elif self.slope == 0:
            return f'y = {self.intercept}'
        elif self.intercept == 0:
            return f'y = {self.slope}x'
        return f'y = {self.slope}x + {self.intercept}'

    __repr__ = __str__

    def __mul__(self, other):
        x = Point2D(other*self.p1x, other*self.p1y)
        y = Point2D(other*self.p2x, other*self.p2y)
        return Line(x,y)

    def __rmul__(self,other):
        x = Point2D(other * self.p1x, other * self.p1y)
        y = Point2D(other * self.p2x, other * self.p2y)
        return Line(x, y)

    def __eq__(self,other):
        try:
            if self.slope == other.slope and self.intercept == other.intercept:
                return True
            else:
                return False
        except:
            return False


if __name__=='__main__':
    import doctest
    # doctest.testmod()  # OR
    doctest.run_docstring_examples(VendingMachine, globals(), name='LAB2',verbose=True) # replace Fibonacci for the class name you want to test
# object oriented programming part3
# created the class Fraction that takes the value of the numerator and denominator,
# and supports all arithmetic operations returning the result as a fraction object.

class Fraction:

    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator

    def trial(self):
        self.n = 1
        self.d = 1

        return Fraction(self.n,self.d)

    def __str__(self):
        return f'{self.n}/{self.d}'

    __repr__ = __str__

    def __add__(self, other):
        n = self.n*other.d + self.d*other.n
        d = self.d*other.d
        return Fraction(n,d)



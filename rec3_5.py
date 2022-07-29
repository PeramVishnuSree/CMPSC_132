class Complex:

    """
        >>> a = Complex(5, -6)
        >>> b = Complex(2, 14)
        >>> a * b
        94 + 58i
        >>> b * 5
        10 + 70i
        >>> 5 * b
        10 + 70i
        >>> isinstance(5 * b, Complex)
        True
        >>> a.conjugate()
        5 + 6i
        >>> b.conjugate()
        2 - 14i
    """
    def __init__(self, r, i):
        self._real = r
        self._imag = i

    def __str__(self):
        """Display complex number"""
        if self._imag >= 0:
            return f"{self._real} + {abs(self._imag)}i"
        else:
            return f"{self._real} - {abs(self._imag)}i"

    __repr__ = __str__

    def conjugate(self):
        """Returns a Complex object that represents the complex conjugate"""
        if self._imag >= 0:
            return Complex(self._real, -1*self._imag)
        else:
            return Complex(self._real, -1*self._imag)

    def __mul__(self, other):

        if isinstance(other, Complex):
            real = (self._real * other._real) - (self._imag * other._imag)
            imag = (self._real * other._imag) + (self._imag * other._real)
            ans = Complex(real, imag)
        else:
            real = self._real*other
            imag = self._imag*other
            ans = Complex(real,imag)
        return ans

    def __rmul__(self, other):
        real = self._real * other
        imag = self._imag * other
        ans = Complex(real, imag)
        return ans

class Real(Complex):

    def __init__(self, value):
        super().__init__(value, 0)

    def __mul__(self,other):
        if isinstance(other, Real):
            return Real(self._real*other._real)
        elif isinstance(other, int):
            return Real(self._real*other)
        elif isinstance(other,float):
            return Real(self._real*other)
        else:
            return Complex(self._real*other._real,self._real*other._imag)

    def __rmul__(self,other):
        if isinstance(other, Real):
            return Real(self._real*other._real)
        elif isinstance(other, int):
            return Real(self._real*other)
        elif isinstance(other,float):
            return Real(self._real*other)

    def __eq__(self,other):
        try:
            if self._imag == other._imag and float(self._real) == float(other._real):
                return True
            return False

        except:
            return False

    def __int__(self):
        return int(self._real)

    def __float__(self):
        return float(self._real)

# if __name__=='__main__':
#     import doctest
#     # doctest.testmod()  # OR
#     doctest.run_docstring_examples(Complex, globals(), name='rec03',verbose=True)
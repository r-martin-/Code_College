__author__ = 'mark'
# simple Rational number class
# assumes both gcd and lcm are already imported

# import sys
#sys.path.append( "/home/mark/Dropbox-Work/Projects-Geany/" )

#from frac import gcd, lcm

def gcd(a, b):
    # Ensure that a > b, if it is not reverse a & b
    if not a > b:
        a, b = b, a

    print("Initial fraction is {}/{}".format(a, b))
    while b != 0:
        rem = a % b
        a, b = b, rem
        print(("... {}/{}".format(a, b)))

    print("GCD is {}".format(a))
    return a


def lcm(a, b):
    print("LCM is {}".format(a * b // gcd(a, b)))
    return (a * b // gcd(a, b))


class Rational(object):
    """ Implements a Rational number"""

    def __init__(self, numer, denom=1):  # note the default for "denom"
        print('in constructor')  # a "print" for illustration
        self.numer = numer
        self.denom = denom

    def __str__(self):
        """ String representation for printing"""
        print('in str')
        return str(self.numer) + '/' + str(self.denom)  # print as a fraction

    def __repr__(self):
        """ Representation of Rational number"""
        print('in repr')
        return self.__str__()

    def __add__(self, f):
        """ Add two Rationals"""
        print('in add')
        if type(f) == int:  # convert ints to Rationals
            f = Rational(f)
        if type(f) == Rational:
            # find a common denominator (lcm)
            theLcm = lcm(self.denom, f.denom)
            # multiply to make denominators the same, then add numerators
            theSum = (theLcm / self.denom * self.numer) + \
                     (theLcm / f.denom * f.numer)
            return Rational(theSum, theLcm)
        else:
            print('wrong type')  # problem: some type we cannot handle
            raise (TypeError)

    def __radd__(self, f):
        """ Add two Rationals (reversed)"""
        # mapping is reversed: if "1 + x", x maps to self, and 1 maps to f
        print("in radd")
        # mapping is already reversed so self will be Rational; call __add__
        return self.__add__(f)

    def __iadd__(self, i):
        '''Increment'''
        print("in iadd")
        return self.__add__(i)

    def __sub__(self, f):
        """ Subtract two Rationals"""
        print('in sub')
        # subtraction is the same as addition with "+" changed to "-"
        theLcm = lcm(self.denom, f.denom)
        numeratorDiff = (theLcm / self.denom * self.numer) - \
                        (theLcm / f.denom * f.numer)
        return Rational(numeratorDiff, theLcm)

    def reduceRational(self):
        """ Return the reduced fractional value."""
        print('in reduce')
        # find the gcd and then divide numerator and denominator by gcd
        thegcd = gcd(self.numer, self.denom)
        return Rational(self.numer / thegcd, self.denom / thegcd)

    def __eq__(self, f):
        """ Compare two Rationals for equality"""
        print('in eq')
        # reduce both; then check that numerators and denominators are equal
        f1 = self.reduceRational()
        f2 = f.reduceRational()
        return f1.numer == f2.numer and f1.denom == f2.denom



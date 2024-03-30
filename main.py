from math import gcd
from copy import copy
class Rational:
    def __init__(self, n, d=None):
        if isinstance(n, Rational):
            self._n = copy(n._n)
            self._d = copy(n._d)
        else:
            try:
                if type(n) is str:
                    ls = n.split('/')
                    self._n = int(ls[0])
                    self._d = int(ls[1])
                else:
                    assert type(n) is int and type(d) is int
                    self._n = n
                    self._d = d
            except:
                print("IncorrectData")
            dd = gcd(self._n, self._d)
            self._n = self._n // dd
            self._d = self._d // dd
            if (self._n < 0 and self._d < 0) or (self._n > 0 and self._d < 0):
                self._n *= -1
                self._d *= -1
    def __str__(self):
        return f"{self._n}/{self._d}"
    def __call__(self):
        return self._n / self._d
    def __getitem__(self, item):
        if item == "n":
            return self._n
        elif item == "d":
            return self._d
        else:
            assert 0 == 1, "Incorrect item"
    def __setitem__(self, item, val):
        assert type(val) is int
        if item == "n":
            self._n = copy(val)
        elif item == "d":
            self._d = copy(val)
        else:
            assert 0 == 1, "Incorrect item"
    def __add__(self, other):
        if type(other) is int:
            return self + Rational(other, 1)
        else:
            w = Rational(self['n'] * other['d'] + other['n'] * self['d'], self['d'] * other['d'])
            return w
    def __radd__(self, other):
        return self + other
    def __sub__(self, other):
        if type(other) is int:
            return self + Rational(other, 1)
        else:
            w = Rational(self['n'] * other['d'] - other['n'] * self['d'], self['d'] * other['d'])
            return w
    def __rsub__(self, other):
        return self - other
    def __mul__(self, other):
        if type(other) is int:
            return self * Rational(other, 1)
        else:
            w = Rational(self['n'] * other['n'], self['d'] * other['d'])
            return w
    def __rmul__(self, other):
        return self * other
if __name__ == "__main__":
    f = open("input01.txt", "rt")
    for line in f.readlines():
        line = line.strip()
        ls = line.split(' ')
        ls=ls[0::2]
        nls = []
        #print(ls)
        for t in range(len(ls)):
            if '/' in ls[t]:
                ls[t] = Rational(ls[t])
            elif ls[t] in '+*-':
                continue
            else:
                ls[t] = int(ls[t])
        for t in range(len(ls)):
            if ls[t] == '*':
                ls[t] = nls[-1] * ls[t + 1]
                ls[t - 1] = 'q'
                ls[t + 1] = 'q'
                nls[-1] = ls[t]
            elif ls[t] == 'q':
                continue
            else:
                nls.append(ls[t])
        res=nls[0]
        for t in range(1, len(nls)-1, 2):
            if nls[t]=='+':
                res=res+nls[t+1]
            elif nls[t]=='-':
                res=res-nls[t+1]
            else:
                continue
        print(res)
    f.close()
    #Ви маєте відповіді щоб я звірився?
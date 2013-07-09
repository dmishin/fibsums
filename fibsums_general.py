#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from sympy import Symbol, binomial, sqrt as sqrts, together

alpha, beta = map(Symbol, "Î±Î²")
alphaval = (1+sqrts(5))/2
betaval = -1/alphaval

abvals = {alpha:alphaval,
          beta:betaval}


Fib = Symbol('F') #Fibonacci function

def powAlpha( n ):
    """Expresses alpha^n via fibonacci numbers"""
    return (1-betaval)*Fib(n) + Fib(n-1)
    #return Fib(n+1) - Fib(n) * betaval

def powBeta( n ):
    """Expresses alpha^n via fibonacci numbers"""
    return (1-alphaval)*Fib(n) + Fib(n-1)
    #return Fib(n+1) - Fib(n) * alphaval

def test_PowAlpha_PowBeta():
    n=Symbol('n')
    f =  (powAlpha(n)-powBeta(n)) / sqrts(5)
    assert f.simplify() == Fib(n)

def sumGeomAB( pow_a, pow_b, pow_m1, n, viaPowers=True):
    """Sum of geometrical progression with ratio:
    alpha^pow_a * beta^pow_b * (-1)^pow_m1
    """
    #print ("Sum of", alpha**pow_a + beta**pow_b * (-1) ** pow_m1)
    if pow_a>0 and pow_b>0:
        #Use the fact that alpha*beta = -1
        dp = min(pow_a, pow_b)
        return sumGeomAB( pow_a - dp, pow_b-dp, pow_m1 + dp, n, viaPowers )
    
    if pow_a == 0 and pow_b == 0 and pow_m1 % 2 == 0:
        #Special case:
        # Sum 1
        return n+1
    else:
        #General case
        #r = alpha **pow_a * beta **pow_b ** (-1)**pow_m1
        if viaPowers:
            numer = powAlpha(n+1)**pow_a * \
                    powBeta(n+1)**pow_b * \
                    ((-1)**pow_m1)**(n+1) - 1
        else:
            numer = (powAlpha((n+1)*pow_a)  if pow_a !=0 else 1)* \
                    (powBeta((n+1)*pow_b)   if pow_b !=0 else 1)* \
                    ((-1)**pow_m1)**(n+1) - 1

        denom = alphaval**pow_a * betaval**pow_b * (-1)**pow_m1 - 1

        return numer / denom

def sumFibPower(n, p, viaPowers = True):
    """Sum Fib(i)^p, i = 0..n"""
    #Expand power, sum each element, then convert to fibonacci numbers
    s = 0
    for i in range(0, p+1):
        si = sumGeomAB( p-i, i, 0, n, viaPowers=viaPowers )
        s = s + binomial(p,i) * (-1)**(i) * si
    return s / (sqrts(5))**p



def showAnswer(p):
    n = Symbol('n')
    sp = together(sumFibPower(n, p, viaPowers=True).expand().simplify())
    sn = together(sumFibPower(n, p, viaPowers=False).expand().simplify())

    print ("Sum F(i)^%d = "%(p))
    print ("=",sp,"=")
    print ("=",sn)


USAGE="""python fibsums_general.py N
python fibsums_general.py N0 N1

Calculate symbolic expression for the sum of Fibonacci powers:

  Sum F(i)^N  for i = 0..n

where F(i) is i'th Fibonacci's number. Result is again expressed via Fibonacci's numbers.
If two arguments are given, calculates formulas for range of powers
"""

if __name__=="__main__":
    import sys
    argc = len(sys.argv)
    if argc <= 1:
        print (USAGE)
        exit()
    else:
        try:
            if argc == 2:
                n0 = n1 = int(sys.argv[1])
            elif argc == 3:
                n0, n1 = map(int, sys.argv[1:3])
            else:
                raise ValueError("too many arguments")
            if n1 < n0: raise ValueError("N1 < N0")
            if n0 < 1:  raise ValueError("N0 < 1")
        except Exception as err:
            print ("Error: %s"%err)
            exit(1)
            
    for p in range(n0,n1+1):
        print ("==================================")
        showAnswer(p)
        

from sympy import Symbol, binomial, sqrt as sqrts, latex, together

alpha, beta = map(Symbol, "αβ")
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


import re


def cleanlatex(s):
    s = s.replace(r"\operatorname{F}", "f")

    #\operatorname{F}^{2}{\left (n \right )}
    #f^{2}{\left (n \right )}

    fp_re = re.compile( r"f(\^\{(\d+)\})?\{([^\}]+)\}" )
    def enclose(s):
        if len(s) == 1:
            return s
        else:
            return "{"+s+"}"
    def do_sub(m):
        pow = m.group(2)
        arg = m.group(3)
        arg = arg.replace("\\left", "")
        arg = arg.replace("\\right", "")
        arg = arg.strip()
        if arg[0] == "(" and arg[-1] == ")":
            arg = arg[1:-1].strip()

        rval = "f_" + enclose(arg)
        if pow:
            rval = rval + "^" + enclose(pow)
        return rval

    s = fp_re.sub(do_sub, s)
    s = s.replace( r"\left(-1\right)", "(-1)")
    s = s.replace( "{n}", "n" )
    #s = s.replace( " + ", "+" )
    #s = s.replace( " - ", "-" )
    return s

def showAnswer(p):
    n = Symbol('n')
    sp = together(sumFibPower(n, p, viaPowers=True).simplify())
    sn = together(sumFibPower(n, p, viaPowers=False).simplify())

    print ("Sum Fib(i)^%d = "%(p))
    print (sp)
    print (sn)
    print ("Or in LaTeX form:")
    print ("")
    print (cleanlatex(latex(sp)))
    print ("")
    print (cleanlatex(latex(sn)))



if __name__=="__main__":
#if False and __name__=="__main__":
    for p in range(1,12):
        print ("==================================")
        showAnswer(p)

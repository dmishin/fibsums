#Testing formulas for fibsums
#from numtheor import fibonacci as F
#kopipe from numtheor.py
def fibonacci(n, zero=0, one=1):
    "Fast, matrix-power based fibbonacci number calculator"
    M=[one, one, one, zero]
    def mul( m1, m2):
        x11, x12, x21, x22 = m1
        y11, y12, y21, y22 = m2
        return [ x11*y11+x12*y21, x11*y12+x12*y22,
                 x21*y11+x22*y21, x21*y12+x22*y22]
    def mpow(m, n):
        if n < 1: raise ValueError("not supported n<1")
        if n == 1: return m
        mp = mpow(m, n // 2)
        mp2 = mul(mp, mp)
        if n % 2 == 0:
            return mp2
        else:
            return mul(mp2, m)
        
    if n == 0: return 0
    elif n < 0: 
        fp = fibonacci(-n, zero=zero, one=one)
        if n % 2 == 1:
            return fp
        else:
            return -fp
    else:
        mn = mpow(M, n)
        return mn[1]

F = fibonacci

def fibsums(p):
    s = 0
    i = 0
    while True:
        s += F(i)**p
        i += 1
        yield s


def test_fibsum( p, formula ):
    n = 100
    for i, fs in zip(range(n), fibsums(p)):
        try:
            fs_t = formula(i)
            if fs != fs_t:
                print ("Error: n=%d, i=%d, expected:%d, got:%d"%(p, i, fs, fs_t))
                return
        except ValueError as err:
            print ("Warning: computation failed for n=%d :%s"%(i, err))
    print ("Test OK for n=%d"%(p))

if __name__=="__main__":
    print ("Testing formulas for fibsums. Edit code to add new tests.")
    test_fibsum( 2, lambda n:
                     F(n)*F(n+1) )
    test_fibsum( 2, lambda n:
                     (F(2*n) + F(2*n+2) - (-1)**n)//5 )
    
    
    #\frac{f_n^3 + 3 f_n f_{n + 1}^2 + f_{n + 1}^3 + 6(-1)^n f_{n-1} + 5} {10}
    test_fibsum( 3, lambda n:
                     (F(n)**3 + 3*F(n)*F(n + 1)**2 + 
                      F(n + 1)**3 - 6*(-1)**n* F(n-1) + 5)//10 )

    test_fibsum( 3, lambda n:
                     (F(3*n + 2) - 6*(-1)**n * F(n-1) + 5) // 10 )


    test_fibsum( 4, lambda n:
                     (F(n+1)**4 - F(n)**4  + 4*F(n)**3*F(n+1) + 4*F(n)*F(n+1)**3 - 4*(-1)**n *( F(n)**2 + F(n+1)**2 ) + 6*n + 3)//25 )

    test_fibsum( 4, lambda n:
                     (F(4*n+2) - 4*(-1)**n * F(2*n+1)+6*n+3)//25 )


    
    test_fibsum( 5, lambda n:
                     ( + 2*F(5*n+4) 
                       + 4*F(5*n+2) 
                       - 55* (-1)**n* F(3*n+1) 
                       + 220* F(n+2) - 175)//(550) )

    
    test_fibsum( 5, lambda n:
                     (2* F(n+1)**5 + 2* F(n)**5 + 11* (-1)**n* ( F(n)**3 - 3*F(n)**2* F(n+1) - F(n+1)**3 ) - 4* F(n)**4* F(n+1) + 12* F(n)**3* F(n+1)**2 + 4* F(n)**2* F(n+1)**3 + 8* F(n)* F(n+1)**4 + 44* F(n+2) - 35)//(110) )


    test_fibsum( 6, lambda n:
                     (     F(6*n + 4)
                        +  F(6*n + 2)
                        -8* (-1)**n* ( F(4* n + 3) + F(4* n + 1) + 5 )
                        + 60* (F(2* n + 2) + F(2* n )  )
                        ) // 500 )

    test_fibsum( 7, lambda n:
                     (
              - 406*(-1)**n*( F(5*n + 1) +2*F(5*n + 3) + 55*F(n - 1))
              + 6699*F(3*n + 2) 
              + 22* (4*F(7*n + 4) + F(7*n + 2)  )
              + 17375)//79750 )

    test_fibsum( 8, lambda n:
                 (
                     + F(8*n + 4) 
                     -12*(-1)**n* (F(6*n + 3)  + 14*F(2*n + 1) )
                     + 84*F(4*n + 2) 
                     + 210*n 
                     + 105
                 )//1875 )
    test_fibsum( 9, lambda n:
                 (
                     - 509124*(-1)**n*F(3*n + 1) 
                     - 3762*(-1)**n*F(7*n + 4) 
                     - 18810*(-1)**n*F(7*n + 3) 
                     + 1527372*F(n + 2) 
                     + 39672*F(5*n + 3) 
                     + 119016*F(5*n + 2) 
                     + 319*F(9*n + 5) 
                     + 1276*F(9*n + 4) 
                     - 1173125
                 )//7576250 )

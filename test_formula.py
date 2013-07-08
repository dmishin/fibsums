#Testing formulas for fibsums


from numtheor import fibonacci as fib

def listify(gen):
    def listified(*args, **kwargs):
        return list(gen(*args, **kwargs))
    return listified

@listify
def fibsums(n, p):
    s = 0
    for i in range(n):
        s += fib(i)**p
        yield s


def test_fibsum( p, formula ):
    n = 100
    for i, fs in enumerate(fibsums(n, p)):
        try:
            fs_t = formula(i)
            if fs != fs_t:
                print ("Error: n=%d, i=%d, expected:%d, got:%d"%(p, i, fs, fs_t))
                return
        except ValueError as err:
            pass
            #print ("Warning: computation failed for n=%d :%s"%(i, err))
    print ("Test OK for n=%d"%(p))

import re


if __name__=="__main__":
    #print (list(map(lambda n: fib(n)*fib(n+1), range(15))))
    #print (fibsums(15, 2))

    test_fibsum( 2, lambda n:
                     fib(n)*fib(n+1) )
    test_fibsum( 2, lambda n:
                     (fib(2*n) + fib(2*n+2) - (-1)**n)//5 )
    
    
    #\frac{f_n^3 + 3 f_n f_{n + 1}^2 + f_{n + 1}^3 + 6(-1)^n f_{n-1} + 5} {10}
    test_fibsum( 3, lambda n:
                     (fib(n)**3 + 3*fib(n)*fib(n + 1)**2 + 
                      fib(n + 1)**3 - 6*(-1)**n* fib(n-1) + 5)//10 )

    test_fibsum( 3, lambda n:
                     (fib(3*n + 2) - 6*(-1)**n * fib(n-1) + 5) // 10 )


    test_fibsum( 4, lambda n:
                     (fib(n+1)**4 - fib(n)**4  + 4*fib(n)**3*fib(n+1) + 4*fib(n)*fib(n+1)**3 - 4*(-1)**n *( fib(n)**2 + fib(n+1)**2 ) + 6*n + 3)//25 )

    test_fibsum( 4, lambda n:
                     (fib(4*n+2) - 4*(-1)**n * fib(2*n+1)+6*n+3)//25 )


    
    test_fibsum( 5, lambda n:
                     ( + 2*fib(5*n+4) 
                       + 4*fib(5*n+2) 
                       - 55* (-1)**n* fib(3*n+1) 
                       + 220* fib(n+2) - 175)//(550) )

    
    test_fibsum( 5, lambda n:
                     (2* fib(n+1)**5 + 2* fib(n)**5 + 11* (-1)**n* ( fib(n)**3 - 3*fib(n)**2* fib(n+1) - fib(n+1)**3 ) - 4* fib(n)**4* fib(n+1) + 12* fib(n)**3* fib(n+1)**2 + 4* fib(n)**2* fib(n+1)**3 + 8* fib(n)* fib(n+1)**4 + 44* fib(n+2) - 35)//(110) )


    test_fibsum( 6, lambda n:
                     (     fib(6*n + 4)
                        +  fib(6*n + 2)
                        -8* (-1)**n* ( fib(4* n + 3) + fib(4* n + 1) + 5 )
                        + 60* (fib(2* n + 2) + fib(2* n )  )
                        ) // 500 )

    test_fibsum( 7, lambda n:
                     (
              - 406*(-1)**n*( fib(5*n + 1) +2*fib(5*n + 3) + 55*fib(n - 1))
              + 6699*fib(3*n + 2) 
              + 22* (4*fib(7*n + 4) + fib(7*n + 2)  )
              + 17375)//79750 )

    test_fibsum( 8, lambda n:
                 (
                     + fib(8*n + 4) 
                     -12*(-1)**n* (fib(6*n + 3)  + 14*fib(2*n + 1) )
                     + 84*fib(4*n + 2) 
                     + 210*n 
                     + 105
                 )//1875 )
    test_fibsum( 9, lambda n:
                 (
                     - 509124*(-1)**n*fib(3*n + 1) 
                     - 3762*(-1)**n*fib(7*n + 4) 
                     - 18810*(-1)**n*fib(7*n + 3) 
                     + 1527372*fib(n + 2) 
                     + 39672*fib(5*n + 3) 
                     + 119016*fib(5*n + 2) 
                     + 319*fib(9*n + 5) 
                     + 1276*fib(9*n + 4) 
                     - 1173125
                 )//7576250 )

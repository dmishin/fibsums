print ("Enter a, b, nmax")
a0, b0, nmax = map(int, input().split(" "))


def yielder(a0, b0):
    a,b = a0,b0
    i =0 
    for _ in range(15):
        yield (i, a, b)
        a, b = b+a, a
        i += 1


    a,b = a0,b0
    i =0 
    for _ in range(15):
        yield (i, a, b)
        a, b = b, a-b
        i -= 1

def keyfunc( iab ):
    i,a,b = iab
    return abs(a)+abs(b)+(0.1 if a < 0 else 0)  + (0.1 if b < 0 else 0)
di, a1, b1 = min(yielder(a0, b0), key = keyfunc)

print ("%dF(n+%d) + %dF(n+%d) ="%(a0, nmax, b0, nmax-1) )
print ("    %dF(n+%d) + %dF(n+%d)"%(a1, nmax-di, b1, nmax-1-di) )

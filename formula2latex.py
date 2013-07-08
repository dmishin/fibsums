from sympy import Symbol, latex, together
import re
from fibsums_general import cleanlatex


def inputlines():
    lines = []
    while True:
        l = input().strip()
        if not l:
            break
        lines.append(l)
    return "".join(lines)

if __name__=="__main__":

    formula = inputlines()
    formula = formula.replace("//","/")
    F = Symbol("F")
    n = Symbol("n")

    f = eval( formula, {"fib": lambda x: F(x), 
                        "n": n } )
    f = together(f)
    #print (f)
    print (cleanlatex(latex(f)))

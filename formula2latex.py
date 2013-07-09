#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from sympy import Symbol, latex, together
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

def inputlines():
    lines = []
    while True:
        l = input()
        if not l: break
        lines.append(l)
    return "".join(lines)


USAGE = """Convert formula, written in Python notation, into LaTeX form.
Replaces occurences of F(<arg>)**n with f_{<arg>}^n.

Enter formula, followed by an empty line:
"""

if __name__=="__main__":
    print (USAGE)
    formula = inputlines()
    formula = formula.replace("//","/")
    F = Symbol("F")
    n = Symbol("n")

    f = eval( formula, {"F": lambda x: F(x), 
                        "n": n } )
    f = together(f)
    #print (f)
    print (cleanlatex(latex(f)))

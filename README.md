FIBSUMS
=======

Collection of Python scripts, dedicated to symbolic computation of sums of powers of Fibonacci numbers:

![equation](http://chart.apis.google.com/chart?cht=tx&chl=\displaystyle{SF%28n,p%29=\sum_{i=0}^nf_i^p} )

Sum( fib(i)^p for i in [0 .. n] )

fibsums_general.py
------------------

Derives formula for sums of Fibonacci powers. Formula is written in Python notation. Run without arguments to see usage details.

Example:
Derivation of formula for p=1:

    $python fibsums_general.py 1
    Sum F(i)^1 =
    = F(n) + F(n + 1) - 1 =
    = F(n) + F(n + 1) - 1

With some simplification by hand, it gives well-known formula: Sum F(i) = F(n+2)-1.

formula2latex.py
----------------

Converts formula, containing F(i)**n into LaTeX notation. Formula is read from stdin, empty line terminates.


test_formula.py
---------------

Set of tests of formulas, derived by author. Edit code to add new tests.

fibpair.py
----------

Simplifies expression of form:

 A*F(x+N) + B*F(x+N-1)

where A, B, N are integers. Run script and enter A B N, separated by spaces.

REQUIREMENTS
============

Python3 and Sympy are required. 

INSTALLATION
============
Not intended for installation.
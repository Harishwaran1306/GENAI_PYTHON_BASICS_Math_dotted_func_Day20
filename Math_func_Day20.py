Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import math
#Math functions

#PART 1 — NUMBER THEORY
#math.factorial()
math.factorial(7)
5040
#7! = 7 * 6 * 5 * 3 * 2 * 1 --> 5040

#math.comb()
math.comb(6,4)
15

n = 5
k = 3
math.comb(n,k)
10

#math.perm()
# n: total items (must be non-negative integer)
# k: items chosen (optional; defaults to n, which returns n!)

math.perm(8,3)
336

n=9
k=5
math.perm(n,k)
15120

#math.gcd()
math.gcd(54,12)
6

#math.lcm()
math.lcm(54,12)
108
math.lcm(9,6)
18

#math.isqrt()
#isqrt = Integer Square Root.
math.isqrt(81)
9
math.isqrt(72)
8


#PART 2 — FLOATING POINT FUNCTIONS
#math.ceil()
#Rounds toward positive infinity.

math.ceil(8.2)
9
math.ceil(-8.2)
-8
math.ceil(0.02)
1
math.ceil(3.0)
3

#math.floor()
#Rounds toward negative infinity.

math.floor(8.2)
8
math.floor(-8.2)
-9
math.floor(0.02)
0
math.floor(3.1)
3

#math.fabs()
#Absolute value returned as a float.

math.fabs(-36)
36.0
math.fabs(45)
45.0

#math.trunc()
#Removes the fractional part/ Decimal part toward zero.

math.trunc(7.89)
7
math.trunc(-7.89)
-7
math.floor(-7.89)
-8
math.floor(7.89)
7
#trunc() and floor() will looks like similar but floor() moves towards negative infinity and trunc()turns Decimal part toward zero.

#math.fmod()
#Floating-point remainder using the C-style fmod rule.

math.fmod(7,3)
1.0
math.fmod(8,3)
2.0
math.fmod(7.5,2)
1.5

#math.modf()
#Splits a number into fractional and integer parts.

math.modf(8.85)
(0.8499999999999996, 8.0)
math.modf(-5.5)
(-0.5, -5.0)

#math.remainder()
#IEEE-style remainder; differs from ordinary % in some cases.

math.remainder(7,2)
-1.0
#Regular division: 7 / 2 = 3.5 (halfway tie -> rounds to even integer 4)
#remainder r = x - n X y, (7 - 4X2)=-1.0 (x-7, n-4, y-2)

#math.fma()
#Fused multiply-add: computes x*y+z with a single final rounding step.

math.fma(5,4,3)
23.0
#((5*4)+3))


#PART 3 — FLOATING-POINT MANIPULATION
#math.isclose()
#Checks whether two floating-point values are approximately equal

math.isclose(7.499996,7.5)
False
math.isclose(10.0,10.000001)
False
math.isclose(7.499996, 7.5, abs_tol=1e-5)
True
math.isclose(10.0, 10.000001, abs_tol=1e-5)
True
math.isclose(7.499996, 7.5, rel_tol=1e-5)
True

#math.isfinite()
#Checks whether a number is finite.

math.isfinite(25)
True
math.isfinite(3.14)
True
math.isfinite(-3.14)
True

#math.isinf()
#Checks whether a number is positive or negative infinity.

math.isinf(math.inf)
True
math.isinf(-math.inf)
True
math.isinf(1e309)
True
math.isinf(0)
False
math.isinf(math.nan)
False

#math.isinf(math.nan)
#Checks whether a value is NaN (Not a Number).

#math.isnan()
#Checks whether a value is NaN (Not a Number).

x = math.nan
math.isnan(x)
True

math.isnan(100.0)
False


#math.copysign()
#Applies the sign of one value to the magnitude of another.

math.copysign(-7,3)
7.0
# Takes magnitude of -7.0 and sign of 3.0 (+)

#math.frexp()
#Splits a float into mantissa and exponent.
>>> #Breaks a float x into its normalized fraction (mantissa) m and exponent e
>>> 
>>> math.frexp(9)
(0.5625, 4)
>>> math.frexp(87)
(0.6796875, 7)
>>> 
>>> #math.ldexp()
>>> #Builds a float from mantissa and a power of two.
>>> 
>>> math.ldexp(0.5625, 4)
9.0
>>> 
>>> #math.nextafter()
>>> #Moves to the next representable floating-point value toward a target.
>>> 
>>> math.nextafter(1.0, 2.0)
1.0000000000000002
>>> math.nextafter(5.3,4.5)
5.299999999999999
>>> 
>>> #math.ulp()
>>> #Measures the spacing of floating-point values at a given number.
>>> 
>>> math.ulp(85)
1.4210854715202004e-14
>>> math.ulp(80000)
1.4551915228366852e-11
>>> math.ulp(1.0)
2.220446049250313e-16

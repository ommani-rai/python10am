'''
operator:
symbol which perfom specific task 
types:
1. arithmetic operator
2. assignment operator
3. logical operator
4. comparision operator
5. membership operator
6. bitwise operator
7. identity operator

'''
# arithmetic operator
# +, -, *, /, % , **(exponential operator), //(floor division operator)

a = 14
b = 4
sum = a + b
expo = a ** b
div = a/b
floor = a // b
# print(sum)
print(expo)
print(div)
print(floor)
print(type(a))
# logical operator
# and or not
'''
# and
a   b  ( a and b)
T   T   T
T   F   F
F   T   F
F   F   F


# OR
a   b   (a or b)
T   T   T
T   F   T
F   T   T
F   F   F

# NOT
a   (not a)
T   F
F   T

if(condition):
    // truth statement

condition:
truth value: true, 
falsy value:false,0, ""

'''
if True:
    print("here is 1")

if a > 12 and b < 12:
    print("true")

if a < 12 or b < 12: # F or T => reult: T
    print('true')

if not(a<12): # not(F) => T
    print("not operator")
'''
num = lambda x, y, z: x + 10 + y + z
# print(num(12, 12,12))
print(type(num))

'''
# num = lambda x, y, z: x + 7 + y - z
# print(num(5, 8, 15))
# print(type(num))

'''
def mul(num):
    return lambda x, y, z: x * num * y * z

res = mul(5)
# print(type(res))
print(res(10, 2,3))

def lal(num):
    return lambda x, y, z, : x * num * y * num * z 
res = lal(2)
print(res(12, 21, 2))

'''
num = int(input("enter a number to get three times the  number you entered \n"))
def hah(num):
    return lambda x : x * num
res = hah(num)
print(res(3))

num = int(input("Enter a number you want to divide by two \n"))
def lol(num):
    return lambda x : num / x
res = lol(num)
print(res(2))
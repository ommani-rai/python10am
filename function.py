# function welcome(){

# }

def welcome():
    print("welcome")

# welcome()


#function return value passing no arguemenets
'''
def sum():
    n1 = 12
    n2 = 34
    sums = n1 + n2
    # print(sums)
    return sums

a = sum()
print(a)
'''
#function return no value and passsing arguements
'''
def sum(n1, n2):

    sums = n1 + n2
    # print(sums)
    return sums

a = sum(n1 = 10, n2 = 20)
print(a)
'''
#function return no value and passing no arguements


# arbitary argument(*args)
def child(*childs):
    firstChild = childs[0]
    print(type(firstChild))


# child("1",2,3,4)


# keyword argument
def welcome(name, address):
    print("welcome " + name + " to " + address)

# welcome( address="vedu",name = 'ram')

# default argument

def country(con="Space"):
    print("i am from ", con)

country("Nepal")
country("USA")
country("China")
country()
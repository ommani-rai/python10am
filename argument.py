'''
arbitrary argument
default argument

kwargs argument



'''

def welcome(**kwargs):
    print('first argument is: ', kwargs['first'])

welcome(first='html', second='css', third='python', fourth='c')

def hello(**kwargs):
    print()


# define
def welcome(*name):
    print("welcome", name[1])

welcome("ram", "shyam")
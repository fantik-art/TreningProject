print('hello GIT!')

name = input('What your name? ')

print(f'My name is {name}')

print(f'this wery cool!')

def main(name):
    new = list(filter(lambda x: x =='a', name))
    return new

xxx = main(['a', 'k'])
print(xxx)
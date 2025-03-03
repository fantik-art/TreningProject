print('hello GIT!')

name = input('What your name? ')

print('trening Brunch')

f = 'Cool' if name=='artem' else 'back'
print(f)
xx = ['qwe','sdasda']
z = list(map(lambda x: x.upper(), xx))

print(z)

print(f'this wery cool!')

def main(name):
    new = list(filter(lambda x: x =='a', name))
    return new

xxx = main(['a', 'k'])
print(xxx)

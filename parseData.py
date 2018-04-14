file = open('out', 'r').read().split('\n')[:-1]

out = open('X', 'w')

w = []
i = 1
x = ''
for line in file:
    genres = line.split(',')[-1]
    x = str(i) + ', ' + genres
    i += 1
    out.write(x + '\n')

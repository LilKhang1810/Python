from kanren import run, fact, eq, Relation, var
adjacent = Relation()
coastal = Relation()

file_coastal = 'coastal_states.txt'
file_adjacent = 'adjacent_states.txt'

with open(file_coastal, 'r') as f:
    line = f.read()
    coastal_states = line.split(',')

for state in coastal_states:
  fact(coastal, state)

with open(file_adjacent,'r') as f:
  adjlist = [line.strip().split(',') for line in f if line and line[0].isalpha()]

for L in adjlist:
  head, tail = L[0], L[1:]
  for state in tail:
    fact(adjacent,head,state)

x = var()
y = var()

output = run(0, x, adjacent('Nevada','Louisiana'))
print('\nIs Neveda adjacent to Louisiana?:')
print('Yes' if len(output) else 'No')

output = run(0, x, adjacent('Oregon', x))
print('\nList of states adjacent to Oregon:')
for item in output:
  print(item)

output = run(0, x, adjacent('Mississippi', x), coastal(x))
print('\nList of states adjacent to Mississippi:')
for item in output:
  print(item)

n = 7
output = run(n, x, coastal(y),adjacent(x,y))
print('\nList of'+str(n) + 'states that border a coastal state:')
for item in output:
  print(item)

output = run(0, x, adjacent('Arkansas',x),adjacent('Kentucky',x))
print('\nList of states that are adjacent to Arkansas and Kentucky:')
for item in output:
  print(item)


import json

file = 'teste2.json'

with open(file, 'r') as arquivo:
    base = json.load(arquivo)

print(base)
base.append('Olá mundo')

with open(file, 'w') as dados:
    json.dump(base, dados)


import random

# Lista dos animais e seu som correspondente.
animais = ['Tigre', 'Leão', 'Cobra', 'Pássaro']
sons = ['Rawr', 'Groar', 'Ssss', 'Chirp']

# Randomizar a lista dos sons.
random = random.sample(sons, 4)
print(random)

# Iterar vários testes do som correspondente ao animal.
for c in range(0, 4) :
    if random[c] == sons[0]:
        print(animais[0])
    elif random[c] == sons[1]:
        print(animais[1])
    elif random[c] == sons[2]:
        print(animais[2])
    else:
        print(animais[3])

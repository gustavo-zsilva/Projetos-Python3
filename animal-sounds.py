import random

animais = ['Tigre', 'Leão', 'Cobra', 'Pássaro']
sons = ['Rawr', 'Groar', 'Ssss', 'Chirp']

random = random.sample(sons, 4)
print(random)

for c in range(0, 4) :
    if random[c] == sons[0]:
        print(animais[0])
    elif random[c] == sons[1]:
        print(animais[1])
    elif random[c] == sons[2]:
        print(animais[2])
    else:
        print(animais[3])





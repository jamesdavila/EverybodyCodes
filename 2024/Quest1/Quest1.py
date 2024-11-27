def score_monster(monster):
    if monster == 'B':
        return 1
    elif monster == 'C':
        return 3
    elif monster == 'D':
        return 5
    return 0


with open('Quest1_Input1.txt') as file:
    monsters = file.readline()
    potion_count = 0
    for monster in monsters:
        potion_count += score_monster(monster)
    print(f'Potion count for part 1: {potion_count}')

with open('Quest1_Input2.txt') as file:
    monsters = file.readline()
    potion_count = 0
    for i in range(0, len(monsters)-1, 2):
        potion_count += score_monster(monsters[i])
        potion_count += score_monster(monsters[i + 1])
        if monsters[i] != 'x' and monsters[i + 1] != 'x':
            potion_count += 2
    print(f'Potion count for part 2: {potion_count}')

with open('Quest1_Input3.txt') as file:
    monsters = file.readline()
    potion_count = 0
    for i in range(0, len(monsters)-2, 3):
        potion_count += score_monster(monsters[i])
        potion_count += score_monster(monsters[i + 1])
        potion_count += score_monster(monsters[i + 2])
        triplet = monsters[i] + monsters[i + 1] + monsters[i + 2]
        x_count = triplet.count('x')
        if x_count == 1:
            potion_count += 2
        if x_count == 0:
            potion_count += 6
    print(f'Potion count for part 3: {potion_count}')

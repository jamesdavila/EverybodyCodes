def part1():
    with open('Quest2_Input1.txt') as file:
        word_data = file.readline()
        words = [word.strip() for word in word_data.split(':')[1].split(',')]
        _ = file.readline()
        inscription = file.readline().strip()

        runic_words_count = 0
        for i in range(len(inscription)):
            for word in words:
                if inscription[i:].startswith(word):
                    runic_words_count += 1
        print(f'Quest 2 Part 1: {runic_words_count}')


def read_inscription(inscription, words, loopback=False):
    runic_positions = set()

    def add_word_positions(start_pos, word):
        mod = len(inscription)
        if loopback:
            mod = int(mod / 2)
        for i in range(len(word)):
            runic_positions.add((start_pos + i) % mod)

    # support loopback by doubling inscription, will math the start pos later
    if loopback:
        inscription = inscription + inscription
    # forward
    for i in range(len(inscription)):
        for word in words:
            if inscription[i:].startswith(word):
                add_word_positions(i, word)

    # backward
    reverse_inscription = inscription[::-1]
    for i in range(len(reverse_inscription)):
        for word in words:
            if reverse_inscription[i:].startswith(word):
                original_start = len(inscription) - (i + len(word))
                add_word_positions(original_start, word)

    return runic_positions


def part2():
    with open('Quest2_Input2.txt') as file:
        word_data = file.readline()
        words = [word.strip() for word in word_data.split(':')[1].split(',')]
        _ = file.readline()

        symbol_count = 0
        while True:
            line = file.readline()
            if not line:
                break
            inscription_count = read_inscription(line.strip(), words)
            symbol_count += len(inscription_count)
        print(f'Quest 2 Part 2: {symbol_count}')


# TODO the problem is that the right edge is connected to the left but the top is not
# connected to the bottom
def part3():
    with open('Quest2_Input3.txt') as file:
        word_data = file.readline()
        words = [word.strip() for word in word_data.split(':')[1].split(',')]
        _ = sorted(len(word) for word in words)
        _ = file.readline()

        coords = set()
        rows = []
        while True:
            line = file.readline()
            if not line:
                break
            rows.append(line.strip())
        for i in range(len(rows)):
            row_inscriptions = read_inscription(rows[i], words, True)
            for entry in row_inscriptions:
                coords.add((i, entry))
        for i in range(len(rows[0])):
            col = ""
            for j in range(len(rows)):
                col += rows[j][i]
            col_inscriptions = read_inscription(col, words, False)
            for entry in col_inscriptions:
                coords.add((entry, i))
        print(f'Quest 2 Part 3: {len(coords)}')


part1()
part2()
part3()

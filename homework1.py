def word_counter(text_):
    counts = dict()
    for line in text_:
        words = line.split()
        for word_ in words:
            counts[word_] = counts.get(word_, 0) + 1
    return counts


while True:
    file = input('Enter the file name: ')
    try:
        text = open(file)
    except FileNotFoundError:
        print(f'Error - File "{file}" does not exist')
        continue

    word_counts = word_counter(text)
    print(word_counts)

    break

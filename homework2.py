class TextFile:
    def __init__(self, name):
        self.name = name
        self.text = open(self.name)
        self.counts = dict()

    def word_counter(self):
        for line in self.text:
            words = line.split()
            for word in words:
                self.counts[word] = self.counts.get(word, 0) + 1
        return self.counts

    def top_ten_words(self):
        for line in self.text:
            words = line.split()
            for word in words:
                self.counts[word] = self.counts.get(word, 0) + 1
        sort_counts = sorted(self.counts.items(), key=lambda x: x[1], reverse=True)

        i = 0
        while i < 10:
            print(sort_counts[i][0], ":", sort_counts[i][1])
            i = i + 1


while True:
    file_name = input('Enter the file name: ')
    try:
        file = TextFile(file_name)
    except FileNotFoundError:
        print(f'Error - File "{file_name}" does not exist')
        continue

    file.top_ten_words()

    break

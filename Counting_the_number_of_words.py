text = input("Введите строку: ")


words = text.split()

word_counts = {}
for word in words:
    word_lower = word.lower()
    word_counts[word_lower] = word_counts.get(word_lower, 0) + 1

for word, count in word_counts.items():
    print(f"{word}: {count}")
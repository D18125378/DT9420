with open("data\\Dagonet Dittie.txt", "r", encoding="utf-8") as read_file:
    book = read_file.readlines()
    #print(book, "\n")

word_counter = {}

for word in book:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

popular_words = sorted(word_counter, key = word_counter.get, reverse = True)

print (popular_words[:10])

#13. Split a string into words and count the frequency of each word.
def count_word_frequency(input_string):
    words = input_string.split()
    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1

    return word_frequency
print(count_word_frequency('kashish garg deeksha garg'))
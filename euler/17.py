from lib.numbers_to_words import count_letters, number_to_words

print(sum(count_letters(number_to_words(number)) for number in range(1, 1001)))

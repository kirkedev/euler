from lib.numbers_to_words import number_to_words, count_letters


def test_numbers_to_words():
    assert number_to_words(115) == "one hundred and fifteen"
    assert number_to_words(342) == "three hundred and forty-two"
    assert number_to_words(333) == "three hundred and thirty-three"
    assert number_to_words(1000) == "one thousand"
    assert number_to_words(110) == "one hundred and ten"
    assert number_to_words(1010) == "one thousand and ten"
    assert number_to_words(1042) == "one thousand and forty-two"
    assert number_to_words(1111) == "one thousand, one hundred and eleven"
    assert number_to_words(1333) == "one thousand, three hundred and thirty-three"
    assert number_to_words(40) == "forty"
    assert number_to_words(5555) == "five thousand, five hundred and fifty-five"
    assert number_to_words(55555) == "fifty-five thousand, five hundred and fifty-five"
    assert number_to_words(555555) == "five hundred and fifty-five thousand, five hundred and fifty-five"


def test_letter_count():
    assert count_letters(number_to_words(115)) == 20
    assert count_letters(number_to_words(342)) == 23

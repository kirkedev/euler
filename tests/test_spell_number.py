from lib.more_itertools import count_letters
from lib.spell_number import spell_number


def test_numbers_to_words():
    assert spell_number(115) == "one hundred and fifteen"
    assert spell_number(342) == "three hundred and forty-two"
    assert spell_number(333) == "three hundred and thirty-three"
    assert spell_number(1000) == "one thousand"
    assert spell_number(110) == "one hundred and ten"
    assert spell_number(1010) == "one thousand and ten"
    assert spell_number(1042) == "one thousand and forty-two"
    assert spell_number(1111) == "one thousand, one hundred and eleven"
    assert spell_number(1333) == "one thousand, three hundred and thirty-three"
    assert spell_number(40) == "forty"
    assert spell_number(5555) == "five thousand, five hundred and fifty-five"
    assert spell_number(55555) == "fifty-five thousand, five hundred and fifty-five"
    assert spell_number(555555) == "five hundred and fifty-five thousand, five hundred and fifty-five"


def test_letter_count():
    assert count_letters(spell_number(115)) == 20
    assert count_letters(spell_number(342)) == 23

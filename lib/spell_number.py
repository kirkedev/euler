words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}


def spell_number(number: int) -> str:
    if 1 <= number < 20:
        return words[number]
    elif 20 <= number < 100:
        tens = words[number // 10 * 10]
        remainder = number % 10
        return tens if remainder == 0 else f"{tens}-{words[remainder]}"
    elif 100 <= number < 1000:
        hundreds = f"{words[number // 100]} {words[100]}"
        remainder = number % 100
        return hundreds if remainder == 0 else f"{hundreds} and {spell_number(remainder)}"
    elif 1000 <= number < 1_000_000:
        thousands = f"{spell_number(number // 1000)} {words[1000]}"
        remainder = number % 1000
        separator = " and " if remainder // 100 == 0 else ", "
        return thousands if remainder == 0 else f"{thousands}{separator}{spell_number(remainder)}"
    else:
        raise ValueError(f"{number} must be less than 1,000,000")

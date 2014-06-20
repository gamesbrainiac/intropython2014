# encoding=utf-8
# Created by quazinafiulislam


def is_vowel_or_consonant(wrd):
    def is_vowel(_check):
        a, *end = _check
        return a.upper() in 'AEIOU'

    if is_vowel(wrd):
        print(wrd, "is a vowel")
    else:
        print(wrd, "is a consonant")


if __name__ == '__main__':
    words = "an and cheese cake loose bruise chase case number".split()

    for word in words:
        is_vowel_or_consonant(word)
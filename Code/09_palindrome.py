# encoding=utf-8
# Created by quazinafiulislam


def is_palindrome(word):
    return word == word[::-1]

if __name__ == '__main__':

    test_name = 'stanley yelnats'

    if is_palindrome(test_name):
        print("Yes! Horay!", test_name)
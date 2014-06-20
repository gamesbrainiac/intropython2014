# encoding=utf-8
# Created by quazinafiulislam


def print_divider():
    end = '+' + ('-' * 4)

    print(end * 2 + '+')


def print_mids():
    mid = '|' + (' ' * 4)

    for i in range(4):
        print(mid * 2 + '|')


if __name__ == '__main__':
    print_divider()
    print_mids()
    print_divider()
    print_mids()
    print_divider()
import types
from tools import logger_path

@logger_path('main2.log')
def flat_generator(list_of_list):
    for listing in list_of_list:
        if type(listing) is list:
            yield from flat_generator(listing)
        else:
            yield listing
def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print(list(flat_generator(list_of_lists_1)))

if __name__ == '__main__':
    test_2()
class FlatIterator:

    def __init__(self, list_of_list):
        self.start = 0
        self.end = len(list_of_list)
        self.list = list_of_list

    def __iter__(self):
        self.cursor_big = 0
        self.cursor_small = self.start - 1
        return self

    def __next__(self):
        self.cursor_small += 1
        if self.cursor_small <= len(self.list[self.cursor_big]) - 1:
            return self.list[self.cursor_big][self.cursor_small]
        else:
            self.cursor_big += 1
            self.cursor_small = 0
            if self.cursor_big == self.end:
                raise StopIteration
            else:
                return self.list[self.cursor_big][self.cursor_small]

                


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item 

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    # for i in FlatIterator(list_of_lists_1):
    #     print(i)
    
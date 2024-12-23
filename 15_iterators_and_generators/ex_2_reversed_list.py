class reverse_iter:
    def __init__(self, obj):
        self.data = obj
        self.end_index = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        self.end_index -= 1
        if self.end_index >= 0:
            return self.data[self.end_index]

        raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:
    print(item)

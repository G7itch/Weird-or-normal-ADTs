class FractalList:
    def __init__(self, n, values=None):
        if values is None:
            values = [None] * n
        self.values = values
        self.sub_lists = [None] * n

    def __getitem__(self, index):
        if index < len(self.values):
            return self.values[index]
        else:
            sub_list_index = (index - len(self.values)) // len(self.sub_lists)
            sub_list_offset = (index - len(self.values)) % len(self.sub_lists)
            return self.sub_lists[sub_list_index][sub_list_offset]

    def __setitem__(self, index, value):
        if index < len(self.values):
            self.values[index] = value
        else:
            sub_list_index = (index - len(self.values)) // len(self.sub_lists)
            sub_list_offset = (index - len(self.values)) % len(self.sub_lists)
            if self.sub_lists[sub_list_index] is None:
                self.sub_lists[sub_list_index] = FractalList(len(self.sub_lists))
            self.sub_lists[sub_list_index][sub_list_offset] = value

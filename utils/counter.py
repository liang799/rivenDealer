class Count:
    @staticmethod
    def countList(test_list):
        count = 0
        if isinstance(test_list, str):
            return 0
        if isinstance(test_list, dict):
            return Count.countList(test_list.values()) + Count.countList(test_list.keys()) + 1
        try:
            for idx in test_list:
                count = count + Count.countList(idx)
        except TypeError:
            return 0
        return count

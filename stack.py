class Stack:
    def __init__(self):
        self.__contents = []

    def __len__(self):
        return len(self.__contents)

    def peek(self):
        return self.__contents[-1]

    def pop(self):
        return self.__contents.pop(-1)

    def push(self, item):
        self.__contents.append(item)

    def __str__(self):
        result = "[\n"
        for i in range(len(self)-1, -1, -1):
            result += f"{self.__contents[i]}\n"
        return result + "]"


    
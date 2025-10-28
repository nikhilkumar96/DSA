class Logger:

    def __init__(self):
        self.word = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.word:
            if self.word[message] + 10 <= timestamp:
                self.word[message] = timestamp
                return True
            else:
                return False
        self.word[message] = timestamp

        return True



a = [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]

obj = Logger()

for i in range(1, len(a)):
    print(obj.shouldPrintMessage(a[i][0], a[i][1]))
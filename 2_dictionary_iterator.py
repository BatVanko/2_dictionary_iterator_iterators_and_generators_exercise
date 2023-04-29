class dictionary_iter:
    def __init__(self, dic):
        self.dic = dic
        self.idx = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx > len(self.dic)-1:
            raise StopIteration
        result = list(self.dic.items())[self.idx]
        self.idx += 1
        return result


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print(20*'-')

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)







# 1
class RangeIterator:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        if self.step == 0:
            raise ValueError("шаг не может быть 0")

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start > self.end:
                raise StopIteration
        start = self.start
        self.start += self.step
        return start


for elem in RangeIterator(10, 100, 10):
    print(elem)



#2

def gen_fibonacci(limit):
    a, b = 0, 1
    counter = 0
    while counter < limit:
        yield a
        a, b = b, a + b
        counter += 1
for number in gen_fibonacci(15):
    print(number)

#3
filename = ['adsaf','','adfdsaf','asdafaf']
class LogReader:
    def __iter__(self):
        for i in filename:
            clean_i = i.strip()
            if clean_i:
                yield clean_i
reader = LogReader()
print(reader)




#4

def flatten(iterable):
    for item in iterable:
        if isinstance(item, Iterable):
            yield from flatten(item)
        else:
            yield item
input_lst = [1, [2, 3], [[4], 5], 6]
output_lst = list(flatten(input_lst))
print(output_lst)



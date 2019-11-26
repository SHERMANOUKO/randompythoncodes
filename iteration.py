#convert a list iterable to an iterator

items = [1, 2, 3, 4]
i_items = iter(items)

while True:
    try:
        item = next(i_items)
        print(item)
    except StopIteration:
        break

#custom range class with iterable
class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration

        current = self.value
        self.value += 1
        return current

nums = MyRange(0,11)

for num in nums:
    print(num)

#using a generator, 
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

gen_nums = my_range(0, 10)

for num in gen_nums:
    print(num)
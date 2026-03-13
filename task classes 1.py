#1

class Variable:
    var1 = 3
    var2 = 4
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def display(self):
        print(self.var1, self.var2)
    def var_sum(self):
        print(self.var1 + self.var2)
    def max_var(self):
        print(max(self.var1, self.var2))


variable_1 = Variable(5, 6)
variable_1.display()
variable_1.var_sum()
variable_1.max_var()

#2

class Counter:
    def __init__(self, start = 0, min1 = 0, max1 = 10, value = 0):
        self.min = min1
        self.max = max1
        self._value = max(min1, min(start, max1))
    def increase(self):
        if self._value < self.max:
            self._value += 1
        else:
            print('Stop')
    def decrease(self):
        if self._value > self.min:
            self._value -= 1
        else:
            print('Stop')
    @property
    def value(self):
        return self.value

counter = Counter()

counter.increase()
counter.increase()
print(counter._value)
counter.decrease()

print(counter._value)

#3

class Shop:
    def __init__(self):
        self.items = {}
    def add_item(self, name, price):
        self.items[name] = price
    def remove_item(self, name):
        del self.items[name]
    def search_name(self, name):
        return self.items[name]

mag = Shop()
mag.add_item("apple", 30)
mag.add_item("banana", 20)
mag.add_item("cherry", 15)
mag.remove_item("apple")
print(mag.search_name("banana"))
print(mag.search_name("apple"))

#4

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.box = 0
    def can_add(self,v):
        return v + self.box <= self.capacity
    def add(self,v):
        if self.can_add(v):
            self.box += v
            return True
        else:
            return False


box = MoneyBox(capacity=30)
print(box.add(v = 29))
print(box.add(v = 31))


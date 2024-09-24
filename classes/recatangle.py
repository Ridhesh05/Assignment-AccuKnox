class rectangle:
    # so here __init__ is a constructor and length and width are attributes with specific int values
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width

    # area is a method
    def area(self):
        return self.length * self.width
    # to iterate we use __iter__
    def __iter__(self):
        yield {"length":self.length}
        yield {"width":self.width}

rect = rectangle(10, 20)
print(rect.area())
for i in rect:
    print(i)
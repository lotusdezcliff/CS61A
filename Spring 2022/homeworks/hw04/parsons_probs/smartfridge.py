class SmartFridge:
    """"
    >>> fridgey = SmartFridge()
    >>> fridgey.add_item('Mayo', 1)
    'I now have 1 Mayo'
    >>> fridgey.add_item('Mayo', 2)
    'I now have 3 Mayo'
    >>> fridgey.use_item('Mayo', 2.5)
    'I have 0.5 Mayo left'
    >>> fridgey.use_item('Mayo', 0.5)
    'Uh oh, buy more Mayo!'
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += quantity
        return f'I now have {self.items[item]} {item}'

    def use_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        if self.items[item] - quantity >= 0:
            self.items[item] -= quantity
            return f'I have {self.items[item]} {item} left'
        else:
            return f'Uh oh, buy more {item}!'

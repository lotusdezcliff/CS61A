# Q1: Map, Filter, Reduce
def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    "*** YOUR CODE HERE ***"
    return [fn(x) for x in seq]

def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    "*** YOUR CODE HERE ***"
    return [x for x in seq if pred(x)]

def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"
    if len(seq) == 1:
        return seq[0]
    else:
        while len(seq) >= 2:
            result = combiner(seq[0], seq[1])
            seq[0] = result
            seq.pop(1)
        return seq[0]

# Q2: WWPD: Mutability
# What would Python display? In addition to giving the output, draw the box and pointer diagrams for each list to the right.

# >>> s1 = [1, 2, 3]
# >>> s2 = s1
# >>> s1 is s2
# Output: True

# >>> s2.extend([5, 6])
# >>> s1[4]
# Output: 6

# >>> s1.append([-1, 0, 1])
# >>> s2[5]
# Output: [-1, 0, 1]

# >>> s3 = s2[:]
# >>> s3.insert(3, s2.pop(3))
# >>> len(s1)
# Output: 6

# >>> s1[4] is s3[6]
# Output: False

# >>> s3[s2[4][1]]
# Output: 1

# >>> s1[:3] is s2[:3]
# Output: False

# >>> s1[:3] == s2[:3]
# Output: True

# >>> s1[4].append(2)
# >>> s3[6][3]
# Output: Error

# Q3: WWPD: Student OOP
# Below we have defined the classes Professor and Student, implementing some of what was described above. Remember that Python passes the self argument implicitly to methods when calling the method directly on an object.
class Student:

    max_slip_days = 3 # this is a class variable

    def __init__(self, name, staff):
        self.name = name # this is an instance variable
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_slip_days(self, student, days):
        student.max_slip_days = days

# What will the following lines output?
# >>> callahan = Professor("Callahan")
# >>> elle = Student("Elle", callahan)
# Output: Added Elle

# >>> elle.visit_office_hours(callahan)
# Output: Thanks, Callahan

# >>> elle.visit_office_hours(Professor("Paulette"))
# Output: Thanks, Paulette

# >>> elle.understanding
# Output: 1

# >>> [name for name in callahan.students]
# Output: [Elle]

# >>> x = Student("Vivian", Professor("Stromwell")).name
# Output: Added, Vivian

# >>> x
# Output: Vivian

# >>> [name for name in callahan.students]
# Output: [Elle]

# >>> elle.max_slip_days
# Output: 3

# >>> callahan.grant_more_slip_days(elle, 7)
# >>> elle.max_slip_days
# Output: 7

# >>> Student.max_slip_days
# Output: 3


# Q4: Keyboard
class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.
    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):
        self.buttons = {}
        i = 0
        for button in args:
            self.buttons[button.pos] = button

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        if info in self.buttons:
            self.buttons[info] = self.press
            self.times_pressed += 1
            return self.buttons[info]
        return ""

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        ________________
        for ________ in ____________________:
            ________________
        ________________


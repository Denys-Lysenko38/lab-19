class Nat:
    def __init__(self, value):
        self.value = value
        self.divs = []
        self.calc_divs()

    def calc_divs(self):
        self.divs = [i for i in range(1, self.value + 1) if self.value % i == 0]

    def display_value(self):
        print(f"Число: {self.value}")

    def set_value(self, new_value):
        self.value = new_value
        self.calc_divs()

    def display_divs(self):
        print(f"Дільники числа {self.value}: {' '.join(map(str, self.divs))}")

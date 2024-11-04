class CHAIR:
    def __init__(self, name, color, price, material):
        self.name = name
        self.color = color
        self.price = price
        self.material = material

    def change_price(self, new_price):
        self.price = new_price

    def display_info(self):
        return f"Назва: {self.name}, Колір: {self.color}, Ціна: {self.price}, Матеріал: {self.material}"

chairs = [
    CHAIR("Стілець 1", "Червоний", 150, "Дерево"),
    CHAIR("Стілець 2", "Синій", 200, "Метал"),
    CHAIR("Стілець 3", "Зелений", 180, "Пластик")
]

for chair in chairs:
    print(chair.display_info())

chairs[0].change_price(170)
print("\nПісля зміни ціни:")
print(chairs[0].display_info())
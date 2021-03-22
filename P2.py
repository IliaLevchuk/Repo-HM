class Roads:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def count_materials(self):
        return f"Масса асфальта: {self.length * self.width * 25 * 1 } kg"

Road = Roads(100, 100)
print(Road.count_materials())
class Cars:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{''.join(self.name)} go")
    def stop(self):
        print(f"{''.join(self.name)} stopped")
    def turn(self, direction):
        print (f'{"".join(self.name)} turn' + direction)
    def show_speed(self):
        print(f"{''.join(self.name)} движется со скоростью: {''.join(self.speed)}")

class TownCars(Cars):
    def show_speed(self):
        return f"{''.join(self.name)} движется с превышением скрорости! : {''.join(self.speed - 60)} км/ч "\
            if self.speed > 60 else f"{''.join(self.name)} движется с допустимой скоростью"


class SportCars(Cars):
    """Ура спортивный автомобиль"""


class WorkCars(Cars):
    def show_speed(self):
        return f"{''.join(self.name)} движется с превышением скрорости! : {''.join(self.speed - 40)} км/ч "\
            if self.speed > 40 else f"{''.join(self.name)} движется с допустимой скоростью"


class PoliceCars(Cars):
    def __init__(self,speed, color, name, is_police=True):
        super().__init__(self,speed, color, name, is_police)

town_car = TownCars(60, "Blue", "Mazda")
town_car.stop()
town_car.go()
town_car.show_speed()
from abc import ABC, abstractmethod


class Base(ABC):

    @abstractmethod
    def __str__(self):
        pass

class Clothes(Base):
    """Clothes"""
    def __init__(self, name, v, h):
        self.name = name
        self.v = v
        self.h = h

# Не получилось релизовать сумму итоговых значений
    @property
    def result_sum(self):
        return f'Общая площадь ткани {round(self.v / 6.5 + 0.5) + round(self.h * 2 + 0.3)}'

    def __str__(self):
        return f"Yours clothes: {self.name}"

class Coat(Clothes):

    def fabric_coat_sum(self):
        return f"Количество М ткани для пальто {round(self.v / 6.5 + 0.5)}"


    def __str__(self):
        return f'For coat size {self.v} need {round(self.v / 6.5 + 0.5)} M fabric'

class Suit(Clothes):

    def fabric_suit_sum(self):
        return f"Value M for suit {self.h * 2 + 0.3} "

    def __str__(self):
        return f'For suit size {self.h} need {self.h * 2 + 0.3} M fabric'

coat = Coat("Zara", 4, 5)
suit = Suit("Adidas", 5, 6)
print(coat.__str__())
print(suit.__str__())
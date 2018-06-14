class LandAnimal:
    def __init__(self):
        super().__init__()
        self.walking_speed = 5

    def increase_walking_speed(self, how_much):
        self.walking_speed += how_much


class WaterAnimal:
    def __init__(self):
        super().__init__()
        self.swiming_speed = 10

    def increase_swiming_speed(self, how_much):
        self.swiming_speed += how_much


class Amphibian(WaterAnimal, LandAnimal):
    def __init__(self):
        super().__init__()


amphibian = Amphibian()
amphibian.increase_swiming_speed(25)
amphibian.increase_walking_speed(10)
print(amphibian.swiming_speed)
print(amphibian.walking_speed)

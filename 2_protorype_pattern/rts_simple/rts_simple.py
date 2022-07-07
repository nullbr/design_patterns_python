# Knight class with properties: life, speed, attack_power, attack_range, weapon
class Knight(object):
    def __init__(self, level):
        self.unit_type = "Knight"

        if level == 1:
            self.life = 400
            self.speed = 5
            self.attack_power = 3
            self.attack_range = 1
            self.weapon = "short sword"
        elif level == 2:
            self.life = 400
            self.speed = 5
            self.attack_power = 6
            self.attack_range = 2
            self.weapon = "long sword"

    def __str__(self):
        return  "Type: {0}\n"\
                "Life: {1}\n" \
                "Speed: {2}\n" \
                "Attack_power: {3}\n" \
                "Attack_range: {4}\n" \
                "Weapon: {5}\n".format(
                    self.unit_type,
                    self.life,
                    self.speed,
                    self.attack_power,
                    self.attack_range,
                    self.weapon
                )

# Archer object
class Archer(object):
    def __init__(self, level):
        self.unit_type = "Archer"

        if level == 1:
            self.life = 200
            self.speed = 7
            self.attack_power = 1
            self.attack_range = 5
            self.weapon = "short bow"
        elif level == 2:
            self.life = 200
            self.speed = 7
            self.attack_power = 1
            self.attack_range = 5
            self.weapon = "long bow"

    def __str__(self):
        return  "Type: {0}\n"\
                "Life: {1}\n" \
                "Speed: {2}\n" \
                "Attack_power: {3}\n" \
                "Attack_range: {4}\n" \
                "Weapon: {5}\n".format(
                    self.unit_type,
                    self.life,
                    self.speed,
                    self.attack_power,
                    self.attack_range,
                    self.weapon
                )

# Barracks class used to generate a knight in the game  
class Barracks(object):
    def build_unit(self, unit_type, level):
        if unit_type == "Knight":
            return Knight(level)
        elif unit_type == "Archer":
            return Archer(level)

if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit("Knight", 1)
    archer1 = barracks.build_unit("Archer", 2)
    print("[knight] {}".format(knight1))
    print("[archer] {}".format(archer1))
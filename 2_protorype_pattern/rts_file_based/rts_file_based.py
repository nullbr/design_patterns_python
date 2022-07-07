# Knight class with properties: life, speed, attack_power, attack_range, weapon
class Knight(object):
    def __init__(self, level):
        self.unit_type = "knight"

        filename = "./2_protorype_pattern/rts_file_based/{}_{}.dat".format(self.unit_type, level)

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[3]

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
        self.unit_type = "archer"

        filename = "./2_protorype_pattern/rts_file_based/{}_{}.dat".format(self.unit_type, level)

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[3]

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
    archer1 = barracks.build_unit("Archer", 1)
    print("[knight] {}".format(knight1))
    print("[archer] {}".format(archer1))
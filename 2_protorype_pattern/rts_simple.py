# Knight class with properties: life, speed, attack_power, attack_range, weapon
class Knight(object):
    def __init__(
        self,
        life,
        speed,
        attack_power,
        attack_range,
        weapon):
    
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return "Life: {0}\n" \
                "Speed: {1}\n" \
                "Attack_power: {2}\n" \
                "Attack_range: {3}\n" \
                "Weapon: {4}\n".format(
                    self.life,
                    self.speed,
                    self.attack_power,
                    self.attack_range,
                    self.weapon
                )

# Archer object
class Archer(object):
    def __init__(
        self,
        life,
        speed,
        attack_power,
        attack_range,
        weapon):
        
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return "Life: {0}\n" \
                "Speed: {1}\n" \
                "Attack_power: {2}\n" \
                "Attack_range: {3}\n" \
                "Weapon: {4}\n".format(
                    self.life,
                    self.speed,
                    self.attack_power,
                    self.attack_range,
                    self.weapon
                )

# Barracks class used to generate a knight in the game  
class Barracks(object):
    def generate_knight(self):
        return Knight(400, 5, 3, 1, "short sword")

    def generate_archer(self):
        return Archer(200, 7, 1, 5, "bow")

if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.generate_knight()
    archer1 = barracks.generate_archer()
    print("[knight] {}".format(knight1))
    print("[archer] {}".format(archer1))
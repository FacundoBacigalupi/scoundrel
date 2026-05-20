class Player:
    def __init__(self):
        self.health = 20
        self.weapon = None
        self.last_monster_killed_with_weapon = None

    def equip_weapon(self, card):
        self.weapon = card
        self.last_monster_killed_with_weapon = None  # Reset the record of monster killed with weapon

    def drink_potion(self, card):
        self.health = min(self.health + card.value(), 20)

    def fight_barehanded(self, monster):
        self.health = max(self.health - monster.value(), 0)

    def fight_with_weapon(self, monster):
        if self.last_monster_killed_with_weapon is None or self.last_monster_killed_with_weapon > monster.value():
            self.health = max(self.health - max(monster.value() - self.weapon.value(), 0), 0)
            self.last_monster_killed_with_weapon = monster.value()
            return True

        return False
    
    def is_dead(self):
        return self.health <= 0
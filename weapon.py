class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int):
        self.name = name
        self.weapon_type = weapon_type
        self.original_damage = damage
        self.damage = damage
        self.value = value

sword = Weapon(name='Sword', weapon_type='close_range', damage=15, value=10)
fists = Weapon(name='Fists', weapon_type='close_range', damage=5, value=0)
bow = Weapon(name='Bow', weapon_type='long_range', damage=10, value=7)


import random
from math import ceil
from healthbar import HealthBar
from weapon import fists


class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = fists

    def attack(self, target) -> None:
        if self.health == 0:
            print(f"{self.name} is dead and can't attack.")
            return

        critical_options = [False, True]
        critical = random.choices(critical_options, weights=[0.7, 0.3])[0]

        if critical:
            self.weapon.damage = self.weapon.original_damage * 2
            print(f'Critical hit from {self.name}!')
        else:
            self.weapon.damage = self.weapon.original_damage

        if self.health != 0 and critical is False:
            self.weapon.damage = ceil(random.uniform(0.1, 1.0) * self.weapon.damage)
            target.health -= self.weapon.damage
            target.health = max(target.health, 0)

        elif self.health != 0 and critical is True:
            target.health -= self.weapon.damage
            target.health = max(target.health, 0)

        else:
            target.health = max(target.health, 0)

        target.health_bar.update()
        print(f'{self.name} dealt {self.weapon.damage} damage using {self.weapon.name}')


class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, health)
        self.original_weapon = self.weapon
        self.health_bar = HealthBar(self, color='blue')

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f'{self.name} equipped a {self.weapon.name}')

    def drop(self) -> None:
        if self.weapon.name == 'Fists':
            return

        print(f'{self.name} dropped {self.weapon.name}')
        self.weapon = self.original_weapon


class Enemy(Character):
    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name, health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color='yellow')

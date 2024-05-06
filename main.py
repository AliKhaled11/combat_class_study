import time
import os
from weapon import bow, sword
from character import Hero, Enemy

hero = Hero(name='Hero', health=100)
hero.equip(sword)
enemy = Enemy(name='Enemy', health=100, weapon=sword)

while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()

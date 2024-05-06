from character import Character

hero = Character(name='Hero', health=100, damage=20)
enemy = Character(name='Enemy', health=100, damage=20)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    print(f'health of {hero.name} is {hero.health}')
    print(f'health of {enemy.name} is {enemy.health}')

    input()

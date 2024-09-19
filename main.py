from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.\nМонстр повержен!")

    def __str__(self):
        return "меч"

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.\nМонстр повержен!")

    def __str__(self):
        return "лук"

class Fighter():
    def __init__(self, sel_weapon):
        self.sel_weapon = sel_weapon

    def change_weapon(self, new_weapon):
        self.sel_weapon = new_weapon
        print(f"Боец выбирает {self.sel_weapon}.")

    def attack(self):
        self.sel_weapon.attack()

class Monster():
    def __init__(self):
        pass

men1 = Fighter(Bow())

men1.change_weapon(Sword())
men1.attack()
men1.change_weapon(Bow())
men1.attack()
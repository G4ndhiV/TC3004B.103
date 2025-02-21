#VideogameTest

from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def defend(self):
        pass

class Knight(Character):
    def attack(self):
        return "El caballero da espadazo"
    
    def defend(self):
        return "El caballero defiende con un escudo"

class Archer(Character):
    def attack(self):
        return "El arquero dispara su arco"
    
    def defend(self):
        return "El arquero evita un ataque"

class Mage(Character):
    def attack(self):
        return "El mago lanza hace un hechizo"
    
    def defend(self):
        return "El mago crea una barrera"

class Faction(ABC):
    @abstractmethod
    def get_characters(self):
        pass
    
    @abstractmethod
    def start_battle(self):
        pass

class Kingdom(Faction):
    def get_characters(self):
        return [Knight(), Archer(), Mage()]
    
    def start_battle(self):
        return "Comienza una guerra"

class DarkForces(Faction):
    def get_characters(self):
        return [Knight(), Mage()]
    
    def start_battle(self):
        return "Las fuerzas Obscuras comienzan una batalla"

def main():
    kingdom = Kingdom()
    print(kingdom.start_battle())
    for character in kingdom.get_characters():
        print(character.attack())
        print(character.defend())

if __name__ == "__main__":
    main()
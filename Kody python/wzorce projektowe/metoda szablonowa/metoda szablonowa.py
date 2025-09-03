from abc import ABC, abstractmethod

# Klasa bazowa z metodą szablonową
class GameAI(ABC):
    def turn(self):
        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()

    # Domyślna implementacja
    def collect_resources(self):
        for structure in self.built_structures:
            structure.collect()

    @abstractmethod
    def build_structures(self):
        pass

    @abstractmethod
    def build_units(self):
        pass

    def attack(self):
        enemy = self.closest_enemy()
        if enemy is None:
            self.send_scouts("map_center")
        else:
            self.send_warriors(enemy.position)

    @abstractmethod
    def send_scouts(self, position):
        pass

    @abstractmethod
    def send_warriors(self, position):
        pass

    # Pomocnicze dane i metody
    def __init__(self):
        self.built_structures = []
        self.scouts = []
        self.warriors = []

    def closest_enemy(self):
        # Przykładowa symulacja
        return None  # lub np. Enemy(position="E5")


# Przykładowa struktura
class Structure:
    def collect(self):
        print("Zbieranie zasobów z budowli.")


# Klasa Orków
class OrcsAI(GameAI):
    def build_structures(self):
        print("Orkowie budują farmy, koszary, twierdzę.")

    def build_units(self):
        print("Orkowie budują jednostki.")
        if not self.scouts:
            print("Tworzenie piechura – dodany do zwiadowców.")
            self.scouts.append("Piechur")
        else:
            print("Tworzenie żołnierza – dodany do wojowników.")
            self.warriors.append("Żołnierz")

    def send_scouts(self, position):
        if self.scouts:
            print(f"Orkowie wysyłają zwiadowców na pozycję {position}.")

    def send_warriors(self, position):
        if len(self.warriors) > 5:
            print(f"Orkowie wysyłają wojowników na pozycję {position}.")


# Klasa Potworów
class MonstersAI(GameAI):
    def collect_resources(self):
        print("Potwory nie zbierają zasobów.")

    def build_structures(self):
        print("Potwory nie budują budowli.")

    def build_units(self):
        print("Potwory nie tworzą jednostek.")

    def send_scouts(self, position):
        print(f"Potwory wysyłają zwiadowców na pozycję {position}.")

    def send_warriors(self, position):
        print(f"Potwory wysyłają wojowników na pozycję {position}.")


# Przykładowe użycie
if __name__ == "__main__":
    print("Tura Orków:")
    orcs = OrcsAI()
    orcs.built_structures = [Structure(), Structure()]
    orcs.turn()

    print("\nTura Potworów:")
    monsters = MonstersAI()
    monsters.turn()

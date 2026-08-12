import json
import random
import sys


class Character:
    """Base class demonstrating OOP inheritance and encapsulation."""
    def __init__(self, name: str, hp: int, attack: int):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, damage: int):
        self.hp = max(0, self.hp - damage)


class Player(Character):
    """Derived class handling player inventory, levels, and state."""
    def __init__(self, name: str):
        super().__init__(name=name, hp=100, attack=15)
        self.level = 1
        self.xp = 0
        self.gold = 50
        # List structure for inventory
        self.inventory = ["Rusty Sword", "Health Potion"]
        # Set structure to track unique discovered locations
        self.discovered_places = set()

    def gain_xp(self, amount: int):
        self.xp += amount
        print(f"✨ Gained {amount} XP!")
        # Quick lambda expression to calculate XP needed for next level
        xp_needed = lambda lvl: lvl * 100
        if self.xp >= xp_needed(self.level):
            self.level += 1
            self.max_hp += 20
            self.hp = self.max_hp
            self.attack += 5
            print(f"🎉 LEVEL UP! You are now Level {self.level}!")

    def show_stats(self):
        print("\n=== PLAYER STATS ===")
        print(f"Name: {self.name} | Level: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp} | Attack: {self.attack}")
        print(f"Gold: {self.gold} | XP: {self.xp}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print(f"Visited: {', '.join(self.discovered_places) if self.discovered_places else 'None'}")
        print("====================")


class GameEngine:
    """Handles game loops, data persistence, and environment logic."""
    def __init__(self):
        self.player = None
        # Dictionary structure holding game world data
        self.locations = {
            "town": {"desc": "A peaceful village. Safe but quiet.", "enemy": None},
            "forest": {"desc": "Dark trees whisper secrets. Dangerous.", "enemy": "Goblin"},
            "cave": {"desc": "A damp, echoing cavern. Very dangerous.", "enemy": "Troll"}
        }

    def save_game(self):
        """Demonstrates File I/O using JSON serialization."""
        if not self.player:
            return
        data = {
            "name": self.player.name,
            "level": self.player.level,
            "xp": self.player.xp,
            "gold": self.player.gold,
            "inventory": self.player.inventory,
            "discovered": list(self.player.discovered_places)
        }
        with open("savegame.json", "w") as f:
            json.dump(data, f)
        print("💾 Game saved successfully!")

    def load_game(self) -> bool:
        """Demonstrates robust File I/O and Error Handling."""
        try:
            with open("savegame.json", "r") as f:
                data = json.load(f)
                self.player = Player(data["name"])
                self.player.level = data["level"]
                self.player.xp = data["xp"]
                self.player.gold = data["gold"]
                self.player.inventory = data["inventory"]
                self.player.discovered_places = set(data["discovered"])
                print(f"📂 Welcome back, {self.player.name}!")
                return True
        except FileNotFoundError:
            return False
        except (json.JSONDecodeError, KeyError):
            print("⚠️ Save file corrupted. Starting fresh.")
            return False

    def combat(self, enemy_name: str):
        """Simulates a turn-based combat loop."""
        # Multi-variable unpacking/tuples for enemy stats generation
        enemy_hp, enemy_atk = (40, 8) if enemy_name == "Goblin" else (80, 14)
        enemy = Character(enemy_name, enemy_hp, enemy_atk)
        
        print(f"⚔️ A wild {enemy.name} appears!")
        
        while enemy.is_alive() and self.player.is_alive():
            print(f"\nYour HP: {self.player.hp} | {enemy.name} HP: {enemy.hp}")
            action = input("Do you want to (A)ttack or (P)otion? ").strip().lower()
            
            if action == 'a':
                dmg = random.randint(self.player.attack - 5, self.player.attack + 5)
                enemy.take_damage(dmg)
                print(f"💥 You strike the {enemy.name} for {dmg} damage!")
            elif action == 'p':
                if "Health Potion" in self.player.inventory:
                    self.player.inventory.remove("Health Potion")
                    self.player.hp = min(self.player.max_hp, self.player.hp + 50)
                    print("🧪 You drank a potion and restored 50 HP!")
                else:
                    print("❌ You don't have any potions!")
                    continue
            else:
                print("❌ Invalid choice! You stand still.")

            if enemy.is_alive():
                e_dmg = random.randint(enemy.attack - 3, enemy.attack + 3)
                self.player.take_damage(e_dmg)
                print(f"🥊 The {enemy.name} hits you for {e_dmg} damage!")

        if self.player.is_alive():
            gold_drop = random.randint(10, 30)
            self.player.gold += gold_drop
            print(f"🏆 victory! You defeated the {enemy.name}!")
            print(f"💰 Found {gold_drop} gold.")
            self.player.gain_xp(50)
        else:
            print("💀 You died! Game over.")
            sys.exit()

    def travel(self):
        """Handles choice matrix, filtering, and conditional travel logic."""
        print("\nWhere would you like to go?")
        # List comprehension to generate menu options
        choices = [loc for loc in self.locations.keys()]
        for i, loc in enumerate(choices, 1):
            print(f"{i}. {loc.title()}")
        
        try:
            choice = int(input("Enter number: ")) - 1
            if choice not in range(len(choices)):
                raise ValueError
        except ValueError:
            print("❌ Invalid location selection.")
            return

        dest_name = choices[choice]
        dest_data = self.locations[dest_name]
        
        self.player.discovered_places.add(dest_name)
        print(f"\n--- {dest_name.title()} ---")
        print(dest_data["desc"])

        if dest_data["enemy"]:
            self.combat(dest_data["enemy"])

    def start(self):
        """Main game control loop."""
        print("=== WELCOME TO THE PYTHON RPG HUB ===")
        if not self.load_game():
            name = input("Enter your character's name: ").strip()
            if not name:
                name = "Hero"
            self.player = Player(name)

        while True:
            print("\nMain Menu: (T)ravel, (S)tats, (P)ersist/Save, (Q)uit")
            choice = input("What to do? ").strip().lower()
            
            if choice == 't':
                self.travel()
            elif choice == 's':
                self.player.show_stats()
            elif choice == 'p':
                self.save_game()
            elif choice == 'q':
                self.save_game()
                print("Goodbye!")
                break
            else:
                print("❌ Unknown command.")


if __name__ == "__main__":
    game = GameEngine()
    game.start()

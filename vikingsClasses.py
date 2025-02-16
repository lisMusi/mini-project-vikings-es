import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength) # super() sirve para llamar al constructor de la clase base (Soldier)
        self.name = name

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
          return f"{self.name} has received {damage} points of damage"
        else:
          return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
          return f"A Saxon has received {damage} points of damage"
        else:
          return "A Saxon has died in combat"

# WAR

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        result = saxon.receiveDamage(viking.attack())  # El vikingo ataca al sajón
        if saxon.health <= 0:  # Si el sajón muere
            self.saxonArmy.remove(saxon)  # Eliminar el sajón de la lista

        return result
    
    def saxonAttack(self):
        # your code here
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        result = viking.receiveDamage(saxon.attack())  # El sajón ataca al vikingo
        if viking.health <= 0:  # Si el vikingo muere
            self.vikingArmy.remove(viking)  # Eliminar al vikingo de la lista

        return result

    def showStatus(self):
        # your code here
        if not self.saxonArmy: # Si no quedan sajones
          return "Vikings have won the war of the century!"
        elif not self.vikingArmy: # Si no quedan vikingos
          return "Saxons have fought for their lives and survived another day..."
        else: # Si aun quedan ambos
          return "Vikings and Saxons are still in the thick of battle."
            
    pass



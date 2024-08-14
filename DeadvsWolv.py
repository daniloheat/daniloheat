import random
import time

class Character:

    def __init__(self, name) -> None:
        self.name = name
        self.health = 0

    def init_health(self):
        self.health = random.randint(700, 1200)

    def update_health(self, power):
        self.health -= power

    def update_power(self):
        if self.name == "deadpool":
            return random.randint(10,100)
        if self.name == "wolverine":
            return random.randint(10,120)

    def update_evade(self):
        if self.name == "deadpool":
            return  random.randint(1,4)
        if self.name == "wolverine":
            return  random.randint(1,5)

    def update_turn(self, turn):
        self.turn = turn

    
def flip_coin():
    return random.randint(1,2)

deadpool = Character("deadpool")
wolverine = Character("wolverine")
deadpool.init_health()
wolverine.init_health()
turn = flip_coin()
attack = 1

while deadpool.health and wolverine.health != 0:
    print("")
    print(f"ATAQUE NUMERO {attack}!!!")
    print("")
    match turn:
        case 1:
            damage = deadpool.update_power()
            print("Deadpool lanza su ataque")
            evade = wolverine.update_evade()
            print("Wolverine intenta esquivarlo")
            if evade < 5:
                wolverine.update_health(damage)
                if wolverine.health <=0:
                    print("Wolverine ha sido derrotado")
                    break
                print(f"Deadpool conectó a Wolverine, su HP es ahora de {wolverine.health}.")
                if damage == 100:
                    print("El ataque ha sido devastador, Wolverine necesita un turno para recuperarse")
                else:
                    turn = 2
            else:
                print("Wolverine esquivó el golpe")
            time.sleep(1)
        case 2:
            damage = wolverine.update_power()
            print("Wolverine comienza su ofensiva")
            evade = deadpool.update_evade()
            print("Deadpool se defiende")
            if evade < 4:
                deadpool.update_health(damage)
                if deadpool.health <=0:
                    print("Deadpool ha sido derrotado")
                    break
                print(f"Wolverine conectó a Deadpool, su HP es ahora de {deadpool.health}.")
                if damage == 120:
                    print("El ataque ha sido devastador, Deadpool ha quedado noqueado")
                else:
                    turn = 1
            else:
                print("Deadpool no tiene ni un rasguño")
            time.sleep(1)
    attack += 1
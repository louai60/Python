class character :

    def __init__( self , name, strength, speed, health ):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health
    
    def attack(self, target):
        if target.health <= self.strength:
            target.health = 0
            print(f'{target.name} is dead !!!')
        else : 
            target.health -= self.strength
            print(f'{self.name}')
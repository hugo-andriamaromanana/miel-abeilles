from generator.bees import Bee
import random

class Evolve(Bee):
    
    def sex(self, bee1: Bee, bee2: Bee)-> Bee:
        """
        Create a new bee with the behavior of the two parents
        """
        
        newBeeBehavior= []
        
        while len(newBeeBehavior) != bee1.behavior:
            newBeeBehavior.append(bee1.behavior.pop(0))
            newBeeBehavior.append(bee2.behavior.pop(0))
            
        return Bee(newBeeBehavior)
            
    def breed(self, bee1: Bee, bee2: Bee) -> tuple[Bee, Bee]:
        """
        Create two new bees with the behavior of the parents
        """
        return self.sex(bee1, bee2),self.sex(bee2,bee1)
    
    def mutation(self, bee: Bee) -> Bee:
        """
        Mutate the bee's behavior
        """
        shuffledBehavior= bee.behavior
        random.shuffle(shuffledBehavior)
        return Bee(shuffledBehavior)
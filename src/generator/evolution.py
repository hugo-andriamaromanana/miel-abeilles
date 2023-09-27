from src.generator.bees import Bee
import random

class Evolve():
    
    def sex(self, bee1: Bee, bee2: Bee)-> Bee:
        """
        Create a new bee with the behavior of the two parents
        """
        newBehavior = []
        
        i=0
        while len(newBehavior) != len(bee1.behavior):
            
            if i == len(bee1.behavior):
                i=0
            if bee1.behavior[i] not in newBehavior:
                newBehavior.append(bee1.behavior[i])
            if bee2.behavior[i] not in newBehavior:
                newBehavior.append(bee2.behavior[i])
            i+=1
            
        return Bee(newBehavior)
            
    def breed(self, bee1: Bee, bee2: Bee) -> tuple[Bee, Bee]:
        """
        Create two new bees with the behavior of the parents
        """
        return self.sex(bee1, bee2),self.sex(bee2,bee1)
    
    def mutation(bee: Bee) -> Bee:
        """
        Mutate the bee's behavior
        """
        shuffledBehavior= bee.behavior
        random.shuffle(shuffledBehavior)
        return Bee(shuffledBehavior)
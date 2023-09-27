from generator.flowers import Flower
from generator.bees import Bee
from generator.evolution import Evolve
import random

class Hive():
    
    def __init__(self):
        self.flowers = Flower().dfToArrayOfArrays()
        self.population :list = self.firstGeneration(100)
        self.averagePerformance :float = 0.0
        
    def firstGeneration(self, size: int) -> list[Bee]:
        """
        Create a list of bees with random behaviors as an array of arrays
        """
        shuffledFlowers= self.flowers
        random.shuffle(shuffledFlowers)
        return [Bee(shuffledFlowers) for _ in range(size)]
    
    def generatetNextGeneration(self) -> list[Bee]:
        """
        Sort and select the best half of the population
        Then breed the best half to create the next generation
        """
        self.population.sort(key=lambda bee: bee.score)
        newPopulation = self.population[:int(len(self.population)/2)]
        
        for i in range(1,int(len(self.population)/2),2):
            newBee1, newBee2 = Evolve().breed(newPopulation[i-1], newPopulation[i])
            newPopulation.append(newBee1)
            newPopulation.append(newBee2)
        
        return newPopulation
    
    def calculateAveragePerformance(self) -> float:
        """
        Calculate the average performance of the population
        """
        return sum([bee.score for bee in self.population])/len(self.population)
    
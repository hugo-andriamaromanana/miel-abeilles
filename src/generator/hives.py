from src.generator.flowers import Flower
from src.generator.bees import Bee
from src.generator.evolution import Evolve
import random
import math
class Hive():
    
    def __init__(self):
        self.flowers: list[list[int]] = Flower().dfToArrayOfArrays()
        self.population :list = self.firstGeneration(100)
        self.evolution :Evolve = Evolve()
        
    def firstGeneration(self, size: int) -> list[Bee]:
        """
        Create a list of bees with random behaviors as an array of arrays
        """
        firstGeneration = []
        shuffledFlowers= self.flowers
        
        for _ in range(size):
            random.shuffle(shuffledFlowers)
            firstGeneration.append(Bee(shuffledFlowers))
            
        return firstGeneration
            
    def generatetNextGeneration(self) -> list[Bee]:
        """
        Sort and select the best half of the population
        Then breed the best half to create the next generation
        """
        self.population.sort(key=lambda bee: bee.score)
        newPopulation = self.population[:int(len(self.population)/2)]
        
        for i in range(1, len(newPopulation) ,2):
            
            difference=abs(self.calculateAveragePerformanceSolo(newPopulation)-self.calculateAveragePerformanceSolo(self.population))
            mutationThreshold = random.randint(80,120)
            numberOfMutations = random.randint(1,3)

            if difference < mutationThreshold:
                for _ in range(numberOfMutations):
                    randomNumber=random.randint(0,len(newPopulation)-1)
                    newPopulation[randomNumber]=Evolve.mutation(newPopulation[randomNumber])
                       
            newBee1, newBee2 = self.evolution.breed(newPopulation[i-1], newPopulation[i])
            

            newPopulation.append(newBee1)
            newPopulation.append(newBee2)

        self.population = newPopulation
    
    def calculateAveragePerformanceSolo(self,group) -> int:
        return int(sum([bee.score for bee in group])/len(group))
        
    def calculateAveragePerformance(self) -> int:
        """
        Calculate the average performance of the population
        """
        topFifty = self.population[:int(len(self.population)/2)]
        return int(sum([bee.score for bee in topFifty])/len(topFifty))
    
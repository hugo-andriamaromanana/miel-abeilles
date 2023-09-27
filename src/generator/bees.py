import math

class Bee():
    
    def __init__(self, behavior):
        self.behavior: list[list[int]] = behavior
        self.score: int = self.calculateScore()
        
    def calculateDistance(point1, point2):
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    
    def calculateScore(self) -> float:
        score = 0
        for i in range(len(self.behavior)-1):
            score += Bee.calculateDistance(self.behavior[i], self.behavior[i+1])
        return score
    
    # def __repr__(self) -> str:
    #     return f"Score: {self.score} | Behavior: {self.behavior}"
from src.generator.hives import Hive
from src.utils.pandasUtils import *

def main(numberOfGenerations: int) -> None:
    
    hive = Hive()
    logs = pd.DataFrame(columns=["averageScore"])
    
    for _ in range(numberOfGenerations):
        
        hive.generatetNextGeneration()
        
        logs = pd.concat([logs, pd.DataFrame({
            "averageScore": [hive.calculateAveragePerformance()],
        })], ignore_index=True)
        
    saveLogs(logs,"results/logs.csv")
from src.utils.pandasUtils import *

class Flower():
    
    flowers=getDfFromCsv("assets/beeData.csv")

    def dfToArrayOfArrays(self) -> list[list[int]]:
        """
        Convert the pandas dataframe to an array of arrays
        """
        return self.flowers.values.tolist()
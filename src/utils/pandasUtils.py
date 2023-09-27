import pandas as pd

def getDfFromCsv(path: str) -> pd.DataFrame:
    """
    Returns a pandas DataFrame from a csv file
    """
    return pd.read_csv(path)

def saveLogs(df: pd.DataFrame, path: str)-> None:
    """
    Saves a pandas DataFrame to a csv file
    """
    df.to_csv(path, index=False)
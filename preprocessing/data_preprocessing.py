# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(df: pd.DataFrame, target:str, features: list=None, test_percent: int=.2):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        target (str): _description_
        features (list, optional): _description_. Defaults to None.
        test_percent (int, optional): _description_. Defaults to .02.

    Returns:
        _type_: _description_
    """
    if features == None:
        X = df.drop(target, axis=1)
        y = df[target]
    else:
        X = df[features]
        y = df[target]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_percent, random_state=42)
    
    return  X_train, X_test, y_train, y_test


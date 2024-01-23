# Import necessary libraries
import pandas as pd

def display_summary_stats(df: pd.DataFrame):
    """_summary_

    Args:
        df (pd.DataFrame): _description_

    Returns:
        _type_: _description_
    """
    return df.describe()

def check_if_data_balanced(df:pd.DataFrame, target: str, threshold: float=0.8):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        target (str): _description_
        threshold (float, optional): _description_. Defaults to 0.8.

    Returns:
        _type_: _description_
    """
    class_distribution = df[target].value_counts()
    print(class_distribution)
    is_balanced = class_distribution.min() / class_distribution.max() > threshold  # Adjust the threshold as needed   
    return is_balanced

def check_null_values(df:pd.DataFrame):
    """_summary_

    Args:
        df (pd.DataFrame): _description_

    Returns:
        _type_: _description_
    """
    # Create a summary DataFrame
    null_df = pd.DataFrame({
        'Column': df.columns,
        'Null Count': df.isnull().sum(),
        'Non-Null Count': df.count(),
        'Unique Values Count': df.nunique()
    })
    return null_df

def check_variable_correlations(df: pd.DataFrame):
    """_summary_

    Args:
        df (pd.DataFrame): _description_

    Returns:
        _type_: _description_
    """
    return df.corr()


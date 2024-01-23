import pandas as pd

def convert_date_column(df:pd.DataFrame, date_feature:str):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        date_feature (str): _description_

    Returns:
        _type_: _description_
    """
    date_feature_name = date_feature.lower().replace(" ", "_")
    # Convert date for year, month, day, dayofweek, and dayofyear
    df[f'{date_feature_name}_year'] = df[date_feature].dt.year
    df[f'{date_feature_name}_month'] = df[date_feature].dt.month
    df[f'{date_feature_name}_day'] = df[date_feature].dt.day
    df[f'{date_feature_name}_dayofweek'] = df[date_feature].dt.dayofweek
    df[f'{date_feature_name}_dayofyear'] = df[date_feature].dt.dayofyear   
    return df


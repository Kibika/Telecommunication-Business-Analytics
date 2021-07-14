import base64
import datetime
import io
import pandas as pd
import numpy as np
from textwrap import wrap
from urllib.parse import quote as urlquote

import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.graph_objects as go


def df_shape(df):
    print(f" There are {df.shape[0]} rows and {df.shape[1]} columns")

def percent_missing(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The dataset contains", totalMissing," missing values or", round(((totalMissing/totalCells) * 100), 2), "%", "of the dataset.")

def missing_per_column(df):
    print(round((df.isna().sum()*100)/len(df), 2))

def exploratory_hist(df):
    df.hist(figsize=(15,15), layout=(11,5))
    plt.show()

def impute(df):
    cat_list=['Bearer Id','Start','End','IMSI','MSISDN/Number','IMEI','Last Location Name','Handset Manufacturer','Handset Type']
    for i in df.columns:
        if i in cat_list:
            df[i]=df[i].fillna(df[i].mode())
        else:
            df[i]=df[i].fillna(df[i].mean())
    return df

def normalizer(df):
    df_new=df.drop(['Bearer Id','Start','End','IMSI','MSISDN/Number','IMEI','Last Location Name','Handset Manufacturer','Handset Type'],axis=1)
    norm = Normalizer()
    # normalize the data with boxcox
    normalized_data = norm.fit_transform(df_new)
    normalized_df=pd.DataFrame(normalized_data,columns = df_new.columns)
    final_df=pd.merge(df,normalized_df, how='right')
    return final_df

def date_time(df):
    df['Start']=pd.to_datetime(df['Start'], infer_datetime_format=True)
    df['End']=pd.to_datetime(df['End'], infer_datetime_format=True)
    return df
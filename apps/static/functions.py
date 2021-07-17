import base64
import datetime
import io
import pandas as pd
import numpy as np
from textwrap import wrap
from urllib.parse import quote as urlquote

import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table as dt
import pandas as pd
#import plotly.graph_objects as go


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
        if i not in cat_list:
            df[i]=df[i].fillna(df[i].mean())
        else:
            df[i]=df[i].fillna(df[i].value_counts().index[0])
    return df


def normalizer(df):
    df_new = df.drop(
        ['Bearer Id', 'Start', 'End', 'IMSI', 'MSISDN/Number', 'IMEI', 'Last Location Name', 'Handset Manufacturer',
         'Handset Type'], axis=1)
    norm = Normalizer()
    # norm=RobustScaler()
    # normalize the data with boxcox
    normalized_data = norm.fit_transform(df_new)
    normalized_df = pd.DataFrame(normalized_data, columns=df_new.columns)
    cols_to_use = df.columns.difference(normalized_df.columns)
    final_df = pd.merge(df[cols_to_use], normalized_df, left_index=True, right_index=True, how='outer')
    # final_df=pd.concat([df,normalized_df],axis=1)
    return final_df
    # final_df.hist(figsize=(15,15), layout=(11,5))



def date_time(df):
    df['Start']=pd.to_datetime(df['Start'], infer_datetime_format=True)
    df['End']=pd.to_datetime(df['End'], infer_datetime_format=True)
    return df

def create_options(df):
    """Creates options in the format that dash needs
     """
    options = []
    for i in df.columns:
        options.append({'label': "{}: {}".format(str(i),df[i].dtype), 'value': str(i)})
    return options


def find_agg(df: pd.DataFrame, agg_column: str, agg_metric: str, col_name: str, top: int, order=False) -> pd.DataFrame:
    new_df = df.groupby(agg_column)[col_name].agg(agg_metric).reset_index(name=col_name). \
                 sort_values(by=col_name, ascending=order)[:top]

    return new_df

def indicator(color, text, id_value):
    return html.Div(
        [
            html.P(id=id_value, className="indicator_value"),
            html.P(text, className="twelve columns indicator_text"),
        ],
        className="four columns indicator pretty_container",
    )

def get_piechart(labels, value, title):
    labels = ['<br>'.join(wrap(str(l), 20)) for l in labels]
    # labels = labels.values.tolist().apply(lambda x: '<br>'.join(textwrap.wrap(x, width=10)) for x in labels)
    # print(labels)
    colors = [
        '#36EEE0',
        '#F652A0',
        '#BCECE0',
        '#4C5270',
        '#0000FF',
        '#F83839',
        '#98042D',
        '#741AAC',
        '#21BF73',
        '#FF8300',
        '#FD49A0',
        '#8B2F97',
        '#F67280'
    ]
    fig = go.Figure(
        data=
        [
            go.Pie(
                labels=labels,
                values=value,
                hole=.3
            )
        ],
        layout=go.Layout(
            title=title,
            autosize=True,
        )
    )
    fig.layout.paper_bgcolor = 'rgba(255, 255, 255, 0)'
    fig.update_layout(legend_orientation='v')  # yanchor='bottom', xanchor='center',
    fig.update_traces(textposition='inside', textinfo='percent', marker=dict(colors=colors), automargin=True)

    return fig
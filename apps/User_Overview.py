import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table as dt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import pathlib
from app import app
from apps.static.functions import indicator, date_time, find_agg


PATH=pathlib.Path(__file__).parent
DATA_PATH=PATH.joinpath("../data").resolve()
df=pd.read_csv(DATA_PATH.joinpath("Week1_challenge_data_1.csv"), low_memory=False)
df=date_time(df)

unique_customers=df['MSISDN/Number'].unique()


layout=app.layout =html.Div([
html.Div([
            html.Pre(children="User", style={"fontSize":"150%"}),
            dcc.Dropdown(
                id='customer_dropdown', value='ALL', clearable=False,
                persistence=True, persistence_type='session',
                options=[{'label': x, 'value': x} for x in df['MSISDN/Number'].unique()],
                multi=False

            )
        ], className='twelve columns'),

dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                html.Div(
                    # dcc.Input(id="session_count", type="number", placeholder="", style={'marginRight': '10px'}),
                    id="overview_indicators",
                    className="row indicators",
                        children=[indicator("#00cc96", "Number of Sessions", id_value="session_count")],
                        style={"border-radius": "10px", "padding": "5px", "margin": "5px", 'backgroundColor': '#EDEBEA',
                               "width": "100%", "height": "150px"}
                ),
], ),
            ]),
        ], md=3),
dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div(
                        className="row indicators",
                        children=[
                            indicator("#119DFF", "Sessions Duration",
                                      id_value="duration"),

                        ],
                        style={"border-radius": "10px", "padding": "5px", "margin": "5px", 'backgroundColor': '#EDEBEA',
                               "width": "100%", "height": "150px"}),
                ], ),
            ], ),
        ], md=3),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div(
                        className="row indicators",
                        children=[
                            indicator("#119DFF", "Total Download Data", id_value="download_data"),
                        ],
                        style={"border-radius": "10px", "padding": "5px", "margin": "5px", 'backgroundColor': '#EDEBEA',
                               "width": "100%", "height": "150px"}),
                ], ),
            ], ),
        ], md=3),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div(
                        className="row indicators",
                        children=[
                            indicator("#119DFF", "Total Upload Data", id_value="upload_data"),
                        ],
                        style={"border-radius": "10px", "padding": "5px", "margin": "5px", 'backgroundColor': '#EDEBEA',
                               "width": "100%", "height": "150px"}),
                ], ),
            ], ),
        ], md=3)
    ]),dbc.Col([
                dbc.Row([
                    dbc.Col([

                        html.Div([
                            dcc.Graph(

                                id='pie-1'
                            )
                        ])

                    ])
                ])
            ],
                md=6
            ),

    ],id="overview")

@app.callback([Output('session_count', 'children'),Output('duration', 'children'),
               Output('download_data', 'children'),Output('upload_data', 'children'),
               Output('pie-1', 'figure')],
                [Input('customer_dropdown', 'value')])
def overview_page( value):
    df = pd.read_csv(DATA_PATH.joinpath("Week1_challenge_data_1.csv"), low_memory=False)

    app_data = df[
        ['Bearer Id', "MSISDN/Number", "Youtube DL (Bytes)", "Youtube UL (Bytes)", "Social Media DL (Bytes)",
         "Social Media UL (Bytes)",
         "Google DL (Bytes)", "Google UL (Bytes)", "Email DL (Bytes)", "Email UL (Bytes)",
         "Netflix DL (Bytes)", "Netflix UL (Bytes)", "Gaming DL (Bytes)", "Gaming UL (Bytes)",
         "Other DL (Bytes)", "Other UL (Bytes)"]]
    app_data["Youtube"] = df["Youtube DL (Bytes)"] + df["Youtube UL (Bytes)"]
    app_data["Social Media"] = df["Social Media DL (Bytes)"] + df["Social Media UL (Bytes)"]
    app_data["Google"] = df["Google DL (Bytes)"] + df["Google UL (Bytes)"]
    app_data["Email"] = df["Email DL (Bytes)"] + df["Email UL (Bytes)"]
    app_data["Netflix"] = df["Netflix DL (Bytes)"] + df["Netflix UL (Bytes)"]
    app_data["Gaming"] = df["Gaming DL (Bytes)"] + df["Gaming UL (Bytes)"]
    app_data["Other"] = df["Other DL (Bytes)"] + df["Other UL (Bytes)"]

    data_per_app = app_data.groupby(["MSISDN/Number"]).agg(Youtube=("Youtube", sum),
                                                           Social_Media=("Social Media", sum),
                                                           Google=("Google", sum),
                                                           Email=("Email", sum),
                                                           Netflix=("Netflix", sum),
                                                           Gaming=("Gaming", sum),
                                                           Other=("Other", sum))

    #User=[i for i in df["MSISDN/Number"].unique()]
    # if type(value) != str:
        # val = value[0]
        # df_filtered= df[df["MSISDN/Number"] == val]
    df_filtered= df[df["MSISDN/Number"] == value]
    app_filtered =  data_per_app[ data_per_app.index == value]
    xDR_Count=df_filtered['Bearer Id'].nunique()
    Duration= df_filtered['Dur. (ms)'].sum()
    Download_Data=df_filtered['Total DL (Bytes)'].sum()
    Upload_Data = df_filtered['Total UL (Bytes)'].sum()
    values=np.array(app_filtered.iloc[0])
    #fig1 = px.pie(app_filtered, values=np.array(app_filtered)[0], names=app_filtered.columns, title='Data Used Per Application')
    fig1 = px.pie(app_filtered, values=values, names=app_filtered.columns, title='Data Used Per Application')


    return dcc.Markdown("**{}**".format(xDR_Count),style={"font-size":"xx-large"}),dcc.Markdown(
        "**{}**".format(Duration),style={"font-size":"xx-large"}),dcc.Markdown(
        "**{}**".format(Download_Data), style={"font-size": "xx-large"}),dcc.Markdown(
        "**{}**".format(Upload_Data),style={"font-size":"xx-large"}),fig1



import pandas as pd
import numpy as np
import datetime
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.tools as tls
import pandas as pd
import plotly.express as px
import numpy as np
import os

import app.static.functions as funcs
from utils import Header

app = dash.Dash()
data=funcs.impute(pd.read_csv("/data/Week1_challenge_data.csv"))

app.layout = html.Div(children=[

    html.H1(children='Univariate Visualizations'),
    html.Div(children='''
        Select a plot:
    '''),
    # this will create a dropdown in the html page, selecting a value here will pass the value to
    # the function called below
        dcc.Dropdown(id='input',
            options = create_options(data),
        value=np.random.choice(data.columns),
        ),
    html.Div(id='output-graph',
        ),
    ])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def return_plot(input_data):
    cat_list = ['Bearer Id', 'Start', 'End', 'IMSI', 'MSISDN/Number', 'IMEI', 'Last Location Name',
                'Handset Manufacturer', 'Handset Type']
    if data[input_data] in cat_list:
        vc = data[input_data.split(':')[0]].value_counts()
        return dcc.Graph(
            id = input_data,
            figure={
            'data' : [go.Bar(
            x=vc.index,
            y=vc.values,
            name = input_data.split(':')[0],
            text = vc.values,
            textposition = "auto",
            )],
            'layout' : {'title':'Distribution plot of {} column'.format(input_data.split(':')[0])}
            })
    if data[input_data] not in cat_list:
        return dcc.Graph(
            id =input_data,
            figure = px.histogram(data, x=input_data,opacity=0.8,
            # color_discrete_sequence=np.random.choice(px.colors.qualitative,1)[0], # choose a random color from the color palate
            title='Histogram of {}'.format(input_data)))


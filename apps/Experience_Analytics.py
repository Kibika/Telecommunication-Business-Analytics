import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table as dt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import pathlib
from app import app

PATH=pathlib.Path(__file__).parent
DATA_PATH=PATH.joinpath("../data").resolve()
df=pd.read_csv(DATA_PATH.joinpath("Week1_challenge_data.csv"))

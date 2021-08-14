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

app = dash.Dash()
data=funcs.impute(pd.read_csv("/data/Week1_challenge_data.csv"))




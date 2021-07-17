import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from app import server
from apps import User_Overview,User_Engagement,Experience_Analytics, Satisfaction_Analysis


# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False),
     html.Div([
         dcc.Link('User Overview|', href='/apps/User_Overview'),
         dcc.Link('User Engagement', href='/apps/User_Engagement'),
         dcc.Link('Experience Analytics', href='/apps/Experience_Analytics'),
         dcc.Link('Satisfaction Analysis', href='/apps/Satisfaction_Analysis'),
     ], className="row"),
     html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == '/apps/User_Overview':
        return User_Overview.layout
    elif pathname == '/apps/Satisfaction_Analysis':
        return Satisfaction_Analysis.layout
    elif pathname == '/apps/User_Engagement':
        return User_Engagement.layout
    elif pathname == "/apps/Experience_Analytics":
        return Experience_analytics.layout
    elif pathname == "/apps/full-view":
        return (
            Experience_Analytics.layout,
            Satisfaction_Analysis.layout,
            User_Engagement.layout,
            User_Overview.layout,
            )
    else:
        return User_Overview.layout


if __name__ == "__main__":
    app.run_server(debug=False)
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dashboard.layouts import (
    EDA,
    Experience_Analytics,
    Satisfaction_Analytics,
    User_Engagement,
    User_Overview,
    )

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "Telecommunication Analytics"
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/Telecom_Analytics/eda":
        return EDA.create_layout(app)
    elif pathname == "/Telecom_Analytics/experience-analytics":
        return Experience_Analytics.create_layout(app)
    elif pathname == "/Telecom_Analytics-report/satisfaction-analysis":
        return Satisfaction_Analytics.create_layout(app)
    elif pathname == "/Telecom_Analytics/user-engagement":
        return User_Engagement.create_layout(app)
    elif pathname == "/Telecom_Analytics/user-overview":
        return User_Overview.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            EDA.create_layout(app),
            Experience_Analytics.create_layout(app),
            Satisfaction_Analytics.create_layout(app),
            User_Engagement.create_layout(app),
            User_Overview.create_layout(app),
            )
    else:
        return User_Overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
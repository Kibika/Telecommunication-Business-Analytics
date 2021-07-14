import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.A(
                        html.Img(
                            src=app.get_asset_url("dash-financial-logo.png"),
                            className="logo",
                        ),
                        href="https://plotly.com/dash",
                    ),
                    html.A(
                        html.Button(
                            "Enterprise Demo",
                            id="learn-more-button",
                            style={"margin-left": "-10px"},
                        ),
                        href="https://plotly.com/get-demo/",
                    ),
                    html.A(
                        html.Button("Source Code", id="learn-more-button"),
                        href="https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-financial-report",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Calibre Financial Index Fund Investor Shares")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/dash-financial-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/Telecom_Analytics-report/eda",
                className="tab first",
            ),
            dcc.Link(
                "Experience Analytics",
                href="/Telecom_Analytics-report/experience-analytics",
                className="tab first",
            ),
            dcc.Link(
                "Satisfaction Analysis", href="/Telecom_Analytics/satisfaction-analysis", className="tab"
            ),
            dcc.Link(
                "User Engagement",
                href="/Telecom_Analytics/user-engagement",
                className="tab",
            ),
            dcc.Link(
                "User Overview",
                href="/Telecom_Analytics/user-overview",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
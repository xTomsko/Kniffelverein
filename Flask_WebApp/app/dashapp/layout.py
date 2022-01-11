from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.io as pio
import pandas as pd


#Dummy vars for display
df = pd.read_json('/Users/tomsparrow/Development/Projects/Kniffelverein/Flask_WebApp/app/dashapp/testdata.json')
figUploads = px.line(df.sort_values(by='Date'), x='Date', y='Sheets', markers=True, line_shape='spline', template='ggplot2')
totalSheets = len('/Users/tomsparrow/Development/Projects/Kniffelverein/Flask_WebApp/app/dashapp/testdata.json')
earliestUpload = "2020-01-18"
Yahtzees = 123432
score = 304


layout = html.Div(id='main', className='row', children=[
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/"))
        ],
        color="primary",
        dark=True,
    ),
    dbc.Col(html.Div(className='Two of three columns', children=[
        html.H1('Statistics'),
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'Past 7 Days', 'value': 7},
                {'label': 'Past 14 Days', 'value': 14},
                {'label': 'Past 30 Days', 'value': 30},
                {'label': 'Last 6 Months', 'value': 180},
                {'label': 'Last Year', 'value': 365}
            ],
            value=7
        ),
        dcc.Graph(figure=figUploads, className='columns')
        ])),

    dbc.Col(html.Div(className='One of three columns', children=[
        html.H1('Column2'),
        dbc.Row(
            [
                dbc.Col(dbc.Card([
                    html.H4('Total sheets uploaded'),
                    html.H1(f'{totalSheets}')
                ])),
                dbc.Col(dbc.Card([
                    html.H4('earliest uploaded'),
                    html.H1(f'{earliestUpload}')
                ])),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card([
                    html.H4('Total Yahtzees'),
                    html.H1(f'{Yahtzees}')
                ])),
                dbc.Col(dbc.Card([
                    html.H4('Total score'),
                    html.H1(f'{score}')
                ])),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card([
                    html.H4('Days played'),
                    html.H1(f'{totalSheets}')
                ])),
                dbc.Col(dbc.Card([
                    html.H4('tbd'),
                    html.H1(f'{totalSheets}')
                ])),
            ]
        )
    ]))
])

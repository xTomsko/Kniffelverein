from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.io as pio
import pandas as pd


df = pd.read_json('/Users/tomsparrow/Development/Projects/Kniffelverein/Flask_WebApp/app/dashapp/testdata.json')
figUploads = px.line(df.sort_values(by='Date'), x='Date', y='Sheets', markers=True, line_shape='spline', template='ggplot2')

# Dummy Layout to get the app running
layout = html.Div(id='main', className='row', children=[
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
        html.H1('Column2')
    ]))
])

from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.io as pio
import pandas as pd

from . import graphs


#Dummy vars for display
df = pd.read_json('app/dashapp/testdata.json')
figUploads = px.line(df.sort_values(by='Date'), x='Date', y='Sheets', markers=True, line_shape='spline', template='ggplot2')
totalSheets = len('app/dashapp/testdata.json')
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
        links_left=True
    ),

    html.H1('Statistics'),

    dbc.Col(html.Div(children=[
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
        graphs.graph_in_tabs
        ],),
    ),

    dbc.Col(html.Div(className='One of three columns', children=[
        html.H1(''),
        dbc.Row(
            [
                dbc.Col(html.Div(dbc.Card([
                    html.H4('Total Sheets'),
                    html.H2(f'{totalSheets}')
                ], className='bg-primary text-white card-layout')), width={"size": 4}),

                dbc.Col(html.Div(dbc.Card([
                    html.H4('First Upload'),
                    html.H2(f'{earliestUpload}')
                ], className='bg-primary text-white card-layout'),), width={"size": 4}),
            ], justify="evenly"
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card([
                    html.H4('Total Yahtzees'),
                    html.H2(f'{Yahtzees}')
                ], className='bg-primary text-white card-layout'), width={"size": 4}),

                dbc.Col(dbc.Card([
                    html.H4('Total Score'),
                    html.H2(f'{3425234}')
                ], className='bg-primary text-white card-layout'), width={"size": 4}),
            ], justify="evenly"
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(dbc.Card([
                    html.H4('Highest Score'),
                    html.H2(f'{345}'),
                ], className='bg-primary text-white card-layout')), width={"size": 4}),

                dbc.Col(html.Div(dbc.Card([
                    html.H4('Averaga Score'),
                    html.H2(f'{260}')
                ], className='bg-primary text-white card-layout')), width={"size": 4}),
            ], justify="evenly"
        )
    ]))
])

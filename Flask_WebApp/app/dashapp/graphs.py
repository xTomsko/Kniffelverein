from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd


df = pd.read_json('/Users/tomsparrow/Development/Projects/Kniffelverein/Flask_WebApp/app/dashapp/testdata.json')

figUploads = px.line(df.sort_values(by='Date'), x='Date', y='Sheets', markers=True, line_shape='spline', template='ggplot2')
figScores = px.line(df.sort_values(by='Date'), x='Date', y='Sheets', markers=True, line_shape='spline', template='ggplot2')
figYathzees = px.line(df.sort_values(by='Date'), x='Date', y='Sheets', markers=True, line_shape='spline', template='ggplot2')

graph_in_tabs = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Uploads', children=[
            dcc.Graph(figure=figUploads, className='columns')
        ]),
        dcc.Tab(label='Scores', children=[
            dcc.Graph(figure=figScores, className='columns')
        ]),
        dcc.Tab(label='Yathzees', children=[
            dcc.Graph(figure=figYathzees, className='columns')
        ]),
    ])
])

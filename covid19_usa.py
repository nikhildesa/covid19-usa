import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go

import dash  
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.read_csv('https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_current.csv')

df = df[['state','positive','recovered','death','fips']]

df.fillna(0, inplace=True)


fig = go.Figure(
    data = go.Choropleth(
        locations = df['state'],
        z = df['positive'],
        locationmode = 'USA-states',
        colorscale = 'matter',
        colorbar_title = 'Postive cases',
        marker_line_color='white',
        
        )
    
    )

fig.update_layout(
    title = '<b>Covid-19 Confirmed cases in USA</b>',
    title_x = 0.5,
  
    geo_scope='usa',
    template='plotly_dark'
)

fig.show()

fig1 = px.bar(df, y='death', x='state', text='death',color='death')
fig1.update_traces(texttemplate='%{text:.2s}',textposition='outside')
fig1.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',template='plotly_dark',title = '<b>Covid-19 Death cases</b>',
    title_x = 0.5)
fig1.show()


fig2 = px.bar(df, y='positive', x='state', text='positive',color = 'positive')
fig2.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig2.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',template='plotly_dark',title = '<b>Covid-19 confirmed cases</b>',
    title_x = 0.5,)
fig2.show()

fig3 = px.bar(df, y='recovered', x='state', text='recovered',color = 'recovered')
fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',template='plotly_dark',title = '<b>Covid-19 Recovered cases</b>',
    title_x = 0.5,)
fig3.show()


app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),
    dcc.Graph(figure=fig),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig1),
            ],className="six columns"),
        html.Div([
            dcc.Graph(figure=fig2),
            ],className = 'six columns'),
        html.Div([
            dcc.Graph(figure=fig3),
            ],className = 'six columns'),
        
        ])
  
])

app.run_server(debug=False) 



























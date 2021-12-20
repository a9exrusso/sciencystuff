import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

from utils import pgn_to_df, get_data

app = dash.Dash(__name__)

# Get the data from the api
username = "Hikamura-Nakaru"
timestamp = "1639554963"
#get_data(username,timestamp)

# Create df from pgn file
df = pgn_to_df("data.pgn")


# Create a layout that contains a graph with two dropdown menues where the user can select the x and y axis
app.layout = html.Div([
    html.H1("Lichess Data Analysis"),
    html.Div([
        html.Div([
            html.H3("Select X-Axis"),
            dcc.Dropdown(
                id="xaxis-column",
                options=[{'label': i, 'value': i} for i in df.columns],
                value='WhiteElo'
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            html.H3("Select Y-Axis"),
            dcc.Dropdown(
                id="yaxis-column",
                options=[{'label': i, 'value': i} for i in df.columns]
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),
    html.Div(id='output-container-button',
             children='Graph will be updated when you press the button.')
])

# Update the graph when the user selects a new x and y axis
@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('xaxis-column', 'value'),
        dash.dependencies.Input('yaxis-column', 'value')])
        


    
if __name__ == '__main__':
    app.run_server(debug=True)
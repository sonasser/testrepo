# Import required packages

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

# Add Dataframe

# Add a bar graph figure

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(
        children='Dashboard',
        style={
            'textAlign': 'center'
        }
    )
    
    # Create dropdown

    # Bar graph
]),

   
    # Create dropdown
    dcc.Dropdown(options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC' # Providing a vallue to dropdown
    )

# Run Application
if __name__ == '__main__':
    app.run_server()
       
    # Create dropdown
    dcc.Dropdown(options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC' # Providing a vallue to dropdown
    )
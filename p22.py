import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Sample demographic data
data = {
    "Year": [2000, 2001, 2002, 2003, 2004] * 6,
    "State": ["Alabama"] * 5 + ["Alaska"] * 5 + ["California"] * 5 + ["Texas"] * 5 + ["New York"] * 5 + ["Florida"] * 5,
    "White": [50, 51, 52, 53, 54] * 6,
    "Black": [20, 21, 22, 23, 24] * 6,
    "Asian": [10, 11, 12, 13, 14] * 6,
    "Indian": [5, 6, 7, 8, 9] * 6,
    "Hawaiian": [1, 1, 2, 2, 3] * 6,
    "Others": [14, 10, 8, 3, 2] * 6,
}

df = pd.DataFrame(data)

# Create the Dash app
app = Dash(__name__)

app.layout = html.Div(style={'padding': '20px'}, children=[
    html.H1("Demographic Population Over Years", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='state-dropdown',
        options=[{'label': state, 'value': state} for state in df['State'].unique()],
        value='Alabama',  # Default value
        multi=False,
        style={'maxHeight': '200px', 'overflowY': 'auto'}
    ),
    html.Div(style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around'}, children=[
        dcc.Graph(id='white-population-graph', style={'flex': '1 1 30%', 'margin': '10px'}),
        dcc.Graph(id='black-population-graph', style={'flex': '1 1 30%', 'margin': '10px'}),
        dcc.Graph(id='asian-population-graph', style={'flex': '1 1 30%', 'margin': '10px'}),
        dcc.Graph(id='indian-population-graph', style={'flex': '1 1 30%', 'margin': '10px'}),
        dcc.Graph(id='hawaiian-population-graph', style={'flex': '1 1 30%', 'margin': '10px'}),
        dcc.Graph(id='others-population-graph', style={'flex': '1 1 30%', 'margin': '10px'}),
    ]),
])

@app.callback(
    Output('white-population-graph', 'figure'),
    Output('black-population-graph', 'figure'),
    Output('asian-population-graph', 'figure'),
    Output('indian-population-graph', 'figure'),
    Output('hawaiian-population-graph', 'figure'),
    Output('others-population-graph', 'figure'),
    Input('state-dropdown', 'value')
)
def update_graphs(selected_state):
    filtered_df = df[df['State'] == selected_state]

    white_fig = px.line(filtered_df, x='Year', y='White', 
                         title='White Population Over Years',
                         hover_data={'Year': True, 'White': True})
    
    black_fig = px.bar(filtered_df, x='Year', y='Black',
                        title='Black Population Over Years',
                        hover_data={'Year': True, 'Black': True})
    
    asian_fig = px.scatter(filtered_df, x='Year', y='Asian',
                            title='Asian Population Over Years',
                            hover_data={'Year': True, 'Asian': True})
    
    indian_fig = px.line(filtered_df, x='Year', y='Indian',
                          title='Indian Population Over Years',
                          hover_data={'Year': True, 'Indian': True})
    
    hawaiian_fig = px.bar(filtered_df, x='Year', y='Hawaiian',
                           title='Hawaiian Population Over Years',
                           hover_data={'Year': True, 'Hawaiian': True})
    
    others_fig = px.line(filtered_df, x='Year', y='Others',
                          title='Others Population Over Years',
                          hover_data={'Year': True, 'Others': True})

    return white_fig, black_fig, asian_fig, indian_fig, hawaiian_fig, others_fig

if __name__ == '__main__':
    app.run_server(debug=True)








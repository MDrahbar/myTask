import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import json
import os

# Load JSON data from a file
def load_data():
    # Replace this with the actual loading mechanism if data.json is not present
   return json.loads('''
[
    {"State": "Alabama", "White": 66.21, "Black": 26.38, "Indian": 0.42, "Asian": 1.39, "Hawaiian": 0.04, "Others": 5.56},
    {"State": "Alaska", "White": 61.3, "Black": 3.18, "Indian": 14.28, "Asian": 6.46, "Hawaiian": 1.53, "Others": 13.24},
    {"State": "Arizona", "White": 66.67, "Black": 4.56, "Indian": 4.15, "Asian": 3.36, "Hawaiian": 0.2, "Others": 21.07},
    {"State": "Arkansas", "White": 72.66, "Black": 15.13, "Indian": 0.56, "Asian": 1.57, "Hawaiian": 0.37, "Others": 9.71},
    {"State": "California", "White": 48.13, "Black": 5.6, "Indian": 1, "Asian": 15.12, "Hawaiian": 0.38, "Others": 29.77},
    {"State": "Colorado", "White": 76.13, "Black": 4.05, "Indian": 0.99, "Asian": 3.21, "Hawaiian": 0.14, "Others": 15.48},
    {"State": "Connecticut", "White": 69.84, "Black": 10.67, "Indian": 0.25, "Asian": 4.73, "Hawaiian": 0.04, "Others": 14.47},
    {"State": "Delaware", "White": 63.83, "Black": 21.97, "Indian": 0.33, "Asian": 4.08, "Hawaiian": 0.04, "Others": 9.75},
    {"State": "District of Columbia", "White": 39.61, "Black": 44.3, "Indian": 0.33, "Asian": 4.04, "Hawaiian": 0.06, "Others": 11.66},
    {"State": "Florida", "White": 63.82, "Black": 15.51, "Indian": 0.27, "Asian": 2.82, "Hawaiian": 0.06, "Others": 17.51},
    {"State": "Georgia", "White": 54.28, "Black": 31.47, "Indian": 0.35, "Asian": 4.34, "Hawaiian": 0.07, "Others": 9.49},
    {"State": "Hawaii", "White": 22.98, "Black": 1.98, "Indian": 0.29, "Asian": 37.16, "Hawaiian": 10.4, "Others": 27.21},
    {"State": "Idaho", "White": 84.94, "Black": 0.69, "Indian": 1.2, "Asian": 1.35, "Hawaiian": 0.15, "Others": 11.67},
    {"State": "Illinois", "White": 65.75, "Black": 13.91, "Indian": 0.44, "Asian": 5.79, "Hawaiian": 0.04, "Others": 14.07},
    {"State": "Indiana", "White": 79.98, "Black": 9.44, "Indian": 0.18, "Asian": 2.49, "Hawaiian": 0.04, "Others": 7.86},
    {"State": "Iowa", "White": 86.85, "Black": 3.78, "Indian": 0.32, "Asian": 2.48, "Hawaiian": 0.14, "Others": 6.43},
    {"State": "Kansas", "White": 79.75, "Black": 5.57, "Indian": 0.75, "Asian": 3.01, "Hawaiian": 0.09, "Others": 10.82},
    {"State": "Kentucky", "White": 84.77, "Black": 8, "Indian": 0.15, "Asian": 1.54, "Hawaiian": 0.08, "Others": 5.46},
    {"State": "Louisiana", "White": 59.45, "Black": 31.56, "Indian": 0.54, "Asian": 1.73, "Hawaiian": 0.05, "Others": 6.67},
    {"State": "Maine", "White": 92.27, "Black": 1.59, "Indian": 0.49, "Asian": 1.1, "Hawaiian": 0.02, "Others": 4.52},
    {"State": "Maryland", "White": 51.19, "Black": 29.89, "Indian": 0.3, "Asian": 6.49, "Hawaiian": 0.05, "Others": 12.08},
    {"State": "Massachusetts", "White": 72.67, "Black": 7.14, "Indian": 0.21, "Asian": 6.98, "Hawaiian": 0.04, "Others": 12.95},
    {"State": "Michigan", "White": 75.73, "Black": 13.56, "Indian": 0.45, "Asian": 3.26, "Hawaiian": 0.03, "Others": 6.97},
    {"State": "Minnesota", "White": 79.67, "Black": 6.71, "Indian": 0.9, "Asian": 5.02, "Hawaiian": 0.04, "Others": 7.66},
    {"State": "Mississippi", "White": 56.95, "Black": 37.24, "Indian": 0.43, "Asian": 0.98, "Hawaiian": 0.04, "Others": 4.36},
    {"State": "Missouri", "White": 79.36, "Black": 11.27, "Indian": 0.29, "Asian": 2.06, "Hawaiian": 0.14, "Others": 6.87},
    {"State": "Montana", "White": 86.44, "Black": 0.55, "Indian": 5.82, "Asian": 0.84, "Hawaiian": 0.06, "Others": 6.28},
    {"State": "Nebraska", "White": 81.84, "Black": 4.78, "Indian": 0.95, "Asian": 2.49, "Hawaiian": 0.07, "Others": 9.87},
    {"State": "Nevada", "White": 55.81, "Black": 9.35, "Indian": 1.31, "Asian": 8.47, "Hawaiian": 0.7, "Others": 24.35},
    {"State": "New Hampshire", "White": 90, "Black": 1.52, "Indian": 0.15, "Asian": 2.63, "Hawaiian": 0.03, "Others": 5.68},
    {"State": "New Jersey", "White": 59.77, "Black": 13.12, "Indian": 0.32, "Asian": 9.88, "Hawaiian": 0.03, "Others": 16.88},
    {"State": "New Mexico", "White": 59.2, "Black": 2.13, "Indian": 9.38, "Asian": 1.63, "Hawaiian": 0.09, "Others": 27.58},
    {"State": "New York", "White": 58.76, "Black": 15.06, "Indian": 0.47, "Asian": 8.84, "Hawaiian": 0.05, "Others": 16.82},
    {"State": "North Carolina", "White": 64.95, "Black": 20.94, "Indian": 1.05, "Asian": 3.11, "Hawaiian": 0.07, "Others": 9.89},
    {"State": "North Dakota", "White": 84.5, "Black": 3.25, "Indian": 4.67, "Asian": 1.61, "Hawaiian": 0.19}
]
''')


data = load_data()
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(children=[
    html.H1("U.S. Demographics Dashboard", className='dashboard-title'),
    dcc.Dropdown(
        id='state-dropdown',
        options=[{'label': state, 'value': state} for state in df['State'].unique()],
        value='Alabama',
        clearable=False,
        className='dropdown'
    ),
    html.Div(style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around'}, children=[
        html.Div(className='card', children=[
            dcc.Graph(id='demographics-bar-graph', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[
            dcc.Graph(id='demographics-pie-chart', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[
            dcc.Graph(id='demographics-scatter-plot', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[
            dcc.Graph(id='demographics-line-plot', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[
            dcc.Graph(id='demographics-box-plot', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[
            dcc.Graph(id='demographics-histogram', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'}),
    ])
])

# Update the graphs based on selected state
@app.callback(
    Output('demographics-bar-graph', 'figure'),
    Output('demographics-pie-chart', 'figure'),
    Output('demographics-scatter-plot', 'figure'),
    Output('demographics-line-plot', 'figure'),
    Output('demographics-box-plot', 'figure'),
    Output('demographics-histogram', 'figure'),
    Input('state-dropdown', 'value')
)
def update_graphs(selected_state):
    filtered_df = df[df['State'] == selected_state].iloc[0]

    # Bar graph
    bar_fig = px.bar(
        x=filtered_df.index[1:],  # Skip 'State' for x-axis
        y=filtered_df.values[1:],  # Skip 'State' for y values
        labels={'x': 'Demographic Group', 'y': 'Percentage'},
        title=f'Demographic Distribution in {selected_state}',
        template='plotly_dark'
    )

    # Pie chart
    pie_fig = px.pie(
        names=filtered_df.index[1:],
        values=filtered_df.values[1:],
        title=f'Demographic Distribution in {selected_state}',
        template='plotly_dark'
    )

    # Scatter plot
    scatter_fig = px.scatter(
        df, x='State', y='White', size='White', color='Black',
        title='Scatter Plot of White vs. Black Population',
        hover_name='State', template='plotly_dark'
    )

    # Line plot
    line_fig = px.line(
        df, x='State', y='White',
        title='Line Plot of White Population by State',
        template='plotly_dark'
    )

    # Box plot
    box_fig = px.box(
        df, y='Black',
        title='Box Plot of Black Population Distribution',
        template='plotly_dark'
    )

    # Histogram
    histogram_fig = px.histogram(
        df, x='Others',
        title='Histogram of Others Population Distribution',
        template='plotly_dark'
    )

    return bar_fig, pie_fig, scatter_fig, line_fig, box_fig, histogram_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

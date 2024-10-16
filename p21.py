import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import json
import os

# Load JSON data from a file
def load_data():
    with open(os.path.join('data.json')) as f:
        return json.load(f)

data = load_data()
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__, assets_folder='assets')

# App layout
app.layout = html.Div(children=[
    html.H1("Sales Dashboard of PTG", className='dashboard-title'),
    dcc.Dropdown(
        id='product-dropdown',
        options=[{'label': product, 'value': product} for product in df['Product'].unique()],
        value='Laptop',  # Default value
        clearable=False,
        className='dropdown'
    ),
    html.Div(style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around'}, children=[
        html.Div(className='card', children=[
            dcc.Graph(id='sales-bar-graph', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[
            dcc.Graph(id='sales-line-graph', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[
            dcc.Graph(id='sales-pie-chart', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[
            dcc.Graph(id='sales-scatter-plot', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[
            dcc.Graph(id='sales-box-plot', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[
            dcc.Graph(id='sales-histogram', style={'height': '300px'})
        ], style={'width': '45%', 'margin': '20px'})
    ])
])

# Define callbacks to update graphs
@app.callback(Output('sales-bar-graph', 'figure'), Input('product-dropdown', 'value'))
def update_bar_graph(selected_product):
    filtered_df = df[df['Product'] == selected_product]
    fig = px.bar(filtered_df, x='Date', y='Sales', color='Region',
                  title=f'Sales Over Time for {selected_product}',
                  labels={'Sales': 'Sales Amount', 'Date': 'Date'},
                  template='plotly_dark')
    return fig

@app.callback(Output('sales-line-graph', 'figure'), Input('product-dropdown', 'value'))
def update_line_graph(selected_product):
    filtered_df = df[df['Product'] == selected_product]
    fig = px.line(filtered_df, x='Date', y='Sales', color='Region',
                   title=f'Sales Trend for {selected_product}',
                   labels={'Sales': 'Sales Amount', 'Date': 'Date'},
                   template='plotly_dark')
    return fig

@app.callback(Output('sales-pie-chart', 'figure'), Input('product-dropdown', 'value'))
def update_pie_chart(selected_product):
    filtered_df = df[df['Product'] == selected_product]
    fig = px.pie(filtered_df, values='Sales', names='Region',
                  title=f'Sales Distribution for {selected_product}',
                  template='plotly_dark')
    return fig

@app.callback(Output('sales-scatter-plot', 'figure'), Input('product-dropdown', 'value'))
def update_scatter_plot(selected_product):
    filtered_df = df[df['Product'] == selected_product]
    fig = px.scatter(filtered_df, x='Quantity Sold', y='Sales', color='Region',
                     title=f'Sales vs Quantity Sold for {selected_product}',
                     labels={'Sales': 'Sales Amount', 'Quantity Sold': 'Quantity'},
                     template='plotly_dark')
    return fig

@app.callback(Output('sales-box-plot', 'figure'), Input('product-dropdown', 'value'))
def update_box_plot(selected_product):
    filtered_df = df[df['Product'] == selected_product]
    fig = px.box(filtered_df, x='Region', y='Sales',
                  title=f'Sales Box Plot for {selected_product}',
                  labels={'Sales': 'Sales Amount', 'Region': 'Region'},
                  template='plotly_dark')
    return fig

@app.callback(Output('sales-histogram', 'figure'), Input('product-dropdown', 'value'))
def update_histogram(selected_product):
    filtered_df = df[df['Product'] == selected_product]
    fig = px.histogram(filtered_df, x='Sales', color='Region',
                       title=f'Sales Histogram for {selected_product}',
                       labels={'Sales': 'Sales Amount'},
                       template='plotly_dark')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

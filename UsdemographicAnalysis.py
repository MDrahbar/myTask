# from dash import Dash, dcc, html

# app = Dash(__name__)

# app.layout = html.Div([
#     dcc.Slider(0, 9, marks={i: f'Label{i}' for i in range(10)}, value=0)
# ])

# if __name__ == '__main__':
#     app.run(debug=True)


# for checklist 
# from dash import Dash, dcc, html

# app = Dash(__name__)

# app.layout = html.Div([
#     dcc.Checklist( 
#         ['New York City', 'Montréal', 'San Francisco'],
#         ['Montréal', 'San Francisco'],
#     )
# ])

# if __name__ == '__main__':
#     app.run(debug=True)


# from dash import Dash, dcc, html

# app = Dash(__name__)

# app.layout = html.Div([
#     dcc.Checklist( 
#         ['New York City', 'Montréal', 'San Francisco'],
#         ['Montréal', 'San Francisco'],
#         inline=True   # to show checklist items in a row
#     )
# ])

# if __name__ == '__main__':
#     app.run(debug=True)


import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Your demographic data
data = [
    {
        "State": "Alabama",
        "White (%)": 65.0,
        "Black (%)": 27.0,
        "Indian (%)": 1.0,
        "Asian (%)": 2.0,
        "Hawaiian (%)": 0.2,
        "Others (%)": 4.8,
        "Total Population": 5024279,
        "Female Population (%)": 50.0,
        "Literacy Rate (%)": 87.5,
        "Crime Rate (per 100k)": 636.1,
        "Year": 2024,
        "Schools": 13500,
        "Mobile Phone Users": 4600000,
        "Employees": 2500000,
        "Students": 800000,
        "Men Age 50+": 800000,
        "Women Age 50+": 700000
    },
    {
        "State": "Alaska",
        "White (%)": 66.5,
        "Black (%)": 3.9,
        "Indian (%)": 15.0,
        "Asian (%)": 5.7,
        "Hawaiian (%)": 1.0,
        "Others (%)": 7.9,
        "Total Population": 733391,
        "Female Population (%)": 49.5,
        "Literacy Rate (%)": 91.0,
        "Crime Rate (per 100k)": 837.8,
        "Year": 2024,
        "Schools": 500,
        "Mobile Phone Users": 600000,
        "Employees": 300000,
        "Students": 120000,
        "Men Age 50+": 50000,
        "Women Age 50+": 40000
    },
    {
        "State": "Arizona",
        "White (%)": 54.5,
        "Black (%)": 5.8,
        "Indian (%)": 4.3,
        "Asian (%)": 3.8,
        "Hawaiian (%)": 0.5,
        "Others (%)": 31.1,
        "Total Population": 7158024,
        "Female Population (%)": 50.2,
        "Literacy Rate (%)": 87.5,
        "Crime Rate (per 100k)": 419.0,
        "Year": 2024,
        "Schools": 5000,
        "Mobile Phone Users": 6000000,
        "Employees": 3700000,
        "Students": 1500000,
        "Men Age 50+": 800000,
        "Women Age 50+": 600000
    },
    {
        "State": "Arkansas",
        "White (%)": 71.0,
        "Black (%)": 15.6,
        "Indian (%)": 1.0,
        "Asian (%)": 1.6,
        "Hawaiian (%)": 0.2,
        "Others (%)": 11.6,
        "Total Population": 3011524,
        "Female Population (%)": 50.3,
        "Literacy Rate (%)": 86.8,
        "Crime Rate (per 100k)": 743.5,
        "Year": 2024,
        "Schools": 1300,
        "Mobile Phone Users": 2600000,
        "Employees": 1500000,
        "Students": 350000,
        "Men Age 50+": 300000,
        "Women Age 50+": 250000
    },
    {
        "State": "California",
        "White (%)": 36.6,
        "Black (%)": 6.5,
        "Indian (%)": 1.7,
        "Asian (%)": 15.5,
        "Hawaiian (%)": 0.4,
        "Others (%)": 39.3,
        "Total Population": 39538223,
        "Female Population (%)": 50.3,
        "Literacy Rate (%)": 85.5,
        "Crime Rate (per 100k)": 2832.4,
        "Year": 2024,
        "Schools": 10000,
        "Mobile Phone Users": 32000000,
        "Employees": 19000000,
        "Students": 4500000,
        "Men Age 50+": 5000000,
        "Women Age 50+": 4700000
    },
    {
        "State": "Colorado",
        "White (%)": 67.0,
        "Black (%)": 4.6,
        "Indian (%)": 1.0,
        "Asian (%)": 3.5,
        "Hawaiian (%)": 0.2,
        "Others (%)": 23.7,
        "Total Population": 5773714,
        "Female Population (%)": 50.2,
        "Literacy Rate (%)": 92.5,
        "Crime Rate (per 100k)": 385.6,
        "Year": 2024,
        "Schools": 2000,
        "Mobile Phone Users": 4600000,
        "Employees": 3500000,
        "Students": 800000,
        "Men Age 50+": 600000,
        "Women Age 50+": 500000
    },
    {
        "State": "Connecticut",
        "White (%)": 65.3,
        "Black (%)": 10.6,
        "Indian (%)": 0.5,
        "Asian (%)": 5.2,
        "Hawaiian (%)": 0.1,
        "Others (%)": 18.3,
        "Total Population": 3605944,
        "Female Population (%)": 50.8,
        "Literacy Rate (%)": 89.6,
        "Crime Rate (per 100k)": 1575.8,
        "Year": 2024,
        "Schools": 1500,
        "Mobile Phone Users": 3300000,
        "Employees": 1800000,
        "Students": 500000,
        "Men Age 50+": 600000,
        "Women Age 50+": 500000
    },
    {
        "State": "Delaware",
        "White (%)": 61.0,
        "Black (%)": 23.0,
        "Indian (%)": 1.0,
        "Asian (%)": 5.0,
        "Hawaiian (%)": 0.3,
        "Others (%)": 10.7,
        "Total Population": 989948,
        "Female Population (%)": 50.5,
        "Literacy Rate (%)": 89.4,
        "Crime Rate (per 100k)": 2087.4,
        "Year": 2024,
        "Schools": 500,
        "Mobile Phone Users": 800000,
        "Employees": 500000,
        "Students": 150000,
        "Men Age 50+": 200000,
        "Women Age 50+": 150000
    },
    {
        "State": "Florida",
        "White (%)": 53.3,
        "Black (%)": 16.9,
        "Indian (%)": 0.5,
        "Asian (%)": 2.7,
        "Hawaiian (%)": 0.1,
        "Others (%)": 26.5,
        "Total Population": 21538187,
        "Female Population (%)": 51.1,
        "Literacy Rate (%)": 86.9,
        "Crime Rate (per 100k)": 2588.3,
        "Year": 2024,
        "Schools": 4000,
        "Mobile Phone Users": 22000000,
        "Employees": 11000000,
        "Students": 3500000,
        "Men Age 50+": 4500000,
        "Women Age 50+": 4200000
    },
    {
        "State": "Georgia",
        "White (%)": 58.0,
        "Black (%)": 32.6,
        "Indian (%)": 0.4,
        "Asian (%)": 4.0,
        "Hawaiian (%)": 0.1,
        "Others (%)": 5.3,
        "Total Population": 10711908,
        "Female Population (%)": 50.6,
        "Literacy Rate (%)": 87.7,
        "Crime Rate (per 100k)": 383.0,
        "Year": 2024,
        "Schools": 3000,
        "Mobile Phone Users": 8000000,
        "Employees": 5000000,
        "Students": 1300000,
        "Men Age 50+": 1000000,
        "Women Age 50+": 900000
    },
    {
        "State": "Hawaii",
        "White (%)": 25.6,
        "Black (%)": 1.7,
        "Indian (%)": 0.2,
        "Asian (%)": 39.3,
        "Hawaiian (%)": 10.2,
        "Others (%)": 23.0,
        "Total Population": 1455281,
        "Female Population (%)": 50.8,
        "Literacy Rate (%)": 90.0,
        "Crime Rate (per 100k)": 446.6,
        "Year": 2024,
        "Schools": 800,
        "Mobile Phone Users": 1300000,
        "Employees": 650000,
        "Students": 200000,
        "Men Age 50+": 200000,
        "Women Age 50+": 200000
    },
    {
        "State": "Idaho",
        "White (%)": 85.0,
        "Black (%)": 1.0,
        "Indian (%)": 1.0,
        "Asian (%)": 3.0,
        "Hawaiian (%)": 0.2,
        "Others (%)": 10.8,
        "Total Population": 1869118,
        "Female Population (%)": 49.7,
        "Literacy Rate (%)": 95.0,
        "Crime Rate (per 100k)": 275.5,
        "Year": 2024,
        "Schools": 700,
        "Mobile Phone Users": 1400000,
        "Employees": 800000,
        "Students": 350000,
        "Men Age 50+": 300000,
        "Women Age 50+": 250000
    },
    {
        "State": "Illinois",
        "White (%)": 61.6,
        "Black (%)": 14.6,
        "Indian (%)": 0.3,
        "Asian (%)": 5.7,
        "Hawaiian (%)": 0.1,
        "Others (%)": 17.7,
        "Total Population": 12812508,
        "Female Population (%)": 50.8,
        "Literacy Rate (%)": 88.4,
        "Crime Rate (per 100k)": 3174.1,
        "Year": 2024,
        "Schools": 4000,
        "Mobile Phone Users": 11000000,
        "Employees": 6000000,
        "Students": 2500000,
        "Men Age 50+": 1500000,
        "Women Age 50+": 1400000
    },
    {
        "State": "Indiana",
        "White (%)": 78.0,
        "Black (%)": 9.5,
        "Indian (%)": 0.8,
        "Asian (%)": 2.4,
        "Hawaiian (%)": 0.1,
        "Others (%)": 9.2,
        "Total Population": 11351039,
        "Female Population (%)": 50.7,
        "Literacy Rate (%)": 87.4,
        "Crime Rate (per 100k)": 284.4,
        "Year": 2024,
        "Schools": 3000,
        "Mobile Phone Users": 8500000,
        "Employees": 5000000,
        "Students": 1200000,
        "Men Age 50+": 900000,
        "Women Age 50+": 800000
    },
    {
        "State": "Iowa",
        "White (%)": 84.0,
        "Black (%)": 4.0,
        "Indian (%)": 2.1,
        "Asian (%)": 2.5,
        "Hawaiian (%)": 0.1,
        "Others (%)": 7.3,
        "Total Population": 3190369,
        "Female Population (%)": 50.4,
        "Literacy Rate (%)": 92.0,
        "Crime Rate (per 100k)": 304.0,
        "Year": 2024,
        "Schools": 2000,
        "Mobile Phone Users": 3000000,
        "Employees": 1800000,
        "Students": 500000,
        "Men Age 50+": 600000,
        "Women Age 50+": 550000
    },
    {
        "State": "Kansas",
        "White (%)": 76.0,
        "Black (%)": 6.1,
        "Indian (%)": 1.0,
        "Asian (%)": 2.8,
        "Hawaiian (%)": 0.2,
        "Others (%)": 14.0,
        "Total Population": 2913314,
        "Female Population (%)": 50.5,
        "Literacy Rate (%)": 91.5,
        "Crime Rate (per 100k)": 340.7,
        "Year": 2024,
        "Schools": 2000,
        "Mobile Phone Users": 2700000,
        "Employees": 1500000,
        "Students": 600000,
        "Men Age 50+": 500000,
        "Women Age 50+": 400000
    },
    {
        "State": "Kentucky",
        "White (%)": 84.0,
        "Black (%)": 8.4,
        "Indian (%)": 1.0,
        "Asian (%)": 1.8,
        "Hawaiian (%)": 0.2,
        "Others (%)": 4.6,
        "Total Population": 4505836,
        "Female Population (%)": 51.1,
        "Literacy Rate (%)": 86.0,
        "Crime Rate (per 100k)": 473.4,
        "Year": 2024,
        "Schools": 2000,
        "Mobile Phone Users": 3500000,
        "Employees": 1800000,
        "Students": 600000,
        "Men Age 50+": 700000,
        "Women Age 50+": 600000
    },
    {
        "State": "Louisiana",
        "White (%)": 61.0,
        "Black (%)": 32.0,
        "Indian (%)": 1.1,
        "Asian (%)": 2.5,
        "Hawaiian (%)": 0.1,
        "Others (%)": 3.3,
        "Total Population": 4657757,
        "Female Population (%)": 51.2,
        "Literacy Rate (%)": 85.5,
        "Crime Rate (per 100k)": 1341.8,
        "Year": 2024,
        "Schools": 2200,
        "Mobile Phone Users": 4000000,
        "Employees": 2300000,
        "Students": 700000,
        "Men Age 50+": 600000,
        "Women Age 50+": 500000
    },
    {
        "State": "Maine",
        "White (%)": 90.2,
        "Black (%)": 1.5,
        "Indian (%)": 1.3,
        "Asian (%)": 2.5,
        "Hawaiian (%)": 0.1,
        "Others (%)": 4.4,
        "Total Population": 1362359,
        "Female Population (%)": 51.4,
        "Literacy Rate (%)": 90.8,
        "Crime Rate (per 100k)": 272.1,
        "Year": 2024,
        "Schools": 700,
        "Mobile Phone Users": 800000,
        "Employees": 600000,
        "Students": 150000,
        "Men Age 50+": 300000,
        "Women Age 50+": 300000
    },
    {
        "State": "Maryland",
        "White (%)": 59.0,
        "Black (%)": 31.1,
        "Indian (%)": 0.4,
        "Asian (%)": 6.8,
        "Hawaiian (%)": 0.1,
        "Others (%)": 3.1,
        "Total Population": 6177224,
        "Female Population (%)": 50.5,
        "Literacy Rate (%)": 88.9,
        "Crime Rate (per 100k)": 2056.9,
        "Year": 2024,
        "Schools": 1400,
        "Mobile Phone Users": 5000000,
        "Employees": 3000000,
        "Students": 800000,
        "Men Age 50+": 800000,
        "Women Age 50+": 700000
    },
    {
        "State": "Massachusetts",
        "White (%)": 70.4,
        "Black (%)": 8.8,
        "Indian (%)": 0.4,
        "Asian (%)": 7.7,
        "Hawaiian (%)": 0.2,
        "Others (%)": 12.5,
        "Total Population": 7029917,
        "Female Population (%)": 51.0,
        "Literacy Rate (%)": 90.4,
        "Crime Rate (per 100k)": 687.4,
        "Year": 2024,
        "Schools": 2500,
        "Mobile Phone Users": 6000000,
        "Employees": 4000000,
        "Students": 900000,
        "Men Age 50+": 1000000,
        "Women Age 50+": 900000
    },
    {
        "State": "Michigan",
        "White (%)": 74.8,
        "Black (%)": 14.0,
        "Indian (%)": 1.3,
        "Asian (%)": 3.2,
        "Hawaiian (%)": 0.3,
        "Others (%)": 6.4,
        "Total Population": 10077331,
        "Female Population (%)": 50.7,
        "Literacy Rate (%)": 89.2,
        "Crime Rate (per 100k)": 578.0,
        "Year": 2024,
        "Schools": 4000,
        "Mobile Phone Users": 8000000,
        "Employees": 4800000,
        "Students": 1200000,
        "Men Age 50+": 1200000,
        "Women Age 50+": 1000000
    },
    {
        "State": "Minnesota",
        "White (%)": 78.0,
        "Black (%)": 7.2,
        "Indian (%)": 1.0,
        "Asian (%)": 5.1,
        "Hawaiian (%)": 0.1,
        "Others (%)": 8.6,
        "Total Population": 5706494,
        "Female Population (%)": 50.4,
        "Literacy Rate (%)": 92.3,
        "Crime Rate (per 100k)": 268.4,
        "Year": 2024,
        "Schools": 3000,
        "Mobile Phone Users": 5000000,
        "Employees": 3000000,
        "Students": 800000,
        "Men Age 50+": 700000,
        "Women Age 50+": 600000
    },
    {
        "State": "Mississippi",
        "White (%)": 58.0,
        "Black (%)": 37.5,
        "Indian (%)": 0.4,
        "Asian (%)": 1.2,
        "Hawaiian (%)": 0.1,
        "Others (%)": 3.8,
        "Total Population": 2961279,
        "Female Population (%)": 51.4,
        "Literacy Rate (%)": 85.0,
        "Crime Rate (per 100k)": 730.8,
        "Year": 2024,
        "Schools": 1500,
        "Mobile Phone Users": 1300000,
        "Employees": 800000,
        "Students": 400000,
        "Men Age 50+": 300000,
        "Women Age 50+": 250000
    },
    {
        "State": "Missouri",
        "White (%)": 80.0,
        "Black (%)": 11.7,
        "Indian (%)": 0.5,
        "Asian (%)": 2.5,
        "Hawaiian (%)": 0.1,
        "Others (%)": 5.2,
        "Total Population": 6154913,
        "Female Population (%)": 50.6,
        "Literacy Rate (%)": 88.4,
        "Crime Rate (per 100k)": 431.5,
        "Year": 2024,
        "Schools": 3000,
        "Mobile Phone Users": 5000000,
        "Employees": 3500000,
        "Students": 800000,
        "Men Age 50+": 700000,
        "Women Age 50+": 600000
    },
    {
        "State": "Montana",
        "White (%)": 86.0,
        "Black (%)": 0.5,
        "Indian (%)": 6.5,
        "Asian (%)": 1.4,
        "Hawaiian (%)": 0.2,
        "Others (%)": 5.4,
        "Total Population": 1084225,
        "Female Population (%)": 50.3,
        "Literacy Rate (%)": 91.0,
        "Crime Rate (per 100k)": 394.0,
        "Year": 2024,
        "Schools": 800,
        "Mobile Phone Users": 700000,
        "Employees": 500000,
        "Students": 200000,
        "Men Age 50+": 200000,
        "Women Age 50+": 150000
    },
    {
        "State": "Nebraska",
        "White (%)": 79.0,
        "Black (%)": 5.6,
        "Indian (%)": 1.0,
        "Asian (%)": 3.5,
        "Hawaiian (%)": 0.2,
        "Others (%)": 10.7,
        "Total Population": 1961504,
        "Female Population (%)": 50.5,
        "Literacy Rate (%)": 93.0,
        "Crime Rate (per 100k)": 323.5,
        "Year": 2024,
        "Schools": 1000,
        "Mobile Phone Users": 1200000,
        "Employees": 800000,
        "Students": 400000,
        "Men Age 50+": 400000,
        "Women Age 50+": 300000
    },
    {
        "State": "Nevada",
        "White (%)": 48.0,
        "Black (%)": 9.1,
        "Indian (%)": 1.2,
        "Asian (%)": 11.2,
        "Hawaiian (%)": 1.0,
        "Others (%)": 29.5,
        "Total Population": 3104614,
        "Female Population (%)": 50.2,
        "Literacy Rate (%)": 87.0,
        "Crime Rate (per 100k)": 523.5,
        "Year": 2024,
        "Schools": 1000,
        "Mobile Phone Users": 2200000,
        "Employees": 1300000,
        "Students": 600000,
        "Men Age 50+": 400000,
        "Women Age 50+": 300000
    },
    {
        "State": "New Hampshire",
        "White (%)": 90.5,
        "Black (%)": 1.2,
        "Indian (%)": 0.8,
        "Asian (%)": 3.1,
        "Hawaiian (%)": 0.1,
        "Others (%)": 4.3,
        "Total Population": 1377529,
        "Female Population (%)": 50.3,
        "Literacy Rate (%)": 93.2,
        "Crime Rate (per 100k)": 253.0,
        "Year": 2024,
        "Schools": 500,
        "Mobile Phone Users": 1000000,
        "Employees": 700000,
        "Students": 200000,
        "Men Age 50+": 200000,
        "Women Age 50+": 200000
    },
    {
        "State": "New Jersey",
        "White (%)": 55.8,
        "Black (%)": 14.2,
        "Indian (%)": 0.4,
        "Asian (%)": 10.1,
        "Hawaiian (%)": 0.1,
        "Others (%)": 19.4,
        "Total Population": 9288994,
        "Female Population (%)": 51.0,
        "Literacy Rate (%)": 89.5,
        "Crime Rate (per 100k)": 1848.1,
        "Year": 2024,
        "Schools": 2500,
        "Mobile Phone Users": 7500000,
        "Employees": 5000000,
        "Students": 1200000,
        "Men Age 50+": 800000,
        "Women Age 50+": 700000
    },
    {
        "State": "New Mexico",
        "White (%)": 47.7,
        "Black (%)": 2.1,
        "Indian (%)": 10.0,
        "Asian (%)": 1.7,
        "Hawaiian (%)": 0.3,
        "Others (%)": 38.2,
        "Total Population": 2117522,
        "Female Population (%)": 50.5,
        "Literacy Rate (%)": 86.7,
        "Crime Rate (per 100k)": 960.0,
        "Year": 2024,
        "Schools": 1500,
        "Mobile Phone Users": 1400000,
        "Employees": 900000,
        "Students": 350000,
        "Men Age 50+": 300000,
        "Women Age 50+": 250000
    },
    {
        "State": "New York",
        "White (%)": 57.0,
        "Black (%)": 14.6,
        "Indian (%)": 0.4,
        "Asian (%)": 10.2,
        "Hawaiian (%)": 0.1,
        "Others (%)": 17.7,
        "Total Population": 20201249,
        "Female Population (%)": 51.0,
        "Literacy Rate (%)": 87.0,
        "Crime Rate (per 100k)": 733.6,
        "Year": 2024,
        "Schools": 6000,
        "Mobile Phone Users": 12000000,
        "Employees": 8000000,
        "Students": 3000000,
        "Men Age 50+": 3000000,
        "Women Age 50+": 2500000
    },
    {
        "State": "North Carolina",
        "White (%)": 61.0,
        "Black (%)": 22.5,
        "Indian (%)": 1.6,
        "Asian (%)": 3.3,
        "Hawaiian (%)": 0.2,
        "Others (%)": 11.4,
        "Total Population": 10418421,
        "Female Population (%)": 51.0,
        "Literacy Rate (%)": 89.1,
        "Crime Rate (per 100k)": 252.2,
        "Year": 2024,
        "Schools": 3000,
        "Mobile Phone Users": 6500000,
        "Employees": 6000000,
        "Students": 1800000,
        "Men Age 50+": 1100000,
        "Women Age 50+": 1000000
    },
    {
        "State": "North Dakota",
        "White (%)": 83.0,
        "Black (%)": 2.1,
        "Indian (%)": 7.0,
        "Asian (%)": 1.5,
        "Hawaiian (%)": 0.2,
        "Others (%)": 6.2,
        "Total Population": 770588,
        "Female Population (%)": 50.4,
        "Literacy Rate (%)": 94.5,
        "Crime Rate (per 100k)": 246.7,
        "Year": 2024,
        "Schools": 500,
        "Mobile Phone Users": 500000,
        "Employees": 300000,
        "Students": 200000,
        "Men Age 50+": 100000,
        "Women Age 50+": 90000
    },
    {
        "State": "Ohio",
        "White (%)": 78.5,
        "Black (%)": 12.4,
        "Indian (%)": 0.2,
        "Asian (%)": 2.9,
        "Hawaiian (%)": 0.1,
        "Others (%)": 6.9,
        "Total Population": 11698441,
        "Female Population (%)": 51.1,
        "Literacy Rate (%)": 87.3,
        "Crime Rate (per 100k)": 253.8,
        "Year": 2024,
        "Schools": 4000,
        "Mobile Phone Users": 9000000,
        "Employees": 5000000,
        "Students": 1500000,
        "Men Age 50+": 1200000,
        "Women Age 50+": 1100000
    },
    {
        "State": "Oklahoma",
        "White (%)": 70.0,
        "Black (%)": 9.1,
        "Indian (%)": 5.5,
        "Asian (%)": 2.6,
        "Hawaiian (%)": 0.3,
        "Others (%)": 12.5,
        "Total Population": 3999203,
        "Female Population (%)": 50.6,
        "Literacy Rate (%)": 88.8,
        "Crime Rate (per 100k)": 386.4,
        "Year": 2024,
        "Schools": 3000,
        "Mobile Phone Users": 3000000,
        "Employees": 1700000,
        "Students": 800000,
        "Men Age 50+": 600000,
        "Women Age 50+": 500000
    },
    {
        "State": "Oregon",
        "White (%)": 76.0,
        "Black (%)": 2.0,
        "Indian (%)": 1.7,
        "Asian (%)": 6.1,
        "Hawaiian (%)": 0.2,
        "Others (%)": 13.9,
        "Total Population": 4302080,
        "Female Population (%)": 50.5,
        "Literacy Rate (%)": 89.4,
        "Crime Rate (per 100k)": 354.4,
        "Year": 2024,
        "Schools": 2000,
        "Mobile Phone Users": 5000000,
        "Employees": 2500000,
        "Students": 900000,
        "Men Age 50+": 700000,
        "Women Age 50+": 600000
    },
    {
        "State": "Pennsylvania",
        "White (%)": 76.3,
        "Black (%)": 12.7,
        "Indian (%)": 0.3,
        "Asian (%)": 5.0,
        "Hawaiian (%)": 0.1,
        "Others (%)": 5.6,
        "Total Population": 13080049,
        "Female Population (%)": 51.0,
        "Literacy Rate (%)": 88.7,
        "Crime Rate (per 100k)": 264.1,
        "Year": 2024,
        "Schools": 4000,
        "Mobile Phone Users": 10000000,
        "Employees": 6000000,
        "Students": 2000000,
        "Men Age 50+": 1300000,
        "Women Age 50+": 1200000
    },
    {
        "State": "Rhode Island",
        "White (%)": 71.3,
        "Black (%)": 12.5,
        "Indian (%)": 0.5,
        "Asian (%)": 5.0,
        "Hawaiian (%)": 0.3,
        "Others (%)": 10.4,
        "Total Population": 1095904,
        "Female Population (%)": 51.2,
        "Literacy Rate (%)": 87.5,
        "Crime Rate (per 100k)": 507.6,
        "Year": 2024,
        "Schools": 500,
        "Mobile Phone Users": 700000,
        "Employees": 500000,
        "Students": 150000,
        "Men Age 50+": 200000,
        "Women Age 50+": 150000
    },
    {
        "State": "South Carolina",
        "White (%)": 62.0,
        "Black (%)": 27.5,
        "Indian (%)": 1.0,
        "Asian (%)": 2.4,
        "Hawaiian (%)": 0.1,
        "Others (%)": 7.0,
        "Total Population": 5344631,
        "Female Population (%)": 51.0,
        "Literacy Rate (%)": 86.4,
        "Crime Rate (per 100k)": 368.1,
        "Year": 2024,
        "Schools": 2500,
        "Mobile Phone Users": 4000000,
        "Employees": 2000000,
        "Students": 800000,
        "Men Age 50+": 600000,
        "Women Age 50+": 500000
    },
    {
        "State": "South Dakota",
        "White (%)": 86.0,
        "Black (%)": 2.4,
        "Indian (%)": 8.9,
        "Asian (%)": 1.4,
        "Hawaiian (%)": 0.2,
        "Others (%)": 1.1,
        "Total Population": 909594,
        "Female Population (%)": 50.4,
        "Literacy Rate (%)": 93.0,
        "Crime Rate (per 100k)": 374.3,
        "Year": 2024,
        "Schools": 500,
        "Mobile Phone Users": 500000,
        "Employees": 200000,
        "Students": 200000,
        "Men Age 50+": 100000,
        "Women Age 50+": 90000
    },
    {
        "State": "Tennessee",
        "White (%)": 75.0,
        "Black (%)": 17.6,
        "Indian (%)": 1.1,
        "Asian (%)": 2.6,
        "Hawaiian (%)": 0.1,
        "Others (%)": 3.6,
        "Total Population": 6829229,
        "Female Population (%)": 51.1,
        "Literacy Rate (%)": 87.5,
        "Crime Rate (per 100k)": 471.1,
        "Year": 2024,
        "Schools": 3000,
        "Mobile Phone Users": 4000000,
        "Employees": 3200000,
        "Students": 900000,
        "Men Age 50+": 800000,
        "Women Age 50+": 700000
    },
    {
        "State": "Texas",
        "White (%)": 45.3,
        "Black (%)": 12.4,
        "Indian (%)": 0.7,
        "Asian (%)": 5.7,
        "Hawaiian (%)": 0.2,
        "Others (%)": 36.6,
        "Total Population": 30918594,
        "Female Population (%)": 50.4,
        "Literacy Rate (%)": 89.5,
        "Crime Rate (per 100k)": 442.2,
        "Year": 2024,
        "Schools": 5000,
        "Mobile Phone Users": 19000000,
        "Employees": 13000000,
        "Students": 5000000,
        "Men Age 50+": 2500000,
        "Women Age 50+": 2400000
    },
    {
        "State": "Utah",
        "White (%)": 78.5,
        "Black (%)": 1.5,
        "Indian (%)": 1.2,
        "Asian (%)": 3.7,
        "Hawaiian (%)": 0.4,
        "Others (%)": 14.7,
        "Total Population": 3261952,
        "Female Population (%)": 49.5,
        "Literacy Rate (%)": 93.0,
        "Crime Rate (per 100k)": 217.5,
        "Year": 2024,
        "Schools": 1000,
        "Mobile Phone Users": 3000000,
        "Employees": 1700000,
        "Students": 600000,
        "Men Age 50+": 400000,
        "Women Age 50+": 300000
    },
    {
        "State": "Vermont",
        "White (%)": 93.2,
        "Black (%)": 1.5,
        "Indian (%)": 1.0,
        "Asian (%)": 2.3,
        "Hawaiian (%)": 0.1,
        "Others (%)": 2.9,
        "Total Population": 646599,
        "Female Population (%)": 50.4,
        "Literacy Rate (%)": 94.0,
        "Crime Rate (per 100k)": 200.0,
        "Year": 2024,
        "Schools": 400,
        "Mobile Phone Users": 400000,
        "Employees": 200000,
        "Students": 150000,
        "Men Age 50+": 70000,
        "Women Age 50+": 60000
    },
    {
        "State": "Virginia",
        "White (%)": 66.4,
        "Black (%)": 18.4,
        "Indian (%)": 0.5,
        "Asian (%)": 7.0,
        "Hawaiian (%)": 0.2,
        "Others (%)": 7.5,
        "Total Population": 8662439,
        "Female Population (%)": 50.7,
        "Literacy Rate (%)": 89.4,
        "Crime Rate (per 100k)": 259.5,
        "Year": 2024,
        "Schools": 3000,
        "Mobile Phone Users": 7000000,
        "Employees": 4500000,
        "Students": 1200000,
        "Men Age 50+": 800000,
        "Women Age 50+": 700000
    },
    {
        "State": "Washington",
        "White (%)": 69.0,
        "Black (%)": 4.6,
        "Indian (%)": 2.0,
        "Asian (%)": 9.4,
        "Hawaiian (%)": 0.5,
        "Others (%)": 14.5,
        "Total Population": 7693612,
        "Female Population (%)": 50.3,
        "Literacy Rate (%)": 90.7,
        "Crime Rate (per 100k)": 317.9,
        "Year": 2024,
        "Schools": 3000,
        "Mobile Phone Users": 7000000,
        "Employees": 4500000,
        "Students": 1200000,
        "Men Age 50+": 800000,
        "Women Age 50+": 700000
    },
    {
        "State": "West Virginia",
        "White (%)": 91.4,
        "Black (%)": 3.5,
        "Indian (%)": 0.4,
        "Asian (%)": 1.1,
        "Hawaiian (%)": 0.1,
        "Others (%)": 3.5,
        "Total Population": 1778595,
        "Female Population (%)": 51.1,
        "Literacy Rate (%)": 87.8,
        "Crime Rate (per 100k)": 388.1,
        "Year": 2024,
        "Schools": 1000,
        "Mobile Phone Users": 700000,
        "Employees": 300000,
        "Students": 300000,
        "Men Age 50+": 200000,
        "Women Age 50+": 150000
    },
    {
        "State": "Wisconsin",
        "White (%)": 80.5,
        "Black (%)": 6.4,
        "Indian (%)": 1.0,
        "Asian (%)": 5.9,
        "Hawaiian (%)": 0.1,
        "Others (%)": 6.1,
        "Total Population": 5893718,
        "Female Population (%)": 50.3,
        "Literacy Rate (%)": 91.0,
        "Crime Rate (per 100k)": 244.4,
        "Year": 2024,
        "Schools": 2000,
        "Mobile Phone Users": 5000000,
        "Employees": 3000000,
        "Students": 1200000,
        "Men Age 50+": 800000,
        "Women Age 50+": 700000
    },
    {
        "State": "Wyoming",
        "White (%)": 89.0,
        "Black (%)": 1.3,
        "Indian (%)": 3.7,
        "Asian (%)": 1.3,
        "Hawaiian (%)": 0.1,
        "Others (%)": 4.6,
        "Total Population": 576851,
        "Female Population (%)": 50.3,
        "Literacy Rate (%)": 93.0,
        "Crime Rate (per 100k)": 195.2,
        "Year": 2024,
        "Schools": 400,
        "Mobile Phone Users": 400000,
        "Employees": 200000,
        "Students": 100000,
        "Men Age 50+": 50000,
        "Women Age 50+": 50000
    }
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1("U.S. Demographics Dashboard", className='dashboard-title', style={'textAlign': 'center','color': '#E6E6FA'}),
    
    html.Div(
        children=[
            dcc.Dropdown(
                id='state-dropdown',
                options=[{'label': state, 'value': state} for state in df['State'].unique()],
                value='Connecticut',  # Default value
                clearable=False,
                className='dropdown',
                style={'width': '300px', 'margin': '0 auto'}  # Set width and center it
            )
        ],
        style={
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
            'width': '100%',
            'height': '100px',
            'margin': 'auto',
            'padding': '20px'
        }
    ),
    html.Div(style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around'}, children=[
        html.Div(className='card', children=[dcc.Graph(id='demographics-bar-graph', style={'height': '300px'})], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[dcc.Graph(id='demographics-pie-chart', style={'height': '300px'})], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[dcc.Graph(id='demographics-scatter-plot', style={'height': '300px'})], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[dcc.Graph(id='demographics-line-plot', style={'height': '300px'})], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[dcc.Graph(id='demographics-box-plot', style={'height': '300px'})], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[dcc.Graph(id='demographics-histogram', style={'height': '300px'})], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[dcc.Graph(id='demographics-area-chart', style={'height': '300px'})], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[dcc.Graph(id='demographics-bubble-chart', style={'height': '300px'})], style={'width': '45%', 'margin': '20px'}),
        html.Div(className='card', children=[dcc.Graph(id='demographics-radar-chart', style={'height': '300px'})], style={'width': '45%', 'margin': '20px'}),
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
    Output('demographics-area-chart', 'figure'),
    Output('demographics-bubble-chart', 'figure'),
    Output('demographics-radar-chart', 'figure'),
    Input('state-dropdown', 'value')
)
def update_graphs(selected_state):
    try:
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

        # Scatter plot (Mobile Phone Users vs Crime Rate)
        scatter_fig = px.scatter(
            df, x='Mobile Phone Users', y='Crime Rate (per 100k)', 
            title='Scatter Plot: Mobile Phone Users vs Crime Rate',
            hover_name='State', template='plotly_dark'
        )

        # Line plot (Female Population vs Total Population)
        line_fig = px.line(
            df, x='State', y='Female Population (%)',
            title='Line Plot of Female Population (%) by State',
            template='plotly_dark'
        )

        # Box plot (Students distribution)
        box_fig = px.box(
            df, y='Schools', x='State',
            title='Box Plot of Student Population Distribution',
            template='plotly_dark'
        )

        # Histogram (Total Population distribution)
        histogram_fig = px.histogram(
            df, x='State', y='Women Age 50+',
            title='Histogram of Total Population Distribution',
            template='plotly_dark'
        )

        # Area Chart
        area_fig = px.area(
            df, x='State', y='Total Population',
            title='Area Chart of Total Population by State',
            template='plotly_dark'
        )

        # Bubble Chart
        bubble_fig = px.scatter(
            df, x='Mobile Phone Users', y='Total Population', size='Students',
            title='Bubble Chart: Total Population vs Mobile Phone Users',
            hover_name='State', template='plotly_dark'
        )

        # Radar Chart (Example for specific demographics)
        radar_fig = px.line_polar(
            df, r=filtered_df[['White (%)', 'Black (%)', 'Indian (%)', 'Asian (%)', 'Others (%)']].values,
            theta=['White (%)', 'Black (%)', 'Indian (%)', 'Asian (%)', 'Others (%)'],
            title='Radar Chart of Racial Distribution in ' + selected_state,
            template='plotly_dark'
        )

        return bar_fig, pie_fig, scatter_fig, line_fig, box_fig, histogram_fig, area_fig, bubble_fig, radar_fig

    except Exception as e:
        # Handle errors here (e.g., no data for the selected state)
        print(f"Error: {e}")
        return {}, {}, {}, {}, {}, {}, {}, {}, {}

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)




import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Sample data for the dashboard
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Value": [23, 17, 35, 29]
})

# Create a simple bar chart
fig = px.bar(df, x="Category", y="Value", title="Sample Bar Chart")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Sample Dashboard"),
    dcc.Graph(
        id='bar-chart',
        figure=fig
    ),
    html.P("This is a sample dashboard using Dash.")
])

if __name__ == '__main__':
    app.run_server(debug=True)
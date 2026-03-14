import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load Titanic dataset (using seaborn's version if available)
try:
    import seaborn as sns
    df = sns.load_dataset('titanic')
except:
    # fallback to reading from a local CSV (user may need to provide this)
    df = pd.read_csv("titanic.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Titanic Dataset Dashboard'),
    html.P("Interactive dashboard visualizing the Titanic dataset"),
    html.Label("Choose feature to display:"),
    dcc.Dropdown(
        id='feature-dropdown',
        options=[
            {'label': 'Survived', 'value': 'survived'},
            {'label': 'Sex', 'value': 'sex'},
            {'label': 'Pclass', 'value': 'pclass'},
            {'label': 'Embarked', 'value': 'embarked'},
            {'label': 'Age', 'value': 'age'},
            {'label': 'Fare', 'value': 'fare'}
        ],
        value='sex'
    ),
    dcc.Graph(id='feature-graph'),
    html.Hr(),
    html.Label("Survival Rate by Class"),
    dcc.Graph(
        id='survival-by-class',
        figure=px.bar(
            df.groupby('pclass')['survived'].mean().reset_index(),
            x='pclass', y='survived', labels={'survived': 'Survival Rate', 'pclass': 'Passenger Class'},
            title='Average Survival Rate by Passenger Class'
        )
    )
])

@app.callback(
    Output('feature-graph', 'figure'),
    [Input('feature-dropdown', 'value')]
)
def update_feature_graph(feature):
    if df[feature].dtype == 'object' or feature in ['survived', 'pclass', 'embarked', 'sex']:
        # Categorical/binned feature: show counts of survivors by feature
        fig = px.histogram(
            df, x=feature, color='survived', barmode='group',
            labels={'survived': 'Survived', feature: feature.title()},
            title=f'Survival Counts by {feature.title()}'
        )
    else:
        # Numerical feature: show histogram split by survivor status
        fig = px.histogram(
            df, x=feature, color='survived',
            nbins=30, barmode='overlay', opacity=0.7,
            labels={'survived': 'Survived', feature: feature.title()},
            title=f'{feature.title()} Distribution by Survival'
        )
    fig.update_layout(legend_title_text='Survived')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
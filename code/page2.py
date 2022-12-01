import dash
from dash import html, dcc, callback, Input, Output

import plotly.express as px

import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('C:/Users/Leeyourack/jookyoung/coffee/data/coffee_A.csv')


dash.register_page(__name__)

layout = html.Div([
    dcc.Graph(id='g-slider'),
    dcc.Slider(
        df['minute'].min(),
        df['minute'].max(),
        step=None,
        value=df['minute'].min(),
        marks={str(minute): str(minute) for minute in df['minute'].unique()},
        id='m-slider'
    )
])


@callback(
    Output('g-slider', 'figure'),
    Input('m-slider', 'value'))
def update_figure(selected_minute):
    filtered_df = df[df.minute == selected_minute]
    
    fig = px.scatter(filtered_df, x="Timestamp", y="Xvib",range_x=None,range_y=[-4000,0],                                             
                       hover_name="Id",
                     log_x=True, size_max=55)


    

    fig.update_layout(transition_duration=500)

    return fig


'''if __name__ == '__main__':
    app.run_server(debug=True)
'''
import dash
from dash import html, dcc, callback, Input, Output

import plotly.express as px

import plotly.graph_objects as go

import pandas as pd

all_df = pd.read_csv('C:/Users/Leeyourack/jookyoung/coffee/data/all_df_time.csv')
minx, maxx = min(all_df['Ax']),max(all_df['Ax'])
miny, maxy = min(all_df['Ay']),max(all_df['Ay'])
minz, maxz = min(all_df['Az']),max(all_df['Az'])

dash.register_page(__name__)

layout = html.Div([
    dcc.Graph(id='graph-slider'),
    dcc.Slider(
        all_df['minute'].min(),
        all_df['minute'].max(),
        step=None,
        value=all_df['minute'].min(),
        marks={str(minute): str(minute) for minute in all_df['minute'].unique()},
        id='minute-slider'
    )
])


@callback(
    Output('graph-slider', 'figure'),
    Input('minute-slider', 'value'))
def update_figure(selected_minute):
    filtered_all_df = all_df[all_df.minute == selected_minute]
    
    fig = px.scatter_3d(filtered_all_df, x="Ax", y="Ay",z = "Az",
                        range_x=[minx, maxx],
                        range_y=[miny, maxy],
                        range_z=[minz, maxz],
                        color="label", hover_name="label",   
                        log_x=False, size_max=200,opacity=0.1)


    

    fig.update_layout(transition_duration=500)

    return fig


'''if __name__ == '__main__':
    app.run_server(debug=True)
'''
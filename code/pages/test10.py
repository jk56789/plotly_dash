from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import plotly.express as px
import dash
from dash import html, dcc, callback, Input, Output

colors = {
'background': '#111111',
'text': '#7FDBFF'
}

dash.register_page(__name__)
layout = html.Div([
    html.H4('Analysis of the restaurant sales'),
    dcc.Graph(id="graph"),
    html.P("Names:"),
    dcc.Dropdown(id='names',
        options=['smoker', 'day', 'time', 'sex'],
        value='day', clearable=False
    ),
    html.P("Values:"),
    dcc.Dropdown(id='values',
        options=['total_bill', 'tip', 'size'],
        value='total_bill', clearable=False
    ),
])


@callback(
    Output("graph", "figure"), 
    Input("names", "value"),    
    Input("values", "value"))
def generate_chart(names, values):
    df = px.data.tips() # replace with your own data source
    fig = px.pie(df, values=values, names=names, hole=.3, color_discrete_sequence=px.colors.sequential.RdBu)
    
    fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )

    
    return fig


'''app.run_server(debug=True)'''
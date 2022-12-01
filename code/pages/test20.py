from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)


layout = html.Div([
    html.H4('Restaurant tips by day of week'),
    dcc.Dropdown(
        id="dropdown_b",
        options=["Fri", "Sat", "Sun"],
        value="Fri",
        clearable=False,
    ),
    dcc.Graph(id="graph_b"),
])


@callback(
    Output("graph_b", "figure"), 
    Input("dropdown_b", "value"))
def update_bar_chart(day):
    df = px.data.tips() # replace with your own data source
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", 
                 color="smoker", barmode="group")
    return fig


'''app.run_server(debug=True)'''
import dash
from dash import Dash, Input, Output, callback, dash_table
import pandas as pd
import dash_bootstrap_components as dbc

from dash import html, dcc, callback, Input, Output

df = pd.read_csv('https://git.io/Juf1t')

external_stylesheets=[dbc.themes.BOOTSTRAP]
dash.register_page(__name__, external_stylesheets=external_stylesheets)


layout = dbc.Container([
    dbc.Label('Click a cell in the table:'),
    dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], id='tbl'),
    dbc.Alert(id='tbl_out'),
])

@callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"

'''if __name__ == "__main__":
    app.run_server(debug=True)'''

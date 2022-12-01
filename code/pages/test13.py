import plotly.express as px
from dash import Dash, dcc, html, Input, Output, no_update
from skimage import data
import json
import dash
from dash import html, dcc, callback, Input, Output

img = data.chelsea()
fig = px.imshow(img)
fig.update_layout(dragmode="drawrect")

dash.register_page(__name__)
layout = html.Div(
    [
        html.H1("Drag and draw rectangle annotations"),
        dcc.Graph(id="graph-picture1", figure=fig),
        dcc.Markdown("Characteristics of shapes"),
        html.Pre(id="annotations-data1"),
    ]
)

@callback(
    Output("annotations-data1", "children"),
    Input("graph-picture1", "relayoutData"),
    prevent_initial_call=True,
)
def on_new_annotation(relayout_data):
    if "shapes" in relayout_data:
        return json.dumps(relayout_data["shapes"], indent=2)
    else:
        return no_update
'''
if __name__ == "__main__":
    app.run_server(debug=True)'''

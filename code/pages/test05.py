# -*- coding: utf-8 -*-

import dash
from dash import html, dcc, callback, Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


dash.register_page(__name__, external_stylesheets=external_stylesheets)
all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}
layout = html.Div([
    dcc.RadioItems(
        list(all_options.keys()),
        'America',
        id='countries-radio',
    ),

    html.Hr(),

    dcc.RadioItems(id='cities-radio'),

    html.Hr(),

    html.Div(id='display-selected-values')
])


@callback(
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@callback(
    Output('cities-radio', 'value'),
    Input('cities-radio', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']


@callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'))
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )

'''
if __name__ == '__main__':
    app.run_server(debug=True)'''

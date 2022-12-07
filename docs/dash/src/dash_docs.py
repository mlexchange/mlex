# #!/usr/bin/env Python3

import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Iframe(
            src="assets/html/index.html",
            style={"height": "1067px", "width": "100%"},
        )
    ]
)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8058, debug=True)
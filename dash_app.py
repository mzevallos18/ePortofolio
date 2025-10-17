from dash import Dash, html, dcc, dash_table, Input, Output
import pandas as pd
from animalshelter import AnimalShelter

# Connect to database
db = AnimalShelter()

# Load rows into DataFrame
def load_df(limit=500):
    cur = db.read({}, limit=limit)
    data = list(cur) if cur is not None else []
    df = pd.DataFrame(data)
    if "_id" in df.columns:
        df["_id"] = df["_id"].astype(str)
    return df

df = load_df(limit=300)

# Build dropdown filter values
animal_types = sorted(df["animal_type"].dropna().unique()) if "animal_type" in df else []
breeds = sorted(df["breed"].dropna().unique()) if "breed" in df else []

# Initialize Dash app
app = Dash(__name__)
app.title = "Animal Shelter Dashboard"

# Layout
app.layout = html.Div(
    style={"fontFamily": "system-ui, -apple-system, Segoe UI, Roboto, Arial", "padding": "16px"},
    children=[
        html.H2("Animal Shelter Dashboard"),

        # Filter controls
        html.Div(
            style={"display": "flex", "gap": "12px", "flexWrap": "wrap", "marginBottom": "12px"},
            children=[
                html.Div([
                    html.Label("Animal Type"),
                    dcc.Dropdown(
                        id="f-type",
                        options=[{"label": v, "value": v} for v in animal_types],
                        value=None,
                        placeholder="All",
                        clearable=True,
                        style={"minWidth": "220px"}
                    ),
                ]),
                html.Div([
                    html.Label("Breed"),
                    dcc.Dropdown(
                        id="f-breed",
                        options=[{"label": v, "value": v} for v in breeds],
                        value=None,
                        placeholder="All",
                        clearable=True,
                        style={"minWidth": "220px"}
                    ),
                ]),
                html.Button("Refresh", id="btn-refresh", n_clicks=0, style={"height": "40px", "alignSelf": "end"})
            ]
        ),

        # Data table
        dash_table.DataTable(
            id="tbl",
            columns=[{"name": c, "id": c} for c in df.columns],
            data=df.to_dict("records"),
            page_size=15,
            filter_action="native",
            sort_action="native",
            style_table={"overflowX": "auto"},
            style_cell={"fontSize": 13, "padding": "6px"},
        ),

        # Row count display
        html.Div(id="row-count", style={"marginTop": "8px", "opacity": 0.75}),
    ]
)

# Update table when filters or refresh button change
@app.callback(
    Output("tbl", "data"),
    Output("tbl", "columns"),
    Output("row-count", "children"),
    Input("f-type", "value"),
    Input("f-breed", "value"),
    Input("btn-refresh", "n_clicks"),
)
def update_table(type_val, breed_val, _):
    base = {}
    if type_val:
        base["animal_type"] = type_val
    if breed_val:
        base["breed"] = breed_val

    cur = db.read(base, limit=500)
    data = list(cur) if cur is not None else []
    df2 = pd.DataFrame(data)
    if not df2.empty and "_id" in df2.columns:
        df2["_id"] = df2["_id"].astype(str)

    if df2.empty:
        cols = [{"name": c, "id": c} for c in (df.columns if len(df.columns) else ["_id"])]
        return [], cols, "0 rows"
    cols = [{"name": c, "id": c} for c in df2.columns]
    return df2.to_dict("records"), cols, f"{len(df2)} rows"

# Run app
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8050)

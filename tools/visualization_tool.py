import plotly.express as px
import pandas as pd

def create_visualization(
    reduced,
    labels
):

    df = pd.DataFrame({
        "x": reduced[:,0],
        "y": reduced[:,1],
        "cluster": labels
    })

    fig = px.scatter(
        df,
        x="x",
        y="y",
        color="cluster"
    )

    return fig
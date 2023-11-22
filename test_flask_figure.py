import base64
from io import BytesIO

from flask import Flask

from matplotlib.figure import Figure
from figure import figure_to_base64

app = Flask(__name__)


@app.route("/")
def hello():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    data = figure_to_base64(fig)
    return f"<img src='data:image/png;base64,{data}'/>"


if __name__ == "__main__":
    app.run(debug=True)

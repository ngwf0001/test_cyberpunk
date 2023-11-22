def figure_to_base64(figure):
    """
    The selected code is a function that takes a Matplotlib figure as an input 
    and returns a base64-encoded PNG representation of the figure. 
    The function first creates a BytesIO object to store the image data, 
    then it saves the figure to the BytesIO object in PNG format using the savefig method. 
    Finally, the function uses the base64 module to encode the image data and 
    returns it as a string.
    """
    fig = figure
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")

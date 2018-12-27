from bokeh.plotting import figure
from bokeh.models import Range1d
import base64
import io
from imageio import imread

height = 500
width = 500
min_bound = 50
def init(plot, xmax, ymax, offset):
    startX = -offset
    startY = -ymax - offset
    plot.x_range = Range1d(startX, xmax + offset)
    plot.y_range = Range1d(startY, offset)
    plot.height = height
    plot.width = width
    plot.axis.visible = False
    plot.toolbar.logo = None
    plot.toolbar.active_drag = None
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_color = None

def adjust_plot(plot, height, width):
    if width > height:
        plot.x_range.start = -min_bound
        plot.x_range.end = width + min_bound
        max_bound = ((width+ 2 * min_bound) - height)/2
        plot.y_range.start = -height - max_bound
        plot.y_range.end = max_bound
    else:
        plot.y_range.start = -height - min_bound
        plot.y_range.end = min_bound 
        max_bound = ((height+ 2 * min_bound) - width)/2
        plot.x_range.start = -max_bound
        plot.x_range.end = width + max_bound


def default(value, default_value):
    if value is None:
        return default_value
    return value

def loadImage(data_uri):
    data_uri = data_uri.split(",")[1]
    imgData = imread(io.BytesIO(base64.b64decode(data_uri)))
    return imgData
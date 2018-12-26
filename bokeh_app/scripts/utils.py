from bokeh.plotting import figure
from bokeh.models import Range1d
import matplotlib.image as mpimg

height = 500
width = 500

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


def default(value, default_value):
    if value is None:
        return default_value
    return value
    
def loadImage(file):
    imgData = mpimg.imread(file)
    return imgData


def foo():
    return 3;
import point_generation as pg
import drawers as ds
import utils as u

import time
import numpy as np
from scipy.spatial import Delaunay
# import matplotlib.image as mpimg

from bokeh.io import save
from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d, ColumnDataSource
from bokeh.layouts import row, column

# file = "images/DSC_0377.JPG"
file = "images/face.jpg"
# file = "HSuDAAAAAXNSR0IArs4c6QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KTMInWQAAQABJREFUeAHsfQFi6ziuZCfdx9sL7UX2tNPJCpJLKpYAghQp23kd"
output_file("file.html")
numPoints = 300
offset = 50
showPlots = True




def core():
    p1 = figure(title= "Original Image")
    p2 = figure(title= "Delaunay Mesh")
    p3 = figure(title= "Low Poly Image")
    imgData = u.loadImage(file)
    ymax, xmax = imgData.shape[:2]
    ymax = 1024
    xmax = 1024
    u.init(p1, xmax, ymax, offset)
    u.init(p2, xmax, ymax, offset)
    u.init(p3, xmax, ymax, offset)

    # points = pg.generate_uniform_random_points([ymax, xmax], numPoints)
    # points = pg.generate_smart_points(imgData, numPoints)
    print "Points Generated in"

    ds.draw_image_url(p1, file, imgData)
    print "Image drawn in"

    # tri = Delaunay(points)
    # ds.draw_delaunay(p2, tri.points, tri.simplices)
    print "Delaunay calculated and drawn in"

    # ds.draw_low_poly(p3, tri, imgData)
    print "Lowpoly drawn in"

    # layout = column(row(p1, p2), p3)
    return column(row(p1, p2), p3)
    # tab = Panel(child=layout, title = 'Histogram')

    # return layout

if __name__ == "__main__":
	# show(core())
    core()
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
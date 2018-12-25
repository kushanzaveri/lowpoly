import point_generation as pg
import drawers as ds

import time
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.io import save
from bokeh.models import Range1d
from bokeh.layouts import row, column
from scipy.spatial import Delaunay
import matplotlib.image as mpimg

# file = "images/DSC_0377.JPG"
file = "images/face.jpg"
output_file("file.html")
numPoints = 300
offset = 50
showPlots = True

def init(plot, xmax, ymax):
    startX = -offset
    startY = -ymax - offset
    plot.x_range = Range1d(startX, xmax + offset)
    plot.y_range = Range1d(startY, offset)
    plot.height = 500
    plot.width = 500
    plot.axis.visible = False
    plot.toolbar.logo = None
    plot.toolbar.active_drag = None

def loadImage(file):
    imgData = mpimg.imread(file)
    return imgData

def start(p1, p2, p3, p4):
    imgData = loadImage(file)
    ymax, xmax = imgData.shape[:2]

    init(p1, xmax, ymax)
    init(p2, xmax, ymax)
    init(p3, xmax, ymax)
    init(p4, xmax, ymax)

    millis = int(round(time.time() * 1000))
    # points = pg.generate_uniform_random_points([ymax, xmax], numPoints)
    points = pg.generate_smart_points(imgData, numPoints)
    print "Points Generated in"
    print int(round(time.time() * 1000)) - millis

    millis = int(round(time.time() * 1000))
    ds.draw_image_url(p1, file, imgData)
    print "Image drawn in"
    print int(round(time.time() * 1000)) - millis

    millis = int(round(time.time() * 1000))
    tri = Delaunay(points)
    ds.draw_delaunay(p2, tri.points, tri.simplices)
    print "Delaunay calculated and drawn in"
    print int(round(time.time() * 1000)) - millis

    millis = int(round(time.time() * 1000))
    ds.draw_low_poly(p3, tri, imgData)
    print "Lowpoly drawn in"
    print int(round(time.time() * 1000)) - millis


if __name__ == "__main__":
    total = int(round(time.time() * 1000))
    p1 = figure(title= "Original Image")
    p2 = figure(title= "Delaunay Mesh")
    p3 = figure(title= "Low Poly Image")
    p4 = figure(title= "ENTROPY?")
    start(p1, p2, p3, p4)
    if (showPlots):
        # show(row(p1, p2, p3))
        save(column(row(p1, p2), row(p3, p4)), "out.html")
    print "Total time:"
    print int(round(time.time() * 1000)) - total

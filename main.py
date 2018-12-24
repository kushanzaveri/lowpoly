from __future__ import division

import point_generation as pg
import drawers as ds
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row
from scipy.spatial import Delaunay
import time
import matplotlib.image as mpimg
total = int(round(time.time() * 1000))

output_file("file.html")
numPoints = 100000
imgW = 1024
imgH = 1024
offset = 50
file = "face.jpg"


p1 = figure(x_range=(- offset, imgW + offset),
           y_range=(-imgH - offset, offset))
p2 = figure(x_range=(- offset, imgW + offset),
           y_range=(-imgH - offset, offset))
p3 = figure(x_range=(- offset, imgW + offset),
           y_range=(-imgH - offset, offset))

imgData = mpimg.imread(file)

millis = int(round(time.time() * 1000))
points = pg.generate_uniform_random_points([imgW, imgH], numPoints)
# points = pg.generate_smart_points(imgData, numPoints)
print "Points Generated in"
print int(round(time.time() * 1000)) - millis



ds.draw_image_url(p1, file)

print "Image drawn"
tri = Delaunay(points)
millis = int(round(time.time() * 1000))
ds.draw_delaunay(p2, tri.points, tri.simplices)
print "Delaunay calculated in"
print int(round(time.time() * 1000)) - millis

millis = int(round(time.time() * 1000))
ds.draw_low_poly(p3, tri, imgData)
print "Lowpoly drawn in"
print int(round(time.time() * 1000)) - millis

# show the results
show(row(p1, p2, p3))
print "total:"
print int(round(time.time() * 1000)) - total

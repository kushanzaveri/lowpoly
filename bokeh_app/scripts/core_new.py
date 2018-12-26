import point_generation as pg
import drawers as ds
import utils as u
# import time
# import numpy as np
from scipy.spatial import Delaunay

from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models.widgets import Button, Slider, RadioButtonGroup



class Core:

    delMesh = figure(title = "Delaunay Mesh")
    lowPol = figure(title = "Low Poly Image")
    slider = Slider(start=10, end=500, value=10, step=1, title="Number of Triangles")
    point_type = RadioButtonGroup(
        labels=["Smart Generation", "Random Points"], active=0)
    def __init__(self, imgView, numPoints = 75, ymax = 1024, xmax = 1024, offset = 50):
        self.imgView = imgView;
        self.numPoints = numPoints;
        self.ymax = ymax
        self.xmax = xmax
        self.offset = offset
        self.slider.value = self.numPoints
        
    

    def generate_points(self, width, height, imgData, numPoints):
        if self.point_type.active == 0:
            return pg.generate_smart_points(imgData, numPoints)
        return pg.generate_uniform_random_points([height, width], numPoints)

    def processImage(self):
        # check if imgView.getName() is default
        imgData = u.loadImage(self.imgView.getName().split(",")[1])
        height, width = imgData.shape[:2]
        points = self.generate_points(width, height, imgData, self.slider.value);
        tri = Delaunay(points)
        ds.draw_delaunay(self.delMesh, tri.points, tri.simplices)
        ds.draw_low_poly(self.lowPol, tri, imgData)



    def getView(self):
        button = Button(label="Process...")
        button.on_click(self.processImage)
        u.init(self.delMesh, self.xmax, self.ymax, self.offset)
        u.init(self.lowPol, self.xmax, self.ymax, self.offset)
        return row(column(row(button, self.point_type), self.delMesh), column(self.slider, self.lowPol))



import point_generation as pg
import drawers as ds
import utils as u
import time
from scipy.spatial import Delaunay

from bokeh.plotting import figure, ColumnDataSource
from bokeh.layouts import row, column
from bokeh.models import Range1d
from bokeh.models.widgets import Button, Slider, RadioButtonGroup
from bokeh.models.glyphs import Patches


class Core:

    delMesh = figure(title = "Delaunay Mesh")
    lowPol = figure(title = "Low Poly Image")
    slider = Slider(start=10, end=10000, value=10, step=1, title="Number of Triangles")
    point_type = RadioButtonGroup(
        labels=["Smart Points", "Random Points"], active=1)
    
    triangles = ColumnDataSource(dict(
        xs=[0],
        ys=[0],
        colours=['black']
    ))
    
    def __init__(self, imgView, numPoints = 75, ymax = 1024, xmax = 1024, min_bound = 50):
        self.imgView = imgView;
        self.numPoints = numPoints;
        self.ymax = ymax
        self.xmax = xmax
        self.min_bound = min_bound
        self.slider.value = self.numPoints

    def generate_points(self, width, height, imgData, numPoints):
        if self.point_type.active == 0:
            return pg.generate_smart_points(imgData, numPoints)
        return pg.generate_uniform_random_points([height, width], numPoints)

    def processImage(self):
        millis = int(round(time.time() * 1000))
        imgData = self.imgView.img_data
        height, width = imgData.shape[:2]
        u.adjust_plot(self.delMesh, height, width)
        u.adjust_plot(self.lowPol, height, width)
        points = self.generate_points(width, height, imgData, self.slider.value);
        tri = Delaunay(points)
        self.triangles.data = ds.get_data(tri, imgData)



    def getView(self):
        button = Button(label="Process...")
        button.on_click(self.processImage)
        u.init(self.delMesh, self.xmax, self.ymax, self.min_bound)
        u.init(self.lowPol, self.xmax, self.ymax, self.min_bound)
        self.delMesh.patches(xs = 'xs', ys = 'ys', line_color="#5581CD", fill_alpha=0, source = self.triangles)
        self.lowPol.patches(xs = 'xs', ys = 'ys', color = 'colours', source = self.triangles)
        return row(column(row(button, self.point_type), self.delMesh), column(self.slider, self.lowPol))



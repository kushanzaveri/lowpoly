from bokeh.plotting import figure, ColumnDataSource
import numpy as np
import random
import time
 
def draw_image_url(p, url, imgData):
    ymax, xmax = imgData.shape[:2]
    p.image_url(url=[url], x=0, y=0, w=xmax, h=ymax)

def draw_points(p, points):
    p.scatter(x = points[:,0], y = points[:,1], fill_color="#00FF00", line_color="#00FF00")

def get_x_coords(points, simplices):
    ret = list(map(lambda i : list(map(lambda j : j[0], points[i])), simplices))
    return ret

def get_y_coords(points, simplices):
    ret = list(map(lambda i : list(map(lambda j : -j[1], points[i])), simplices))
    return ret


def get_triangle_colours(tri, imgData, agg_func=np.median):
    # create a list of all pixel coordinates
    ymax, xmax = imgData.shape[:2]
    xx, yy = np.meshgrid(np.arange(xmax), np.arange(ymax))
    pixel_coords = np.c_[xx.ravel(), yy.ravel()]
    
    # for each pixel, identify which triangle it belongs to
    triangles_for_coord = tri.find_simplex(pixel_coords)
    combRed = np.stack(arrays=(triangles_for_coord, imgData.reshape(-1, 3)[:, 0]), axis = -1)
    combGreen = np.stack(arrays=(triangles_for_coord, imgData.reshape(-1, 3)[:, 1]), axis = -1)
    combBlue = np.stack(arrays=(triangles_for_coord, imgData.reshape(-1, 3)[:, 2]), axis = -1)
    import numpy_indexed as npi
    reds =  (npi.group_by(combRed[:, 0]).median(combRed[:, 1])[1])
    greens = (npi.group_by(combGreen[:, 0]).median(combGreen[:, 1])[1])
    blues = (npi.group_by(combBlue[:, 0]).median(combBlue[:, 1])[1])
    by_triangle = np.stack(arrays=(reds, greens, blues), axis = -1)
    ret = list(map(lambda i: "rgb(%d,%d,%d)" % (i[0], i[1], i[2]), by_triangle))
    return ret


def get_data(tri, imgData):
    x = get_x_coords(tri.points, tri.simplices)
    y = get_y_coords(tri.points, tri.simplices)
    colours = get_triangle_colours(tri, imgData)
    return dict(xs = x, ys = y, colours = colours)

def draw_delaunay(p, points, simplices):
    x = get_x_coords(points, simplices)
    y = get_y_coords(points, simplices)
    p.patches(xs = x, ys = y, line_color="#5581CD", fill_alpha=0)



def draw_low_poly(p, tri, imgData):
    x = get_x_coords(tri.points, tri.simplices)
    y = get_y_coords(tri.points, tri.simplices)
    p.patches(xs = x, ys = y, color = get_triangle_colours(tri, imgData))

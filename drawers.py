from bokeh.plotting import figure
import numpy as np
import pandas as pd
import random
def draw_image_url(p, url):
    p.image_url(url=[url], x=0, y=0, w=1024, h=1024)

def draw_points(p, points):
    p.scatter(x = points[:,0], y = points[:,1], fill_color="#00FF00", line_color="#00FF00")

def get_x_coords(points, simplices):
    return map(lambda i : map(lambda j : j[0], points[i]), simplices)

def get_y_coords(points, simplices):
    return map(lambda i : map(lambda j : -j[1], points[i]), simplices)


def get_triangle_colours(tri, imgData, agg_func=np.median):
    # create a list of all pixel coordinates
    ymax, xmax = imgData.shape[:2]
    xx, yy = np.meshgrid(np.arange(xmax), np.arange(ymax))
    pixel_coords = np.c_[xx.ravel(), yy.ravel()]

    # for each pixel, identify which triangle it belongs to
    triangles_for_coord = tri.find_simplex(pixel_coords)

    df = pd.DataFrame({
        "triangle": triangles_for_coord,
        "r": imgData.reshape(-1, 3)[:, 0],
        "g": imgData.reshape(-1, 3)[:, 1],
        "b": imgData.reshape(-1, 3)[:, 2]
    })

    n_triangles = tri.vertices.shape[0]

    by_triangle = (
        df
            .groupby("triangle")
        [["r", "g", "b"]]
            .aggregate(agg_func)
            .reindex(range(n_triangles), fill_value=0)
        # some triangles might not have pixels in them
    )

    return by_triangle.values / 256

def draw_delaunay(p, points, simplices):
    x = get_x_coords(points, simplices)
    y = get_y_coords(points, simplices)
    p.patches(xs = x, ys = y, line_color="#5581CD", fill_alpha=0)



def draw_low_poly(p, tri, imgData):
    x = get_x_coords(tri.points, tri.simplices)
    y = get_y_coords(tri.points, tri.simplices)
    colors = \
    map(lambda i : "rgb(%d,%d,%d)" % (i[0]*255, i[1]*255, i[2]*255),
        get_triangle_colours(tri, imgData))
    p.patches(xs = x, ys = y, color = colors)

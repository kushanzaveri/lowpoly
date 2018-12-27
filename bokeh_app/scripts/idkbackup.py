
    # print (type(imgData))
    # millis = int(round(time.time() * 1000))
    # arr = list(range(tri.simplices.shape[0]))
    # def func(elem):
    #     return [0, 0, 0]
    # blank = list(map(func, arr))
    # print (blank)

    # for i, elem in enumerate(triangles_for_coord):
    #     rVal = rgbData[i][0]
    #     gVal = rgbData[i][1]
    #     bVal = rgbData[i][2]
    #     blank[elem] = [blank[elem][0] + rVal, 
    #                    blank[elem][1] + gVal, 
    #                    blank[elem][2] + bVal]
    # # for i, x in enumerate(rgbData):
    #     # print (i)
    #     # 2+2;
    #     # simplex = triangles_for_coord[i]
    #     # if simplex in my_dict:
    #     #     # 2 + 2;
    #     #     my_dict[simplex] = np.concatenate([my_dict[simplex], [rgbData[i]]])
    #     # else:
    #     #     my_dict[simplex] = np.array([rgbData[i]])
    #         # print (my_dict[simplex])

    # print (int(round(time.time() * 1000))- millis);
    # def func(arr):
    #     print(arr[:10])
    #     # cool = reduce((lamda x, y: x = [x[0] + y[0], x[1] + y[1]]),arr)
    #     print(len(arr))
    #     return len(arr)
    # map(func, my_dict)  
    # my_arr = {func(v) for k, v in my_dict.items()}
    # from collections import defaultdict
    # dicts_by_group = defaultdict(my_dict)
    # for dic in my_dict:

    from bokeh.plotting import figure, ColumnDataSource
import numpy as np
import pandas as pd
import random
import time

 
def draw_image_url(p, url, imgData):
    ymax, xmax = imgData.shape[:2]
    p.image_url(url=[url], x=0, y=0, w=xmax, h=ymax)

def draw_points(p, points):
    p.scatter(x = points[:,0], y = points[:,1], fill_color="#00FF00", line_color="#00FF00")

def get_x_coords(points, simplices):
    return list(map(lambda i : map(lambda j : j[0], points[i]), simplices))

def get_y_coords(points, simplices):
    return list(map(lambda i : map(lambda j : -j[1], points[i]), simplices))


def get_triangle_colours(tri, imgData, agg_func=np.median):
    # create a list of all pixel coordinates
    ymax, xmax = imgData.shape[:2]
    xx, yy = np.meshgrid(np.arange(xmax), np.arange(ymax))
    pixel_coords = np.c_[xx.ravel(), yy.ravel()]
    
    # for each pixel, identify which triangle it belongs to
    triangles_for_coord = tri.find_simplex(pixel_coords)
    millis = int(round(time.time() * 1000))
    # rgbData = imgData.reshape(-1, 3)
    combRed = np.stack(arrays=(triangles_for_coord, imgData.reshape(-1, 3)[:, 0]), axis = -1)
    combGreen = np.stack(arrays=(triangles_for_coord, imgData.reshape(-1, 3)[:, 1]), axis = -1)
    combBlue = np.stack(arrays=(triangles_for_coord, imgData.reshape(-1, 3)[:, 2]), axis = -1)
    import numpy_indexed as npi
    test1 = npi.group_by(combRed[:, 0]).split(combRed[:, 1])
    test2 = npi.group_by(combGreen[:, 0]).split(combGreen[:, 1])
    test3 = npi.group_by(combBlue[:, 0]).split(combBlue[:, 1])
    test1 = list(map(lambda i: np.median(i), test1))
    test2 = list(map(lambda i: np.median(i), test2))
    test3 = list(map(lambda i: np.median(i), test3))
    by_triangle = np.stack(arrays=(test1, test2, test3), axis = -1)
    print (int(round(time.time() * 1000))- millis);
    millis = int(round(time.time() * 1000))
        
    # df = pd.DataFrame({
    #     "triangle": triangles_for_coord,
    #     "r": imgData.reshape(-1, 3)[:, 0],
    #     "g": imgData.reshape(-1, 3)[:, 1],
    #     "b": imgData.reshape(-1, 3)[:, 2]
    # })


    # n_triangles = tri.vertices.shape[0]
    import sys
    print(sys.version)
    # by_triangle = (
    #     df.groupby("triangle")[["r", "g", "b"]]
    #       .aggregate(agg_func)
    #       .reindex(range(n_triangles), fill_value=0)
    #     # some triangles might not have pixels in them
    # )
    # print (int(round(time.time() * 1000))- millis);
    # print (by_triangle.values[0:5])
    return list(map(lambda i: "rgb(%d,%d,%d)" % (i[0], i[1], i[2]), by_triangle))


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

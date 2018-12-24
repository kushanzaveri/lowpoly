import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d

def draw_image(ax, im):
    ax.imshow(im);

def draw_points(ax, points):
    ax.scatter(x=points[:, 0], y=points[:, 1], color="k", s = 25);

def draw_delaunay(ax, points):
    tri = Delaunay(points)
    print type(tri);
    ax.triplot(points[:,0], points[:,1], tri.simplices.copy())

def draw_voronoi(ax, points):
    vor = Voronoi(points)
    voronoi_plot_2d(vor, ax, show_points = False, show_vertices = False)

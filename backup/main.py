import point_generation as pg
import drawers as ds
import numpy as np
import matplotlib.pylab as plt

fig, ax = plt.subplots();

im = plt.imread("lake.jpg");
points = pg.generate_uniform_random_points(im.shape, 100);

ds.draw_image(ax, im);
ds.draw_delaunay(ax, points);
# ds.draw_voronoi(ax, points);
ds.draw_points(ax, points);
plt.show();

import tools.drawers as d
import matplotlib.image as mpimg
from scipy.spatial import Delaunay
import tools.point_generation as pg
import tools.drawers as d
file = "../../../images/face.jpg"

img = mpimg.imread(file)
points = pg.generate_uniform_random_points(img.shape[:2], 5)
tri = Delaunay(points)

d.get_triangle_colours(tri, img)
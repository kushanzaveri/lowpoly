import numpy as np
from skimage import filters, morphology, color
import matplotlib.pyplot as plt

def generate_edge_points(dims, scale = 200):
    ymax, xmax = dims[:2]
    horiz_points = int(xmax / scale)
    vert_points = int(ymax / scale)
    del_x = scale
    del_y = scale
    return np.array(
        [[0, 0], [xmax, 0], [0, ymax], [xmax, ymax]]
        + [[del_x * i, 0] for i in range(1, horiz_points)]
        + [[del_x * i, ymax] for i in range(1, horiz_points)]
        + [[0, del_y * i] for i in range(1, vert_points)]
        + [[xmax, del_y * i] for i in range(1, vert_points)]
        )

def generate_uniform_random_points(dims, num_points):
    height, width = dims[:2]
    height = height
    width = width
    points = np.random.uniform(size=(num_points, 2))
    points = np.multiply(points, [width, height])
    points = np.concatenate([points, generate_edge_points(dims)])
    return points

def gaussian_mask(x, y, shape, amp=1, sigma=15):
    xv, yv = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))
    g = amp * np.exp(-((xv - x) ** 2 + (yv - y) ** 2) / (2 * sigma ** 2))
    return g

def default(value, default_value):
    if value is None:
        return default_value
    return value

def generate_smart_points(image, num_points=100,
                                entropy_width=None,
                                filter_width=None,
                                suppression_width=None,
                                suppression_amplitude=None):
    ymax, xmax = image.shape[:2]
    scale = np.sqrt(xmax*ymax / num_points)

    entropy_width = scale * default(entropy_width, 0.2)
    filter_width = scale * default(filter_width, 0.1)
    suppression_width = scale * default(suppression_width, 0.3)
    suppression_amplitude = default(suppression_amplitude, 3)

    im_copy = color.rgb2gray(image)
    im_copy = (
        255 * filters.gaussian(im_copy, sigma=filter_width, multichannel=True)
    ).astype("uint8")
    ranked_pixels = filters.rank.entropy(im_copy, morphology.disk(entropy_width))

    points = []
    for i in range(num_points):
        # print i
        y, x = np.unravel_index(np.argmax(ranked_pixels), ranked_pixels.shape)
        ranked_pixels -= gaussian_mask(x, y,
                             shape=ranked_pixels.shape[:2],
                             amp=suppression_amplitude,
                             sigma=suppression_width)
        points.append((x, y))

    points = np.array(points)

    points = np.concatenate([points, generate_edge_points([ymax, xmax])])
    
    return points

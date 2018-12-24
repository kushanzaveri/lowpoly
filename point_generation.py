import numpy as np
from skimage import filters, morphology, color

def generate_edge_points(dims, scale = 200):
    ymax, xmax = dims[:2];
    horiz_points = int(xmax / scale)
    vert_points = int(ymax / scale)
    del_x = scale;
    del_y = scale;
    return np.array(
        [[0, 0], [xmax, 0], [0, ymax], [xmax, ymax]]
        + [[del_x * i, 0] for i in range(1, horiz_points)]
        + [[del_x * i, ymax] for i in range(1, horiz_points)]
        + [[0, del_y * i] for i in range(1, vert_points)]
        + [[xmax, del_y * i] for i in range(1, vert_points)]
        )

def generate_uniform_random_points(dims, num_points):
    height, width = dims[:2];
    height = height;
    width = width;
    points = np.random.uniform(size=(num_points, 2));
    points = np.multiply(points, [width, height]);
    points = np.concatenate([points, generate_edge_points(dims)]);
    return points;

def gaussian_mask(x, y, shape, amp=1, sigma=15):
    """
    Returns an array of shape, with values based on

    amp * exp(-((i-x)**2 +(j-y)**2) / (2 * sigma ** 2))

    :param x: float
    :param y: float
    :param shape: tuple
    :param amp: float
    :param sigma: float
    :return: array
    """
    xv, yv = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))
    g = amp * np.exp(-((xv - x) ** 2 + (yv - y) ** 2) / (2 * sigma ** 2))
    return g

def default(value, default_value):
    """
    Returns default_value if value is None, value otherwise
    """
    if value is None:
        return default_value
    return value

def generate_smart_points(image, n_points=100,
                                entropy_width=None,
                                filter_width=None,
                                suppression_width=None,
                                suppression_amplitude=None):



    # # calculate length scale
    # ymax, xmax = image.shape[:2]
    # length_scale = np.sqrt(xmax*ymax / n_points)
    # entropy_width = length_scale * default(entropy_width, 0.2)
    # filter_width = length_scale * default(filter_width, 0.1)
    # suppression_width = length_scale * default(suppression_width, 0.3)
    # suppression_amplitude = default(suppression_amplitude, 3)
    #
    # # convert to grayscale
    # im2 = color.rgb2gray(image)
    #
    # # filter
    # im2 = (
    #     255 * filters.gaussian(im2, sigma=filter_width, multichannel=True)
    # ).astype("uint8")
    #
    # # calculate entropy
    # im2 = filters.rank.entropy(im2, morphology.disk(entropy_width))
    #
    # points = []
    # for _ in range(n_points):
    #     y, x = np.unravel_index(np.argmax(im2), im2.shape)
    #     im2 -= gaussian_mask(x, y,
    #                          shape=im2.shape[:2],
    #                          amp=suppression_amplitude,
    #                          sigma=suppression_width)
    #     points.append((x, y))
    #
    # points = np.array(points)
    # points = np.concatenate([points, generate_edge_points([xmax, ymax])]);
    #
    # return points
    return 0;

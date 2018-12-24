import numpy as np

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
    height = height - 1;
    width = width - 1;
    print width;
    print height;
    points = np.random.uniform(size=(num_points, 2));
    points = np.multiply(points, [width, height]);
    points = np.concatenate([points, generate_edge_points(dims)]);
    return points;

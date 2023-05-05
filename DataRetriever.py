import random

import DataModel
from DataModel import *
import json

def rand_points(n=10, x_range=(-10.0, 10.0), y_range=(-10.0, 10.0)):

    # compute length of the x and y interval
    d_x = abs(x_range[0] - x_range[1])
    d_y = abs(y_range[0] - y_range[1])

    # create an output list
    points = []

    # compute n points and fill the list
    for i in range(n):
        points.append(Point(x_range[0] + random.random() * d_x, y_range[0] + random.random() * d_y))

    # return point list

    return points


def rand_points_sorted(n=10, x_range=(-10.0, 10.0), y_range=(-10.0, 10.0), direction='x', reverse=False):
    """Computes n random points and sorts them.
    Params:
        n (int) - number of points;
        x-range (tuple) - boundary on x-axis;
        y-range (tuple) - boundary on y-axis;
        direction (str) - 'x' sorted horizontal, 'y' sorted vertical;
        reverse (boolean) - indicates sorting direction;
        """

    # compute length of the x and y interval
    d_x = abs(x_range[0] - x_range[1])
    d_y = abs(y_range[0] - y_range[1])

    # create an output list
    points = []

    # compute n points and fill the list
    for i in range(n):
        points.append(Point(x_range[0] + random.random() * d_x, y_range[0] + random.random() * d_y))

    # return sorted point list
    if direction == 'x':
        sorted_points = sorted(points, key=lambda point: point.x, reverse=reverse)
    else:
        sorted_points = sorted(points, key=lambda point: point.y, reverse=reverse)

    return sorted_points

def rand_lines(x_range=(-250,250), y_range=(-250,250), line_length=(10, 100), n=10):
    source_list = rand_points(x_range=x_range, y_range=y_range, n=n)
    target_list = []

    # Check if lines can fit into bounding box
    assert line_length[1] < np.sqrt((x_range[1] - x_range[0])**2 + (y_range[1] - y_range[0])**2), "line length exceeds bounding box"

    # For each source point in source list, a target point in a random direction and a random length within the specified interval is computed
    for source in source_list:

        while 1 < 2:
            distance = random.uniform(*line_length)
            direction = random.uniform(0, 2 * np.pi)
            target = Point(source.x + distance * np.cos(direction), source.y + distance * np.sin(direction))

            # Check if computed target is within the bounding box
            if x_range[0] <= target.x <= x_range[1] and y_range[0] <= target.y <= y_range[1]:
                break

        # If target is valid, append target point to target list
        target_list.append(target)

    # Return a list of lines (specified by its source and target points)
    return [DataModel.Line(source_list[i], target_list[i]) for i in range(len(source_list))]


def readJsonFeatures(filepath):
    f = open(filepath)
    # returns JSON object as a dictionary
    data = json.load(f)
    # Closing file
    f.close()
    return data


if __name__ == "__main__":
    r_p = rand_lines((-100, 100), (99, 1000))
    for i in r_p:
        print((i.source.x, i.source.y),  (i.target.x, i.target.y))
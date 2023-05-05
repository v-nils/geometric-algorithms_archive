from numpy import inf
import DataModel
from DataRetriever import rand_points, rand_lines
from DataModel import Point, BoundingBox

def get_closest_point(points: list):
    """
    Checks for a list of points of Class DataModel.Point() the combination having the minimum distance to each other
    The complexity of this function is O(n**2)
    """

    # Set minimum distance to infinite
    min_dist = inf
    vertex_combination = None

    # Select point combinations
    for idx_src, source in enumerate(points):
        for idx_trg, target in enumerate(points):

            # Do not check duplicates
            if idx_trg <= idx_src:
                continue

            # check distance between vertex a and vertex b
            current_dist = source.distance(target)

            # check if current distance is smaller than minimum distance
            if current_dist < min_dist:
                min_dist = current_dist
                vertex_combination = [(source.x, source.y), (target.x, target.y)]
    return vertex_combination


def find_intersecting_lines(lines: list):
    """
    Identifies intersecting lines in a list of Line Objects

    Params:
        lines (list): List of Line Objects

    Returns:
        Tuple of two lists:
        - intersecting_lines: A list of Line objects that intersect with at least one other line in the input list.
        - non_intersecting_lines: A list of Line objects that do not intersect with any other line in the input list.

    Complexity:
        O(n**2)
    """

    # First a boolean list with the length of all elements in lines is created
    intersection_list = [False for _ in range(len(lines))]

    # Select and compare two lines in a nested loop:
    for idx, line_a in enumerate(lines):
        for line_b in lines:
            # Check if line a and b intersect using line_intersect function in Line Class
            if line_a.line_intersect(line_b):
                intersection_list[idx] = True
                break

    # Create two new lists. One containing intersecting and another with non-intersecting lines
    intersecting_lines = [line for line, intersects in zip(lines, intersection_list) if intersects]
    non_intersecting_lines = [line for line, intersects in zip(lines, intersection_list) if not intersects]

    return intersecting_lines, non_intersecting_lines


def convex_hull(points: list):
    """
    Creates a convex hull around a given list of points

    Params:
        - points (list): Al list containing points of class Point (specified in DataModel)
    """

    # Start with the point having the lowest y-value. Below that point there will be no other point
    seed = min([p.y for p in points])

    # Create a predecessor to append seed polar
    #predecessor = Point(s)






if __name__ == "__main__":
    r_l = find_intersecting_lines(rand_lines((-100, 100), (99, 1000), line_length=(100, 500)))
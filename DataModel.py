import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        delta_x = abs(point.x - self.x)
        delta_y = abs(point.y - self.y)
        return np.sqrt(delta_x + delta_y)

class BoundingBox:
    def __init__(self, points, padding=10):
        self.points = points
        self.padding = padding
        x_coords = [p.x for p in points]
        y_coords = [p.y for p in points]
        self.bb_min_x = np.min(x_coords)
        self.bb_min_y = np.min(y_coords)
        self.bb_max_x = np.max(x_coords)
        self.bb_max_y = np.max(y_coords)
        self.height = self.bb_max_y - self.bb_min_y
        self.width = self.bb_max_x - self.bb_min_x
        self.bbox_center_x = self.bb_min_x + self.width / 2
        self.bbox_center_y = self.bb_min_y + self.height / 2

    def transform_points(self, panel_size=700):
        scale = panel_size / max(self.width + self.padding, self.height + self.padding)
        x_translation = panel_size / 2 - self.bbox_center_x * scale
        y_translation = panel_size / 2 - self.bbox_center_y * scale
        return [Point((p.x * scale) + x_translation, (p.y * scale) + y_translation) for p in self.points]

class Line:
    def __init__(self, source: Point, target: Point):
        self.source = source
        self.target = target

    def point_orientation(self, point):
         p_o = (self.target.x - self.source.x) * (point.y - self.source.y) - \
               (point.x - self.source.x) * (self.target.y - self.source.y)
         if p_o == 0:
             return 0
         elif p_o > 0:
             return 1
         else:
            return -1

    def line_intersect(self, line):
        po1 = self.point_orientation(line.source)
        po2 = self.point_orientation(line.target)
        po3 = line.point_orientation(self.source)
        po4 = line.point_orientation(self.target)
        if po1 * po2 < 0 and po3 * po4 < 0:
            return True
        else:
            return False
from DataRetriever import rand_lines
import DataModel
from GeomOp import find_intersecting_lines
import pygletDrawer
import warnings
warnings.filterwarnings('ignore')

# Create random lines and two lists with intersecting and not intersecting lines
intersect, no_intersect = find_intersecting_lines(rand_lines((0, 800), (0, 800), (25, 250), 50))

# Plot points
drawer = pygletDrawer.Drawer(800, 800, "Example 1")

# Add points to the batch including their index a labels
for i, line in enumerate(intersect):
    drawer.addLineToBatch(line.source, line.target, 2)
    drawer.addCircleToBatch(line.source.x, line.source.y, 3, color=(100, 100, 100))
    drawer.addCircleToBatch(line.target.x, line.target.y, 3, color=(100, 100, 100))

for i, line in enumerate(no_intersect):
    drawer.addLineToBatch(line.source, line.target, 0.5, color=(100, 10, 10))
    drawer.addCircleToBatch(line.source.x, line.source.y, 3, color=(100, 100, 100))
    drawer.addCircleToBatch(line.target.x, line.target.y, 3, color=(100, 100, 100))

print(intersect, no_intersect)
drawer.openPanel()
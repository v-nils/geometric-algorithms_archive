import DataRetriever, pygletDrawer, GeomOp, sys

# read the x and y coordinates from the arguments (python lab1ExDemo.py 123 145). Always give a option to run the app without arguments by providing default values!
"""if len(sys.argv) == 3:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
else:
    x = 300
    y = 300"""

# Generate a random set of points, and return a list of Points
randomPointList = DataRetriever.rand_points_sorted(n=100, x_range=(0, 800), y_range=(0, 800), direction='y')

# Print in the console all generated radom points
for i in range(0, len(randomPointList)):
    print("Point {} ({},{})".format(i, randomPointList[i].x, randomPointList[i].y))

# Find the closest point
closestPoint = GeomOp.get_closest_point(randomPointList)

# Print the closest point
print("closest point combination is ({},{})".format(closestPoint[0], closestPoint[1]))

#######DRAWING###########
# Intanciate an pyglet drawer
drawer = pygletDrawer.Drawer(900, 900, "Example 1")

# Add points to the batch including their index a labels
for i in range(0, len(randomPointList)):
    drawer.addCircleToBatch(randomPointList[i].x, randomPointList[i].y, 3, color=(100, 100, 100))
    drawer.addLabelToBatch(str(i), randomPointList[i].x, randomPointList[i].y, 8)

# Highlight closes point in green
drawer.addCircleToBatch(closestPoint[0][0], closestPoint[0][1], 5, color=(255, 0, 0))

# Highlight given coordinates
drawer.addCircleToBatch(closestPoint[1][0], closestPoint[1][1], 5, color=(255, 225, 30))

# Open panel and draw shapes in batch!
drawer.openPanel()
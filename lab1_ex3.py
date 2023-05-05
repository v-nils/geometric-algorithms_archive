import DataRetriever
import DataModel
import pygletDrawer
import warnings
warnings.filterwarnings('ignore')

# Import Points
data = DataRetriever.readJsonFeatures("airports4.geojson")

# Extract coordinates of points and save them in a list
points = [(x['geometry']['coordinates'][0], x['geometry']['coordinates'][1]) for x in data['features']]
point_list = [DataModel.Point(v[0], v[1]) for v in points]

# Create a bounding box with a padding of 5
bbox = DataModel.BoundingBox(point_list, 5)

# Transform points to a box with edge length = 800
transformed_points = bbox.transform_points(800)

# Plot points
drawer = pygletDrawer.Drawer(800, 800, "Example 1")

# Add points to the batch including their index a labels
for i, p in enumerate(transformed_points):
    drawer.addCircleToBatch(p.x, p.y, 3, color=(100, 100, 100))
    drawer.addLabelToBatch(str(i), p.x, p.y, 8)

drawer.openPanel()
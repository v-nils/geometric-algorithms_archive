import pyglet
from pyglet import shapes
from pyglet.gl import *
import warnings
warnings.filterwarnings('ignore')


class Drawer(pyglet.window.Window):

    def __init__(self, width, height, title):
        config = pyglet.gl.Config(sample_buffers=1, samples=8)
        super().__init__(width=width, height=height, resizable=True, config=config)

        # change background color to white (default is black)
        pyglet.gl.glClearColor(1, 1, 1, 1)

        # Batch is a list of shapes that needs to be drawn.
        # By giving a Batch to multiple objects, you can tell pyglet that you expect to draw all of these objects at
        # once, so it can optimise its use of OpenGL
        self.batch = pyglet.graphics.Batch()
        self.shape_list = []
        self.label_list = []
        self.title = title


    def addCircleToBatch(self, x, y, radio, color=(200, 20, 20)):
        self.shape_list.append(shapes.Circle(x, y, radio, color=color, batch=self.batch))

    def addLineToBatch(self, point1, point2, width, color=(200, 20, 20)):
        self.shape_list.append(shapes.Line(point1.x, point1.y, point2.x, point2.y,
                                           width=width, color=color, batch=self.batch))

    def addLabelToBatch(self, text, x, y, fontSize):
        label = pyglet.text.Label(text, font_name='Times New Roman', font_size=fontSize, x=x, y=y, anchor_x='right',
                                  anchor_y='top', batch=self.batch)
        label.color = (0, 0, 0, 255)
        self.label_list.append(label)

        # Render the batch or anything else.

    def on_draw(self):
        # This command has to happen before we start drawing
        self.clear()
        # Draw everyting in batch!

        self.batch.draw()
        # glFlush empties all of these buffers, causing all issued commands to be executed as quickly as they are
        # accepted by the actual rendering engine.
        pyglet.gl.glFlush()

    # create the panel and run the drawings
    def openPanel(self):
        # This is a blocking function starting pyglet’s event loop meaning it will start to dispatch events such as
        # on_draw and on_update.
        pyglet.app.run()
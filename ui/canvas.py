from easygraphics import *
from .plot import Plot


class Canvas:

    def __init__(self, size=(900, 600), background=(52, 52, 59)):
        self.plt = Plot(x=100, y=100, width=400, height=300)
        if len(size) != 2:
            raise TypeError("size param must be a tuple: (width, height)")

        if len(background) != 3:
            raise TypeError("background param must be a tuple: (red, green, blue)")

        if background[0] > 255 or background[1] > 255 or background[2] > 255:
            raise ValueError("RGB color values must be between 0-255")

        self.width = size[0]
        self.height = size[1]
        self.background_color = \
            color_rgb(background[0], background[1], background[2])

    def create(self):
        init_graph(width=self.width,
                   height=self.height,
                   headless=False)

        # set_render_mode(RenderMode.RENDER_MANUAL)
        set_caption("Gesture Data Visualization")
        self.apply_background()
        self.loop()
        close_graph()

    def run(self):
        easy_run(self.create)

    def apply_background(self):
        set_fill_color(self.background_color)
        fill_rect(0, 0, self.width, self.height)


    def loop(self):
        while is_run():
            self.plt.bar([1, 2, 3], [100, 30, 200])

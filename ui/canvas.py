from easygraphics import *
from util import util
from .plot import Plot
import numpy as np


class Canvas:

    def __init__(self, data_source, size=(900, 600), background=(52, 52, 59)):
        self.data_source = data_source
        self.flex_plot = Plot(x=120, y=100, width=300, height=300)
        self.rotation_plot = Plot(x=500, y=100, width=300, height=300)
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
        self.show_waiting_dialog()
        self.loop()
        close_graph()

    def run(self):
        easy_run(self.create)

    def apply_background(self):
        set_fill_color(self.background_color)
        fill_rect(0, 0, self.width, self.height)

    def show_waiting_dialog(self):
        self.apply_background()
        set_color(rgb(255, 255, 255))
        draw_rect_text(0, 0, self.width, self.height, "Calibrating...", flags=TextFlags.ALIGN_CENTER)

    @staticmethod
    def add_plot_label(label, x, y):
        set_fill_style(FillStyle.SOLID_FILL)
        draw_rect_text(x, y, 300, 100, label, flags=TextFlags.ALIGN_CENTER)

    def loop(self):
        calibration_data = util.get_calibration_data(self.data_source)
        while is_run():
            try:
                values = self.data_source.readline().decode('utf-8').rstrip().split(',')
                values = np.array(list(map(float, values)))
                self.apply_background()
                self.flex_plot.draw_bar([1, 2, 3, 4, 5], values[:5], calibration_data[:5])
                self.add_plot_label("Flex Sensor Data", 110, 400)

                rotation_angles = util.get_rotation_angles(values[5], values[6], values[7], values[8])
                self.rotation_plot.draw_bar([1, 2, 3], values[12:15], calibration_data[12:15])
                self.add_plot_label("MPU 6050 Data", 510, 400)

            except ValueError:
                pass
            except KeyboardInterrupt:
                exit(0)

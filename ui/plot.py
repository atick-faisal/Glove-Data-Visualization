from easygraphics import *
from .config import *
import numpy as np


class Plot:
    def __init__(self, x, y, width, height):
        self.origin_x = x
        self.origin_y = y + height
        self.width = width
        self.height = height
        self.spacing = width * 0.25

    @staticmethod
    def get_mapped_y(y, calibration_data, max_y):
        scaled_y = np.abs(y - calibration_data) + 100
        mapped_y = scaled_y / np.max(scaled_y) * max_y
        return mapped_y

    @staticmethod
    def get_scaled_y(y, max_y):
        y = np.abs(y)
        scaled_y = y - min(y)
        mapped_y = scaled_y / np.max(scaled_y) * max_y
        return mapped_y

    def draw_bar(self, x_data, y_data, calibration_data=None):
        n = len(x_data)
        bar_width = (self.width - self.spacing) / n
        gap_width = self.spacing / n
        if calibration_data is not None:
            y_data = self.get_mapped_y(y_data, calibration_data, self.height)
        else:
            y_data = self.get_scaled_y(y_data, self.height)
        for i in range(n):
            bar_x1 = self.origin_x + i * (bar_width + gap_width)
            bar_x2 = bar_x1 + bar_width
            set_fill_style(FillStyle.LINE_FILL)
            set_fill_color(COLORS[i])
            fill_rect(bar_x1, self.origin_y - y_data[i], bar_x2, self.origin_y)

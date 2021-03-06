from easygraphics import *
from .config import *


class Plot:
    def __init__(self, x, y, width, height):
        self.origin_x = x
        self.origin_y = y + height
        self.width = width
        self.height = height
        self.spacing = width * 0.25

    @staticmethod
    def get_mapped_y(y, max_y):
        mapped_y = []
        for i in range(len(y)):
            mapped_y.append((y[i] / max(y)) * max_y)

        return mapped_y

    def bar(self, x_data, y_data):
        n = len(x_data)
        bar_width = (self.width - self.spacing) / n
        gap_width = self.spacing / n
        y = self.get_mapped_y(y_data, self.height)
        for i in range(n):
            bar_x1 = self.origin_x + i * (bar_width + gap_width)
            bar_x2 = bar_x1 + bar_width
            set_fill_color(COLORS[i])
            fill_rect(bar_x1, self.origin_y - y[i], bar_x2, self.origin_y)

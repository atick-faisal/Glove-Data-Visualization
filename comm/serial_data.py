import numpy as np


class SerialData:
    def __init__(self, data_source, calibration_data):
        self.data_source = data_source
        self.calibration_data = calibration_data

    def process_serial_data(self, canvas, callback):
        try:
            values = self.data_source.readline().decode('utf-8').rstrip().split(',')
            values = np.array(list(map(float, values)))
            callback(canvas, self.calibration_data, values)

        except ValueError:
            pass
        except KeyboardInterrupt:
            exit(0)

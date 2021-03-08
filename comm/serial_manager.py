import serial
import warnings
import serial.tools.list_ports
from time import sleep
from util import util
import numpy as np


class SerialManager:
    def __init__(self):
        self.data_source = SerialManager.__get_serial_port()
        self.calibration_data = util.get_calibration_data(self.data_source)

    # ------------------------ Auto Detect Port --------------------------- #
    @staticmethod
    def __auto_detect_port():

        ports = [
            p.device
            for p in serial.tools.list_ports.comports()
            if 'CP2102' in p.description  # may need tweaking to match arduino
        ]
        if not ports:
            raise IOError("No Device found!")
        if len(ports) > 1:
            warnings.warn('Multiple Device found - using the first')
        return ports[0]

    # ------------------------ Get Serial Port --------------------------- #
    @staticmethod
    def __get_serial_port():
        port = SerialManager.__auto_detect_port()
        # port = '/dev/ttyUSB0'
        ser = serial.Serial(port=port,
                            baudrate=115200,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            timeout=1,
                            xonxoff=0,
                            rtscts=0)

        ser.dtr = False
        sleep(1)
        ser.reset_input_buffer()
        ser.dtr = True
        sleep(1)

        return ser

    def process_serial_data(self, canvas, callback):
        try:
            values = self.data_source.readline().decode('utf-8').rstrip().split(',')
            values = np.array(list(map(float, values)))
            callback(canvas, self.calibration_data, values)

        except ValueError:
            pass
        except KeyboardInterrupt:
            exit(0)

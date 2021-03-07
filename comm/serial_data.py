import serial
import warnings
import serial.tools.list_ports
from time import sleep


class SerialData:
    def __init__(self):
        pass

    @staticmethod
    def port_auto_detect():

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

    def get_serial_port(self):
        port = self.port_auto_detect()
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
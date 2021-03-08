from comm import SerialManager
from comm import SerialData
from ui import Canvas
from util import util


def main():
    # _______________________ Serial ______________________ #
    data_source = SerialManager.get_serial_port()
    calibration_data = util.get_calibration_data(data_source)
    serial_data = SerialData(data_source, calibration_data)

    # ________________________ UI _______________________ #
    ui = Canvas()
    ui.add_serial_data_source(serial_data)
    ui.run()


if __name__ == '__main__':
    main()

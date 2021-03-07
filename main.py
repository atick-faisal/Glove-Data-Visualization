from ui import Canvas
from comm import SerialData


def main():
    serial_port = SerialData().get_serial_port()
    ui = Canvas(data_source=serial_port)
    ui.run()


if __name__ == '__main__':
    main()

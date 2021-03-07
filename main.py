from ui import Canvas
from comm import SerialData


def main():
    ser = SerialData().get_serial_port()
    canvas = Canvas(ser)
    canvas.run()


if __name__ == '__main__':
    main()

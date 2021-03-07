import numpy as np


def get_rotation_matrix(w, x, y, z):
    # Calculates the rotation matrix
    # Returns a 9x1 size array
    # Each row of the array contains the 9 elements of the corresponding rotation matrix
    # Required Argument(s):
    #     - w, x, y, z : Quaternion parameters

    rotation_matrix = np.zeros((9,))

    rotation_matrix[0] = 1 - 2 * (y ** 2 + z ** 2)
    rotation_matrix[4] = 1 - 2 * (x ** 2 + z ** 2)
    rotation_matrix[8] = 1 - 2 * (x ** 2 + y ** 2)

    rotation_matrix[2] = 2 * (x * z + w * y)
    rotation_matrix[3] = 2 * (x * y + w * z)
    rotation_matrix[7] = 2 * (y * z + w * x)

    rotation_matrix[1] = 2 * (x * y - w * z)
    rotation_matrix[5] = 2 * (y * z - w * x)
    rotation_matrix[6] = 2 * (x * z - w * y)

    return rotation_matrix


def get_rotation_angles(w, x, y, z):
    rm = get_rotation_matrix(w, x, y, z)
    yaw = np.arctan(rm[3] / rm[0])
    pitch = np.arctan(-rm[6] / np.sqrt(rm[7] ** 2 + rm[8] ** 2))
    roll = np.arctan(rm[7] / rm[8])
    rotation_angles = (np.array([yaw, pitch, roll]) + np.pi) * 50
    return rotation_angles


def get_calibration_data(data_source):
    i = 0
    buffer = np.zeros((500, 30))
    while i < 400:
        try:
            values = data_source.readline().decode('utf-8').rstrip().split(',')
            values = list(map(float, values))
            buffer[i, :] = np.array(values)
            i = i + 1

        except KeyboardInterrupt:
            exit(0)

        except ValueError:
            pass

    calibration_data = np.median(buffer, axis=0)
    return calibration_data

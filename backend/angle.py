import numpy as np

# Helper function to get degrees from coordinate

def get_degrees_from_coordinate(num1, num2):
    slope = np.divide(np.abs(num1), np.abs(num2))

    slope_arc_tan = np.arctan(slope)

    slope_to_degrees = np.degrees(slope_arc_tan)

    return slope_to_degrees


# given two points A & B on the screen with (X1, Y1) and (X2, Y2) respectively
# the absolute saccade slope = |(Y2-Y1)|/|(X2-X1)|
# and the absolute saccade arctangent = arctan(slope)
# finally turn the arctangent into degrees
# in the rare cases where the fixation B is a straight vertical line to fixation A,
# in other words, A and B have the same X value,
# 90 degrees is returned as the absolute angle (with respect to X axis) since we cannot divide numbers by zero.


def get_all_absolute_angles(all_coordinates):
    all_absolute_angles = []

    for index, value in enumerate(all_coordinates):
        curr_coordinate = all_coordinates[index]

        if (index+1) < len(all_coordinates):
            next_coordinate = all_coordinates[index+1]

            Y_diff = np.subtract(next_coordinate[1], curr_coordinate[1])
            X_diff = np.subtract(next_coordinate[0], curr_coordinate[0])

            if X_diff == 0:
                absolute_degrees = 90.00
            elif Y_diff == 0:
                absolute_degrees = 0.0
            else:
                absolute_degrees = get_degrees_from_coordinate(Y_diff, X_diff)

            all_absolute_angles.append(absolute_degrees)

    return all_absolute_angles

# given three points A, B and C with (X1, Y1) (X2, Y2) and (X3, Y3) respectively
# the relative saccade angle = 180 degrees - ( arctan(|(Y2-Y1)/(X2-X1)|).toDegrees + arctan(|(Y3-Y2)/(X3-X2)|).toDegrees )
# in cases where X1=X2=X3, the relative angle is 0 degree


def get_all_relative_angles(all_coordinates):
    all_relative_angles = []

    for index, value in enumerate(all_coordinates[:-2], 1):
        prev_coordinate = all_coordinates[index-1]
        curr_coordinate = all_coordinates[index]
        next_coordinate = all_coordinates[index + 1]

        Y_diff_A_B = np.subtract(curr_coordinate[1], prev_coordinate[1])
        X_diff_A_B = np.subtract(curr_coordinate[0], prev_coordinate[0])

        Y_diff_B_C = np.subtract(next_coordinate[1], curr_coordinate[1])
        X_diff_B_C = np.subtract(next_coordinate[0], curr_coordinate[0])

        if (X_diff_A_B == 0 and X_diff_B_C == 0) or (Y_diff_A_B == 0 and Y_diff_B_C == 0):
            relative_degrees = 180.0

        elif (X_diff_A_B == 0 and Y_diff_B_C < 0):
            relative_degrees = np.subtract(
                180.0, np.abs(get_degrees_from_coordinate(X_diff_B_C, Y_diff_B_C)))

        elif (X_diff_A_B == 0 and Y_diff_B_C > 0):
            relative_degrees = get_degrees_from_coordinate(
                X_diff_B_C, Y_diff_B_C)

        elif (X_diff_B_C == 0 and Y_diff_A_B < 0):
            relative_degrees = np.subtract(
                180.0, np.abs(get_degrees_from_coordinate(X_diff_A_B, Y_diff_A_B)))

        elif (X_diff_B_C == 0 and Y_diff_A_B > 0):
            relative_degrees = get_degrees_from_coordinate(
                X_diff_A_B, Y_diff_A_B)

        elif (Y_diff_A_B == 0 and X_diff_B_C < 0):
            relative_degrees = get_degrees_from_coordinate(
                Y_diff_B_C, X_diff_B_C)

        elif (Y_diff_B_C == 0 and X_diff_A_B < 0):
            relative_degrees = get_degrees_from_coordinate(
                Y_diff_A_B, X_diff_A_B)

        else:
            f_degree = np.abs(get_degrees_from_coordinate(Y_diff_A_B, X_diff_A_B))
            s_degree = np.abs(get_degrees_from_coordinate(Y_diff_B_C, X_diff_B_C))
            relative_degrees = 180.0 - f_degree - s_degree

        all_relative_angles.append(relative_degrees)

    return all_relative_angles

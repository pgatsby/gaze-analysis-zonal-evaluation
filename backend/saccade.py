import numpy as np


def get_all_saccade_length(all_coordinates):
    all_saccade_lengths = []

    for index, value in enumerate(all_coordinates):
        prev_coordinate = all_coordinates[index]

        if (index + 1) < len(all_coordinates):
            curr_coordinate = all_coordinates[index + 1]

            if (prev_coordinate[2] == curr_coordinate[2] - 1):
                all_saccade_lengths.append(np.sqrt(
                    np.add(np.power((np.subtract(curr_coordinate[0], prev_coordinate[0])), 2), np.power(
                        np.subtract(curr_coordinate[1], prev_coordinate[1]), 2))
                ))

    return all_saccade_lengths


def get_all_saccade_durations(saccade_details):
    all_saccade_duration = []

    for index, value in enumerate(saccade_details):
        prev_saccade_detail = saccade_details[index]

        if (index+1) < len(saccade_details):
            curr_saccade_detail = saccade_details[index + 1]

            if (prev_saccade_detail[2] == curr_saccade_detail[2] - 1):
                prev_saccade_timestamp = prev_saccade_detail[0]
                prev_fixation_duration = prev_saccade_detail[1]
                curr_saccade_timestamp = curr_saccade_detail[0]

                saccade_duration = np.subtract(curr_saccade_timestamp, np.add(
                    prev_saccade_timestamp, prev_fixation_duration))
                
                all_saccade_duration.append(saccade_duration)
    
    return all_saccade_duration

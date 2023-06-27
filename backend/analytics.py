import os
import pandas as pd
import numpy as np
from scipy.spatial import ConvexHull

from saccade import get_all_saccade_length, get_all_saccade_durations

def process_fixation(input_file, output_file, SCREEN_WIDTH=1920, SCREEN_HEIGHT=1080):

    # Load the data from csv file
    df = pd.read_csv(input_file)

    # Initialize lists for calculations
    all_fixation_duration = []
    all_coordinates = []
    all_points = []
    saccade_details = []

    timestamp_col_name = df.filter(regex='TIME.*').columns.to_list()[0]

    for index, row in df.iterrows():

        # Get each fixation's duration
        fixation_duration_seconds = row['FPOGD']
        fixation_id = row['FPOGID']

        # Get each fixation's (X, Y) coordinates
        x = row['FPOGX'] * SCREEN_WIDTH
        y = row['FPOGY'] * SCREEN_HEIGHT

        each_point = np.array([x, y])

        each_coordinate = np.array([x, y, fixation_id])

        # Get timestamp of each fixation
        timestamp = row[timestamp_col_name]

        each_saccade_detail = np.array([timestamp, fixation_duration_seconds, fixation_id])

        all_fixation_duration.append(fixation_duration_seconds)
        all_coordinates.append(each_coordinate)
        all_points.append(each_point)
        saccade_details.append(each_saccade_detail)

    all_saccade_lengths = get_all_saccade_length(all_coordinates)

    all_saccade_durations = get_all_saccade_durations(saccade_details)

    output_df = pd.Series({
        'Total Number of Fixations' : df.shape[0], # Returns number of rows (-1 for the)
        'Sum of All Fixation Duration': np.sum(all_fixation_duration), 
        'Mean Fixation Duration (MS)' : np.mean(all_fixation_duration),
        'Median Fixation Duration (MS)': np.median(all_fixation_duration),
        'StDev of Fixation Duration (MS)': np.std(all_fixation_duration),
        'Min. Fixation Duration (MS)': np.min(all_fixation_duration),
        'Max. Fixation Duration (MS)': np.max(all_fixation_duration), 
        'Total Number of Saccades' : len(all_saccade_lengths),
        'Sum of All Saccade Lengths' : np.sum(all_saccade_lengths),
        'Mean Saccade Length' : np.mean(all_saccade_lengths),
        'Median Saccade Length' : np.median(all_saccade_lengths),
        'StDev of Saccade Lengths' : np.std(all_saccade_lengths),
        'Min. Saccade Length': np.min(all_saccade_lengths),
        'Max. Saccade Length' : np.max(all_saccade_lengths),
        'Sum of All Saccade Durations' : np.sum(all_saccade_durations),
        'Mean Saccade Duration' : np.mean(all_saccade_durations), 
        'Median Saccade Duration' : np.median(all_saccade_durations),
        'StDev of Saccade Duration' : np.std(all_saccade_durations),
        'Min. Saccade Duration': np.min(all_saccade_durations),
        'Max. Saccade Duration' : np.max(all_saccade_durations),
    })

    print(output_df)

    # print(len(get_all_saccade_length(all_coordinates)))

process_fixation("/Users/pgatsby/Downloads/p1/cleansed_data/p1_cleansed_fixation.csv", "/Users/pgatsby/Desktop/output_file.csv", 1920, 1080)
process_fixation("/Users/pgatsby/Desktop/test/inputFiles/test_cleansed_fixation.csv", "/Users/pgatsby/Desktop/output_file.csv", 1920, 1080)


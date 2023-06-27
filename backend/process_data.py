import os
import pandas as pd
import numpy as np

# This funciton will clean the data and check the valdity of the pupils. 

def clean_data(input_files, dir, SCREEN_WIDTH=1920, SCREEN_HEIGHT=1080):
    participant_name = os.path.basename(dir)
    dir_prefix = os.path.join(dir, "cleansed_data", f"{participant_name}_cleansed")
    output_files =  [f"{dir_prefix}_all_gaze.csv", f"{dir_prefix}_fixation.csv"]

    try:
        os.makedirs(os.path.join(dir, "cleansed_data"))
    except Exception as e: 
        print(e)

    for i, input_file in enumerate(input_files):
        print(f"cleaning {input_file}")

        df = pd.read_csv(input_file)

        # Ensure required columns exist in data
        required_columns = ["FPOGV", "FPOGID", "SACCADE_DIR", "FPOGX", "FPOGY", "LPMMV", "RPMMV", "LPMM", "RPMM", "SACCADE_MAG"]
        missing_columns = set(required_columns) - set(df.columns)

        if missing_columns:
            print(f"Data file does not contain required columns: {', '.join(missing_columns)}")
            exit(1)

        df_new = df.copy()

        # Check for on screen and valid pupil sizes
        on_screen = ((df['FPOGX'] <= 1.0) & (df['FPOGX'] >= 0) & (df['FPOGY'] <= 1.0) & (df['FPOGY'] >= 0))
        pupil_left_valid = df['LPMMV'] == 1
        pupil_right_valid = df['RPMMV'] == 1
        pupil_sizes_possible = ((df['LPMM'] >= 2) & (df['LPMM'] <= 8) & (df['RPMM'] >= 2) & (df['RPMM'] <= 8))
        pupil_size_difference_valid = np.abs(df['RPMM'] - df['LPMM']) <= 1

        # Combine the conditions to find valid data
        valid_data = on_screen & pupil_left_valid & pupil_right_valid & pupil_sizes_possible & pupil_size_difference_valid

        # Apply the condition to the DataFrame
        df_new = df_new[valid_data]

        # Save the cleansed data to a new CSV file
    
        df_new.to_csv(output_files[i], index=False)

        print(f"{output_files[i]} completed")
    
    return output_files

    
clean_data(["/Users/pgatsby/Downloads/p1/Esther Jung_all_gaze.csv", "/Users/pgatsby/Downloads/p1/Esther Jung_fixations.csv"],
             "/Users/pgatsby/Downloads/p1")
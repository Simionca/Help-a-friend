import os
import shutil

# Path to the input file
input_file_path = r"output_folder\final_final_output.txt"

# Path to the folder where output files will be created
output_folder_path = r"routes"

# Get the total number of files in the output folder
num_output_files = len(os.listdir(output_folder_path))

# Open the input file
with open(input_file_path, "r") as input_file:
    # Read the lines of the input file
    lines = input_file.readlines()

    # Calculate the number of lines per output file
    num_lines_per_file = len(lines) // num_output_files

    # Create output files and distribute the lines
    for i in range(num_output_files):
        # Calculate the start and end indices for the lines for this output file
        start_index = i * num_lines_per_file
        end_index = start_index + num_lines_per_file

        # If this is the last output file, give it all remaining lines
        if i == num_output_files - 1:
            end_index = len(lines)

        # Get the lines for this output file
        file_lines = lines[start_index:end_index]

        # Create the output file
        output_file_path = os.path.join(output_folder_path, f"output_file_{i+1}.txt")
        with open(output_file_path, "w") as output_file:
            # Write the lines to the output file
            output_file.writelines(file_lines)

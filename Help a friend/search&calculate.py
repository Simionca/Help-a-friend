import os
import re

def calculate_sum_and_append(file_lines):
    total_sum = 0
    for line in file_lines:
        number_match = re.search(r'\d+$', line.strip())
        if number_match:
            total_sum += int(number_match.group())
    file_lines.append(f'sum={total_sum}\n')
    return file_lines

# Read input file
with open(r'output_folder\final_final_output.txt', 'r') as f:
    input_lines = f.readlines()

# Read the 9 files into a list
folder_path = r'routes/'
files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
file_contents = []

for file in files:
    with open(file, 'r') as f:
        file_contents.append(f.readlines())

# Iterate through each line in the input file
for line in input_lines:
    # Extract the string at the start of the line and the number at the end
    input_match = re.match(r'^(.+?)\s+(\d+)$', line.strip())
    if input_match:
        input_string, input_number = input_match.groups()

        # Iterate through the 9 files
        for i, file_lines in enumerate(file_contents):
            # Search for a match in each file and update the number at the end
            for j, file_line in enumerate(file_lines):
                file_match = re.match(r'^(.+?)\s+(\d+)$', file_line.strip())
                if file_match:
                    file_string, file_number = file_match.groups()
                    if input_string == file_string:
                        file_contents[i][j] = f'{input_string} {input_number}\n'
                        break
# Calculate the sum and append it to the end of each file
for i, file_lines in enumerate(file_contents):
    file_contents[i] = calculate_sum_and_append(file_lines)


# Write the updated contents back to the 9 files
for i, file in enumerate(files):
    with open(file, 'w') as f:
        f.writelines(file_contents[i])

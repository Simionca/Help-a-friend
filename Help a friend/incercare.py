import os

def remove_last_num(count):
    return count[:len(count) - 1]

input_files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']

# Create output folder if it doesn't exist
if not os.path.exists('output_folder'):
    os.mkdir('output_folder')

all_data = []

for i, input_file in enumerate(input_files):
    # Parse the original file and save the output
    with open(input_file, 'r') as f:
        lines = f.readlines()

    data = []

    for line in lines:
        fields = line.split('<td>')
        fields = [field.strip('</td>\n') for field in fields if '</td>' in field]
        if len(fields) >= 9:
            data.append(fields[0] + ' ' + fields[8])

    output_file = os.path.join('output_folder', 'output' + str(i+1) + '.txt')
    with open(output_file, 'w') as f:
        for row in data:
            f.write(row + '\n')

    # Re-parse the output file and extract the location name and count
    with open(output_file, 'r') as f:
        lines = f.readlines()

    new_data = []

    for line in lines:
        name_count = line.split('</td><td class="  column-right">')
        if 'report_expandable' in name_count[0]:
            name = name_count[0].split('report_expandable">')[1]
            count = name_count[1].strip()
            count = remove_last_num(count)
            new_data.append([name, count])

    all_data.extend(new_data)

# Sort all_data alphabetically based on the location names
all_data.sort(key=lambda x: x[0])

# Save the sorted data to the final_final_output file
output_file = os.path.join('output_folder', 'final_final_output.txt')
with open(output_file, 'w') as f:
    for row in all_data:
        if row[0].startswith('easybox '):
            row[0] = row[0].replace('easybox ', '')
        f.write(row[0] + ' ' + row[1] + '\n')

# Delete all other intermediate files
for i in range(len(input_files)):
    os.remove(os.path.join('output_folder', 'output' + str(i+1) + '.txt'))
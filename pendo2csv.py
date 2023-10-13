import csv
import os

# Helper function to determine if a line is a date-type line
def is_date_type_line(line):
    return ',' in line and '-' in line and any(char.isdigit() for char in line)

# Define the path to your text file and CSV file in the current directory
current_directory = os.getcwd()
txt_file_path = os.path.join(current_directory, "文本.txt")
csv_file_path = os.path.join(current_directory, "notes.csv")

# Parse the text file and extract notes
notes = []
with open(txt_file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Define variables to track the state
in_note = False
current_note = {}
content_lines = []

# Iterate over each line in the file
for line in lines:
    line = line.strip()

    # If we encounter a date-type line
    if is_date_type_line(line):
        # If we're already in the middle of a note, we finalize the current note
        if in_note:
            current_note["笔记内容"] = "\n".join(content_lines).strip()
            notes.append(current_note)
            current_note = {}
            content_lines = []

        date, rest = line.split(',', 1)
        time_, type_ = rest.split('-', 1)
        current_note["日期"] = date.strip()
        current_note["时间"] = time_.strip()
        current_note["类型"] = type_.strip()
        in_note = True
    # If it's a field line
    elif line.startswith(':'):
        key, value = line.split(':', 2)[1:]
        current_note[key.strip()] = value.strip()
    # If it's a content line or blank line
    else:
        content_lines.append(line)

# Handle the last note, if any
if current_note:
    current_note["笔记内容"] = "\n".join(content_lines).strip()
    notes.append(current_note)

# Extract all unique fieldnames from the notes to ensure all fields are covered in the CSV file
all_fieldnames = set()
for note in notes:
    all_fieldnames.update(note.keys())

# Create the CSV file with all notes and all possible fields
with open(csv_file_path, "w", encoding="utf-8", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=sorted(all_fieldnames))
    writer.writeheader()
    for note in notes:
        writer.writerow(note)

print(f"CSV file has been created at: {csv_file_path}")

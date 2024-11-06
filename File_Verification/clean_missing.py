import json
import os
import random

# Paths to the original metadata and audio directory
metadata_train_path = "D:\\Projects\\VITS_Speech_Synthesis\\data\\IndicVoices-R\\Telugu\\metadata_train.json"
wavs_dir = "D:\\Projects\\VITS_Speech_Synthesis\\data\\IndicVoices-R\\Telugu\\wavs"
train_output_path = "D:\\Projects\\VITS_Speech_Synthesis\\data\\IndicVoices-R\\Telugu\\metadata_train_cleaned.json"
test_output_path = "D:\\Projects\\VITS_Speech_Synthesis\\data\\IndicVoices-R\\Telugu\\metadata_test_cleaned.json"

def clean_and_split_metadata(metadata_path, wavs_dir, train_output, test_output, test_ratio=0.1):
    # Read the original metadata file
    with open(metadata_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    valid_entries = []  # List to store valid entries
    missing_files = []  # List to store paths of missing files

    # Check for each entry if the corresponding file exists
    for line in lines:
        data = json.loads(line)
        filepath = os.path.join(wavs_dir, data["filepath"])

        # Check if the file exists in the wavs directory
        if os.path.isfile(filepath):
            valid_entries.append(data)  # Add valid entry to the list
        else:
            missing_files.append(data["filepath"])  # Track missing files

    # Shuffle the valid entries randomly
    random.shuffle(valid_entries)

    # Split the data into train and test based on the specified ratio
    split_index = int(len(valid_entries) * (1 - test_ratio))
    train_entries = valid_entries[:split_index]
    test_entries = valid_entries[split_index:]

    # Write the cleaned training data to the output JSON file
    with open(train_output, 'w', encoding='utf-8') as f_train:
        for entry in train_entries:
            json.dump(entry, f_train, ensure_ascii=False)
            f_train.write('\n')

    # Write the cleaned test data to the output JSON file
    with open(test_output, 'w', encoding='utf-8') as f_test:
        for entry in test_entries:
            json.dump(entry, f_test, ensure_ascii=False)
            f_test.write('\n')

    # Output statistics about the process
    print(f"Cleaned training metadata saved to {train_output} with {len(train_entries)} entries.")
    print(f"Cleaned test metadata saved to {test_output} with {len(test_entries)} entries.")
    if missing_files:
        print(f"{len(missing_files)} files were missing and removed from metadata.")
    else:
        print("No missing files found.")

# Run the cleaning and splitting function
clean_and_split_metadata(metadata_train_path, wavs_dir, train_output_path, test_output_path, test_ratio=0.1)

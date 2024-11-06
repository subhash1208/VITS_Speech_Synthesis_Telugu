import json
import os

# Paths to the metadata files
metadata_train_path = "D:\\Projects\\VITS_Speech_Synthesis\\data\\IndicVoices-R\\Telugu\\metadata_train.json"
metadata_test_path = "D:\\Projects\\VITS_Speech_Synthesis\\data\\IndicVoices-R\\Telugu\\metadata_test.json"
wavs_dir = "D:\\Projects\\VITS_Speech_Synthesis\\data\\IndicVoices-R\\Telugu\\wavs"

def verify_audio_paths(metadata_path, wavs_dir, output_filename):
    with open(metadata_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Open the output file in write mode
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        missing_files = []
        for line in lines:
            data = json.loads(line)
            filepath = os.path.join(wavs_dir, data["filepath"])
            if not os.path.isfile(filepath):
                missing_files.append(filepath)

        # Write missing file information to the output file
        if missing_files:
            output_file.write(f"Missing {len(missing_files)} files:\n")
            for missing_file in missing_files:
                output_file.write(missing_file + "\n")
        else:
            output_file.write(f"All files in {metadata_path} are verified to be present.\n")

# Run verification for both train and test metadata
verify_audio_paths(metadata_train_path, wavs_dir, "File_Verification\outputs\missing_files_train.txt")
verify_audio_paths(metadata_test_path, wavs_dir, "File_Verification\outputs\missing_files_test.txt")

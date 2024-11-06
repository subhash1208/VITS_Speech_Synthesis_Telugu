
# VITS Speech Synthesis for Telugu

This project aims to build a Variational Inference Text-to-Speech (VITS) model to synthesize Telugu speech. Below is a step-by-step guide on how the preprocessing is done, starting from setting up the project to cleaning and splitting the dataset.

---

## Table of Contents

1. [Project Setup](#project-setup)
2. [Download and Organize Dataset](#download-and-organize-dataset)
3. [Data Cleaning and Splitting](#data-cleaning-and-splitting)
4. [Next Steps](#next-steps)

---

## 1. Project Setup


### Step 1: **Set Up Your Python Environment in VS Code**
1. **Clone this repo**:
```git bash


2. **Open VS Code** and create a new folder for your project, for example, `VITS_Speech_Synthesis`.
3. **Create a Virtual Environment**:
   - In VS Code’s integrated terminal, navigate to your project folder.
   - Run the following command to create a virtual environment named `venv` using Python 3.11 (since VITS and dependencies are more likely to be compatible with Python 3.11):
     ```bash
     python3.11 -m venv venv
     ```
   - **Activate the virtual environment**:
     - On **Windows**:
       ```bash
       .\venv\Scripts\activate
       ```
     - On **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

4. **Install Required Libraries**:
   - With the virtual environment active, install the required libraries for VITS, audio processing, and WebSocket streaming:
     ```bash
     pip install torch torchaudio numpy librosa websockets soundfile ffmpeg-python
     ```
   
### Step 2: **Clone the VITS Repository**

1. In your terminal (still in the project directory), clone the VITS repository:
   ```bash
   git clone https://github.com/jaywalnut310/vits.git
   ```
2. Navigate into the VITS folder:
   ```bash
   cd vits
   ```
   
3. **Install Additional Requirements for VITS**:
   - Inside the `vits` folder, install any additional dependencies required by the VITS model:
     ```bash
     pip install -r requirements.txt
     ```

Let me know when you’re set with these steps, and we’ll proceed with data acquisition from the AI4Bharat corpus!
### Directory Structure

Your project directory should look like this:

```
VITS_Speech_Synthesis_Telugu/
│
├── data/
│   └── IndicVoices-R/
│       └── Telugu/
│           ├── metadata_train.json
│           ├── metadata_test.json
│           ├── metadata_train_cleaned.json
│           ├── metadata_test_cleaned.json
│           └── wavs/
│               └── [Audio files here]
├── vits_model/
└── README.md
```

## 2. Download and Organize Dataset

You will need a dataset of Telugu audio files for this project. We are using the **IndicVoices-R** dataset, which contains audio files and corresponding metadata.

- **Step 1**: Download the **IndicVoices-R(Telugu.tar - 87GB)** dataset.Extract it according to the directory structure shown above. Ensure you have the directory structure shown above, where the `wavs/` folder contains all the Telugu audio files in `.wav` format.

- **Step 2**: The metadata files `metadata_train.json` and `metadata_test.json` are necessary for the training and testing of the model. These files contain information about each audio file, such as the file path and the corresponding transcript.
- **Step 3**: Run the `File_Verification/verify_paths.py` to check the missing files 

---

## 3. Data Cleaning and Splitting

In this section, we will clean the metadata by removing entries where the corresponding audio file is missing, shuffle the data, and split it into training and testing sets.

### Data Preprocessing Script

Run the preprocessing notebook cell by cell 

### Explanation:

1. **Input Data**: 
   - `metadata_train.json`: Original metadata for the training set.
   - `metadata_test.json`: Original metadata for the testing set.
   - `wavs_dir`: Directory containing audio files (WAV format).

2. **Process**:
   - We read the metadata files and check if each referenced audio file exists in the `wavs/` directory.
   - If the file exists, it is added to a list of valid entries. Missing files are logged for review.
   - The valid entries are shuffled randomly and then split into training and testing sets. We use 90% of the data for training and 10% for testing (this ratio is adjustable).
   - The cleaned metadata is then saved into new files: `metadata_train_cleaned.json` and `metadata_test_cleaned.json`.

3. **Output**:
   - A message is printed showing how many entries were included in the cleaned training and test sets.
   - Any missing files are also reported.

---


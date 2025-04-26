# Project Setup Guide

This guide outlines the steps to set up, prepare the dataset, and run the backend server for this project using Anaconda/Miniconda.

## 1. Prerequisites: Install Anaconda or Miniconda

This project uses Conda to manage environments and dependencies, defined in:

- `environment.yml` (for Windows/Linux)
- `environment-mac.yml` (for macOS)

You need to have either Anaconda or Miniconda installed.

- **Anaconda:** A full distribution including Conda, Python, and many scientific packages.
- **Miniconda:** A minimal installer containing only Conda, Python, and their essential dependencies.

Choose one and download it from the official website:

- **Download Anaconda:** [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
- **Download Miniconda:** [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

Follow the installation instructions for your operating system provided on the download pages. After installation, open your terminal (Anaconda Prompt on Windows, or your standard terminal on macOS/Linux) to verify the installation:

```sh
conda --version
```

---

## 2. Download and Prepare the BreaKHis Dataset

> **Optional:** If you only want to use the pre‑trained CNN model, you can skip Steps 2 (dataset download/preparation) and 5 (training)—the ready-to-go model files are provided in `OncoVision/ai/models`.


### 2.1. Download the Images

1. Go to the Kaggle dataset page: [https://www.kaggle.com/datasets/ambarish/breakhis?select=BreaKHis\_v1](https://www.kaggle.com/datasets/ambarish/breakhis?select=BreaKHis_v1)
2. Download the ZIP file (`BreaKHis_v1.zip`) containing all histology-slide images.

### 2.2. Extract and Clean Up

1. Move the downloaded `BreaKHis_v1.zip` into the `OncoVision/back-end` directory.

2. Extract the ZIP file in that directory.

   ```sh
   cd OncoVision/back-end
   unzip BreaKHis_v1.zip
   ```

3. **Important:** After extraction, you may see a nested folder structure like:

   ```text
   OncoVision/back-end/BreaKHis_v1/BreaKHis_v1/histology_slides/...
   ```

   If that's the case, rename or delete the extra `BreaKHis_v1` layer so that the path to an image looks like:

   ```text
   BreaKHis_v1/histology_slides/breast/benign/.../100X/SOB_B_A-14-22549AB-100-001.png
   ```

### 2.3. Organize Images into Train/Test Folders

A helper script `fileUtils.py` is provided to read the CSV metadata and copy images into:

```
./ai/dataset/
  ├── train/
  │   ├── benign/
  │   └── malignant/
  └── test/
      ├── benign/
      └── malignant/
```

Ensure the CSV file `breast-cancer-images.csv` is placed in:

```
OncoVision/back-end/ai/dataset/breast-cancer-images.csv
```

Then run:

```sh
cd OncoVision/back-end
python fileUtils.py
```

The `fileUtils.py` script content:

```python
import os
import shutil
import pandas as pd

# Define paths
csv_file = './ai/dataset/breast-cancer-images.csv'  # OncoVision/back-end directory
base_dir   = './ai/dataset'
source_root = './ai'

# Load the CSV file
df = pd.read_csv(csv_file, header=0, names=['fold', 'magnifying', 'dataset_type', 'image_path'])

# Determine class from filename
print("Processing dataset. This may take a while...")
def get_class_label(image_path):
    if 'benign' in image_path.lower():
        return 'benign'
    elif 'malignant' in image_path.lower():
        return 'malignant'
    else:
        return None

# Process each row in the DataFrame
for _, row in df.iterrows():
    dataset_type = row['dataset_type'].lower()
    image_path   = row['image_path']
    class_label  = get_class_label(image_path)

    if class_label is None:
        print(f"Skipping file with unknown class: {image_path}")
        continue

    # Construct source and destination paths
    src_path  = os.path.join(source_root, image_path)
    dest_dir  = os.path.join(base_dir, dataset_type, class_label)
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, os.path.basename(image_path))

    try:
        shutil.copy2(src_path, dest_path)
    except FileNotFoundError:
        print(f"Source file not found: {src_path}")
    except Exception as e:
        print(f"Error copying {src_path} to {dest_path}: {e}")

print("Dataset processing completed.")
```

---

## 3. Create the Conda Environment

Use the appropriate `.yml` file to create the Conda environment. This command will create an environment called `OncoVision`.

- **On Windows or Linux:**

  ```bash
  conda env create -f environment.yml
  ```

- **On macOS:**

  ```bash
  conda env create -f environment-mac.yml
  ```

This process might take a few minutes as Conda resolves and downloads the required packages.

## 4. Activate the Conda Environment

Once the environment is created, activate it:

```bash
conda activate OncoVision
```

## 5. Train the CNN Model

The training script `train_cnn.py` contains the code to train your CNN model. Run it from the `back-end` directory:

```bash
cd OncoVision/back-end
python train_cnn.py
```

The script will load images from `./ai/dataset/train`, apply preprocessing and augmentation, and save the best model to:

```
./ai/models/cnn_model.keras
```

## 6. Run the Backend Server

Once all dependencies are installed and the dataset is organized, start the backend server by running:

```bash
flask run --debug
```

The backend should now be running and ready for use!

## 7. Verify the Setup

To confirm that the backend is running correctly, make a `GET` request to `http://127.0.0.1:5000/api/status` using Postman or `curl`.

- **Using Postman:** Send a `GET` request to `http://127.0.0.1:5000/api/status`.
- **Using ****`curl`****:** Run the following command in your terminal:
  ```sh
  curl -X GET http://127.0.0.1:5000/api/status
  ```

You should receive a JSON response:

```json
{
    "status": "ok",
    "statusCode": 200
}
```

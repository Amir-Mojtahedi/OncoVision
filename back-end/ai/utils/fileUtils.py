import os
import shutil
import pandas as pd

# Define paths
csv_file = './ai/dataset/breast-cancer-images.csv' # Assuming you are currently in OncoVision/back-end directory
base_dir = './ai/dataset'            # Base directory for organized dataset
source_root = './ai'               # Root directory where original images are located

# Load the CSV file
df = pd.read_csv(csv_file, header=0, names=['fold', 'magnifying', 'dataset_type', 'image_path'])

# Function to determine class from filename
def get_class_label(image_path):
    if 'benign' in image_path.lower():
        return 'benign'
    elif 'malignant' in image_path.lower():
        return 'malignant'
    else:
        return None

# Process each row in the DataFrame
print("Processing dataset. This may take a while...")
for _, row in df.iterrows():
    dataset_type = row['dataset_type'].lower()
    image_path = row['image_path']
    class_label = get_class_label(image_path)

    if class_label is None:
        print(f"Skipping file with unknown class: {image_path}")
        continue

    # Construct source and destination paths
    src_path = os.path.join(source_root, image_path)
    dest_dir = os.path.join(base_dir, dataset_type, class_label)
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, os.path.basename(image_path))

    # Copy the file
    try:
        shutil.copy2(src_path, dest_path)
    except FileNotFoundError:
        print(f"Source file not found: {src_path}")
    except Exception as e:
        print(f"Error copying {src_path} to {dest_path}: {e}")

print("Dataset processing completed.")

# OncoVision
## Problem Definition

Breast cancer is a critical global health issue, with early detection playing a major role in increasing patient survival rates. Traditional methods of analyzing mammogram data are prone to human error and often require significant manual effort. The aim of this project, OncoVision, is to develop a hybrid AI system capable of classifying breast cancer tumours as benign or malignant by processing structured image-derived data and, in future iterations, raw mammogram images.

## Target Audience

OncoVision is designed to assist healthcare professionals, such as radiologists and oncologists, by providing a second-opinion diagnostic tool. Secondary stakeholders include patients, hospital administrators, and medical AI researchers.


# Report

## Abstract

OncoVision is an AI-powered system developed to assist in the early detection of breast cancer using medical imaging and machine learning algorithms. The system utilizes preprocessed patient data from mammograms and applies trained classification models such as Support Vector Machine (SVM), Decision Tree, Logistic Regression, and Random Forest to determine the likelihood of malignancy. A web-based interface built with React allows users to input data and view predictions in real-time. This tool aims to reduce diagnostic delays and support healthcare professionals with fast, reliable second opinions.

## Introduction

Breast cancer remains one of the leading causes of cancer-related deaths among women. Early detection is crucial in increasing survival rates. Traditional manual analysis of mammogram images can be time-consuming and prone to human error. OncoVision addresses this by providing an AI-assisted tool that classifies tumours as benign or malignant using image-derived data. The system combines machine learning, image preprocessing, and web technologies to deliver a user-friendly and effective solution.

## Dataset For Tabular ML Models

The dataset (`breast-cancer.csv`) contains 30 structured features derived from mammographic images (e.g., `radius`, `texture`, `symmetry`). Each row represents a tumour case, labelled as Malignant (`1`) or Benign (`0`).

### Data Preparation:

Removed ID column
Converted diagnosis to numeric (`M`→`1`, `B`→`0`)
Normalized all features using StandardScaler
Split into 80% training and 20% testing sets

## Dataset For CNN Image-Processing
Dataset for Image-Based Classification (CNN)
The image dataset used for CNN-based classification consists of over 11,000 labeled mammogram images, organized into subfolders by diagnosis: benign and malignant. Due to its large size (~4 GB), the dataset is not uploaded to the repository.

### Data Preparation:
- Loaded images from folder structure using `image_dataset_from_directory`
- Resized all images to `224`×`224` pixels to ensure consistent input shape
- Converted folder names to binary labels (benign → `0`, malignant → `1`)
- Split into 80% training and 20% validation using built-in `validation_split`
- Applied rescaling to normalize pixel values from `0`–`255` to a `0`–`1` range
- Used real-time data augmentation (`flip`, `rotation`, `zoom`, `contrast`) to improve model generalization
- Computed class weights to handle class imbalance during training


## Methodology
1. Preprocessing
 - Converted raw `CSV` input into a structured format
 -  Normalized numeric feature values using `StandardScaler`
 - Removed missing or redundant values
    
2. Feature Extraction
 - Based on structured features like `radius_mean`, `texture_mean`, `concavity_mean`, etc.
 - No manual feature engineering was required due to a clean dataset
 - (Image processing to be integrated in future work)

3. Modelling  
Five machine learning models were implemented and trained:
 - `svm.py`: Trains an SVM classifier
 - `DecisionTree.py`: Builds a decision tree model
 - `logisticModel.py`: Logistic regression-based classifier
 - `randomforestmodel.py`: Ensemble learning using Random Forest
 - `cnn.py`: Convolutional Neural Network (CNN) on mammogram image data

4. API Integration
 - `app.py` sets up a Flask backend that exposes a /predict endpoint
 - Receives patient data via `JSON` and routes it to the selected model
 - Returns binary classification result (“Malignant” or “Benign”)

5. Frontend Development
 - Developed using React (see `front-end/src/`)
 - App.js manages state and API communication
 - Users input feature values into a dynamic form
 - Submissions trigger API calls, and results are displayed clearly on-screen
 
6. CNN-Based Image Processing 
 - Loaded mammogram images (`224`×`224`) from directory using `image_dataset_from_directory`
 - Applied real-time data augmentation (`flip`, `rotation`, `zoom`, `contrast`)
 - Normalized pixel values with `Rescaling(1./255)`
 - Handled class imbalance using `compute_class_weight`
 - Built CNN with 4 convolutional blocks + BatchNorm + MaxPooling
 - Added `Dropout` and `Dense` layers with L2 regularization
 - Trained with Adam optimizer, binary crossentropy loss, and callbacks: EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
 - Saved best model as `cnn_model.keras`

## System Architecture
### 1. Tabular Data Classification  
<pre>  
[User Input (React Web Form)]
        ↓
[Frontend (App.jsx)]
        ↓  (HTTP fetch)
[Backend Flask Server (app.py)]
        ↓
[ML Models: SVM / Decision Tree / Random Forest / Logistic Regression]
        ↓
[Prediction Returned to UI]
 </pre>

### 2. Image-based Classification
<pre> 
[User Upload (Image File)]
        ↓
[Frontend (React + File Upload)]
        ↓
[Backend Flask Server (app.py)]
        ↓
[Pretrained CNN Model]
        ↓
[Malignant / Benign Prediction Returned to UI]
 </pre>

Users can switch between the two methods of classification

## Results

The results below were obtained from an  evaluation performed during development:
 - SVM: 96%
 - Decision Tree: 94%
 - Random Forest: 96%
 - Logistic Regression: 97%
 - CNN: 97%

## Success Criteria
| Model              | Accuracy | Precision (avg) | Recall (avg) | F1-Score (avg) |
|--------------------|----------|------------------|--------------|----------------|
| SVM                | 96%      | 0.96             | 0.96         | 0.96           |
| Random Forest      | 96%      | 0.96             | 0.96         | 0.96           |
| Decision Tree      | 94%      | 0.94             | 0.94         | 0.94           |
| Logistic Regression| 97%      | 0.97             | 0.97         | 0.97           |
| CNN                | 97%      | 0.97             | 0.97         | 0.97           |
## Challenges
 - Handling noisy or borderline cases in medical data
 - Ensuring compatibility between frontend form design and backend models
 - Avoiding overfitting due to class imbalance

## Future Work
 - Integrate with cloud storage for real hospital deployment use cases

## Conclusion
OncoVision has successfully demonstrated the power of combining classical ML models and CNN-based image processing for breast cancer diagnosis. With Logistic Regression and CNN both achieving `97` % accuracy, the tool supports both structured data classification and direct image-based diagnosis.
This hybrid approach allows real-time, reliable predictions for healthcare professionals. Future enhancements will include integrating image uploads from clinical systems, improving model explainability (e.g., heatmaps for CNN), and deploying models via secure cloud infrastructure.



# Datasets used
- https://www.kaggle.com/datasets/hayder17/breast-cancer-detection/data
- https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset
- https://www.kaggle.com/datasets/ambarish/breakhis?select=BreaKHis_v1
 

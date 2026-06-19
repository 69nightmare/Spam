# Spam Shield (Spam Detection System)

This project is an AI-powered Spam Detection system built with Python, Flask, and a Chrome Extension. It uses a Naive Bayes classifier to detect whether a message is safe (Ham) or a scam/spam.

## Features

- **Machine Learning Model:** Built using `scikit-learn` with a `MultinomialNB` classifier and `TfidfVectorizer`.
- **Flask Backend:** A lightweight API server that serves the prediction model.
- **Chrome Extension:** A user-friendly browser extension to quickly analyze suspicious messages.
- **Custom Datasets:** Includes scripts to add datasets from Kaggle and Indian scam/ham messages to improve model accuracy.

## Installation & Usage

### 1. Start the Backend Server

The machine learning model needs a backend server to process predictions.

1. Ensure you have Python installed.
2. Install the required dependencies:
   ```bash
   pip install pandas numpy scikit-learn nltk flask flask-cors
   ```
3. Run the Flask backend:
   ```bash
   python app.py
   ```
   *Note: The server must be running on `http://localhost:5000` for the extension to work.*

### 2. Install the Chrome Extension

1. Open Google Chrome and navigate to `chrome://extensions/`.
2. Enable **Developer mode** in the top right corner.
3. Click on **Load unpacked** in the top left.
4. Select the `extension/` folder located inside this project repository.
5. The "Spam Detector" extension will now be added to your browser.

### 3. Using the Extension

1. Click on the extension icon in your browser toolbar.
2. Paste any suspicious message into the text box.
3. Click **Analyze Message** to see if it's Safe or a High-Risk Scam!

## Additional Scripts

- `train_model.py`: Retrains the Naive Bayes model and saves it as `model.pkl` and `vectorizer.pkl`.
- `add_indian_scams.py`: Appends a custom list of Indian scam and normal messages to the dataset.
- `add_kaggle_dataset.py`: Downloads and merges a spam classification dataset from Kaggle.
- `clean_dataset.py`: Removes nulls, duplicates, and invalid entries from the dataset.
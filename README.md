# Spam Shield (Spam Detection System)

This project is an AI-powered Spam Detection system built with Python, Flask, and a Chrome Extension. It uses a Naive Bayes classifier to detect whether a message is safe (Ham) or a scam/spam.

## Tech Stack Used

- **Python**: Core programming language.
- **Flask & Flask-CORS**: Used to create a lightweight API server to expose the ML model.
- **Scikit-learn (sklearn)**: Machine Learning library used for model training (`MultinomialNB`) and feature extraction (`TfidfVectorizer`).
- **NLTK (Natural Language Toolkit)**: For text preprocessing, tokenization, removing stop words, and stemming.
- **Pandas & NumPy**: For data manipulation and arrays.
- **HTML/CSS/JavaScript**: Built the Chrome Extension frontend interface.

## Model Parameters & Specifications

- **Algorithm**: Multinomial Naive Bayes (`MultinomialNB`), ideal for discrete features like word counts.
- **Feature Extraction**: TF-IDF Vectorizer (`TfidfVectorizer`).
- **Number of Parameters/Features**: The model extracts and uses exactly **3000** maximum features/parameters (`max_features=3000` in the TF-IDF vectorizer). 

## Features

- **Machine Learning Model:** High-accuracy `MultinomialNB` model utilizing 3000 TF-IDF features to effectively classify messages.
- **Flask Backend API:** A local RESTful server that accepts POST requests and returns prediction probabilities in real time.
- **Chrome Extension UI:** A user-friendly browser extension that allows users to seamlessly paste messages and get instant analysis without leaving their tab.
- **Data Preprocessing:** Implements advanced NLP techniques, including Porter Stemming and stopword removal via NLTK.
- **Real-time Probability:** Gives users not just a safe/spam label, but the exact probability percentage of how likely it is to be a scam.

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

## Project Structure

- `app.py`: The Flask server that serves the pre-trained ML model.
- `train_model.py`: Script used to read the dataset, train the Naive Bayes model, and export the `model.pkl` and `vectorizer.pkl`.
- `spam.csv`: The cleaned dataset consisting of thousands of legitimate and spam/scam messages.
- `model.pkl` & `vectorizer.pkl`: Serialized model files loaded by the backend.
- `extension/`: Contains the frontend Chrome Extension logic (`popup.html`, `popup.css`, `popup.js`, `manifest.json`).
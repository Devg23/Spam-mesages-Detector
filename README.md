# SMS Spam Detector

📱 The SMS Spam Detector is a web application built using Streamlit that allows users to quickly identify whether a given message is SPAM or HAM (not spam). This tool utilizes natural language processing techniques and a pre-trained machine learning model to make accurate predictions.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Features

- User-friendly interface for inputting messages.
- Real-time predictions on whether a message is spam or ham.
- Animated background and stylish design for an enhanced user experience.

## Technologies Used

- **Python**: Programming language used for building the application.
- **Streamlit**: Framework for creating web applications.
- **NLTK**: Natural Language Toolkit for text processing.
- **Pickle**: For loading pre-trained models.
- **Pandas**: For data manipulation (if used in the model).

## Installation

To run the SMS Spam Detector locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Devg23/Spam-Messages-Detector.git
    cd Spam-Messages-Detector
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download NLTK resources**:
    ```python
    import nltk
    nltk.download('punkt')
    ```

4. **Ensure you have the necessary model files**:
    - `vector.pkl`: Pre-trained TF-IDF vectorizer.
    - `model.pkl`: Pre-trained classification model.

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Enter the message you want to check in the text area and click on the "🚀 Predict" button.

4. The result will be displayed indicating whether the message is SPAM or HAM.

## How It Works

The SMS Spam Detector uses the following steps to process and predict the input message:

1. **Text Preprocessing**: 
   - Converts text to lowercase.
   - Tokenizes the text.
   - Removes stop words and punctuation.
   - Applies stemming to reduce words to their root forms.

2. **Vectorization**:
   - The preprocessed text is transformed using a TF-IDF vectorizer.

3. **Prediction**:
   - The transformed text is fed into a pre-trained machine learning model to classify it as SPAM or HAM.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and create a pull request. Any suggestions or improvements are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️ using Streamlit

import streamlit as st
import pickle
import nltk
import string
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
from stops import words
nltk.download('punkt')

# Function to preprocess text
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for ch in text:
        if ch.isalnum():
            y.append(ch)
    text = y[:]
    y.clear()

    for i in text:
        if i not in words and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

# Load the pre-trained models
tfidf = pickle.load(open('vector.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Set page config (title, layout, etc.)
st.set_page_config(page_title="SMS Spam Detector", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    /* Background styling */
    .main {
        background: linear-gradient(to right, #74ebd5, #acb6e5);
        font-family: 'Poppins', sans-serif;
    }

    /* Center the title and subheader */
    h1, h2, h3 {
        text-align: center;
        color: #ffffff;
        font-weight: 600;
    }

    /* Text area styling */
    textarea {
        background-color: #ffffff;
        border: 2px solid #74ebd5;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px;
        margin-bottom: 20px;
        font-family: 'Poppins', sans-serif;
    }

    /* Button styling with hover animation */
    .stButton button {
        background-color: #2c3e50;
        color: white;
        border: none;
        padding: 15px 30px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        transition-duration: 0.4s;
    }
    .stButton button:hover {
        background-color: #74ebd5;
        color: black;
    }

    /* Result block styling */
    .result-block {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        text-align: center;
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 12px;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("📱 SMS Spam Detector")

# Subheader
st.subheader("Quickly detect if a message is SPAM or HAM")

# Input text box with placeholder and stylish padding
input_sms = st.text_area("Enter the message", placeholder="Type your message here...")

# Predict button in a centered column layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button('🚀 Predict'):
        if input_sms.strip() != "":
            transformed_sms = transform_text(input_sms)

            # Transform input text using the saved TF-IDF vectorizer
            vector_input = tfidf.transform([transformed_sms])

            # Predict whether SPAM or HAM
            result = model.predict(vector_input)[0]

            # Display result
            if result == 1:
                st.markdown('<div class="result-block"><h2>🚨 This is SPAM!</h2></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="result-block"><h2>✅ This is HAM!</h2></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-block"><h2>⚠️ Please enter a message!</h2></div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)

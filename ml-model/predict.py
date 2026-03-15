from textblob import TextBlob
from googletrans import Translator
import json
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random

translator = Translator()

# Load model
model = load_model("model/chatbot_model.h5")

# Load tokenizer and encoder
tokenizer = pickle.load(open("model/tokenizer.pkl", "rb"))
encoder = pickle.load(open("model/label_encoder.pkl", "rb"))

# Load dataset
data = json.load(open("data/intents.json"))

# Get required input length from model
MAX_LEN = model.input_shape[1]


def analyze_sentiment(text):
    analysis = TextBlob(text)

    if analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "positive"


def translate_to_english(text):
    translated = translator.translate(text, dest="en")
    return translated.text


def get_response(text):

    text = translate_to_english(text)

    sentiment = analyze_sentiment(text)

    if sentiment == "negative":
        return "It seems you might be feeling stressed. You can schedule a counseling session with our student wellness center."

    seq = tokenizer.texts_to_sequences([text])

    padded = pad_sequences(seq, maxlen=MAX_LEN)

    result = model.predict(padded)

    confidence = np.max(result)

    if confidence < 0.2:
        return "I'm not sure about that. Please contact the support office."

    tag = encoder.inverse_transform([np.argmax(result)])

    for intent in data["intents"]:
        if intent["tag"] == tag[0]:
            return random.choice(intent["responses"])

    return "Sorry, I couldn't understand your question."
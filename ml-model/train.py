import json
import numpy as np
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

lemmatizer = WordNetLemmatizer()

with open('data/intents.json') as file:
    data = json.load(file)

patterns = []
tags = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])

tokenizer = Tokenizer()
tokenizer.fit_on_texts(patterns)

sequences = tokenizer.texts_to_sequences(patterns)
padded = pad_sequences(sequences)

encoder = LabelEncoder()
encoded_tags = encoder.fit_transform(tags)

model = Sequential()

model.add(Dense(128, input_shape=(padded.shape[1],), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(set(tags)), activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(padded, encoded_tags, epochs=500)

model.save("model/chatbot_model.h5")

pickle.dump(tokenizer, open("model/tokenizer.pkl","wb"))
pickle.dump(encoder, open("model/label_encoder.pkl","wb"))

print("Model training completed")
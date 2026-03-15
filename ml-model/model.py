from tensorflow.keras.models import load_model
import pickle

print("AI Student Support Model Loaded")

model = load_model("model/chatbot_model.h5")

tokenizer = pickle.load(open("model/tokenizer.pkl","rb"))
encoder = pickle.load(open("model/label_encoder.pkl","rb"))

print("Model Ready")
import tkinter as tk
from tkinter import ttk
from transformers import pipeline

# Use a pre-trained sentiment analysis pipeline
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

# Function to perform sentiment analysis
def analyze_sentiment(text):
    # Perform sentiment analysis using the pipeline
    result = sentiment_analyzer(text)
    sentiment = result[0]['label']
    return sentiment

# GUI Function to handle the sentiment analysis process
def on_analyze_click():
    text = input_text.get("1.0", tk.END).strip()
    if text:
        sentiment = analyze_sentiment(text)
        result_label.config(text=f"Sentiment: {sentiment}", fg="green")
    else:
        result_label.config(text="Please enter text!", fg="red")

# Create the main window
root = tk.Tk()
root.title("Multi-Lingual Sentiment Analysis")
root.geometry("400x400")

# Add title label
title_label = tk.Label(root, text="Multi-Lingual Sentiment Analysis", font=("Helvetica", 14))
title_label.pack(pady=10)

# Text input box for user to enter text
input_text = tk.Text(root, height=5, width=40)
input_text.pack(pady=10)

# Language dropdown (you can extend this list with other languages supported by the model)
lang_var = tk.StringVar(value="en")
lang_label = tk.Label(root, text="Select Language:")
lang_label.pack()
lang_dropdown = ttk.Combobox(root, textvariable=lang_var, values=["en", "es", "fr", "de", "hi"])
lang_dropdown.pack()

# Analyze Button
analyze_button = tk.Button(root, text="Analyze Sentiment", command=on_analyze_click, bg="lightblue")
analyze_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Sentiment will appear here.", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()

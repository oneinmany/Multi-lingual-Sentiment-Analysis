# Multi-lingual-Sentiment-Analysis
Here's a step-by-step procedure for running the provided sentiment analysis with the GUI. The goal is to perform sentiment analysis in multiple languages using the `nlptown/bert-base-multilingual-uncased-sentiment` model. The output will be shown as stars, corresponding to sentiment levels.

### Step 1: Set up the environment
Before you begin, ensure you have the necessary environment and libraries installed.

1. **Install Python**: Make sure Python 3.7+ is installed on your system.
2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # For Windows
   source myenv/bin/activate  # For Mac/Linux
   ```

3. **Install required libraries**:
   You will need the following libraries:
   - `transformers` for the pre-trained model.
   - `tkinter` for the GUI.
   - `torch` as a dependency for the transformers library.

   Run the following commands:
   ```bash
   pip install transformers
   pip install torch
   pip install tkinter
   ```

### Step 2: Running the code

Once the environment is set up and the required libraries are installed, follow these steps:

1. **Open a new Python file** (for example, `sentiment_analysis_gui.py`).
2. **Copy the code into the Python file**.
3. **Run the Python file**:
   - Open a terminal or command prompt.
   - Navigate to the folder where your script is located.
   - Run the script:
     ```bash
     python sentiment_analysis_gui.py
     ```

### Step 3: Using the GUI for sentiment analysis

1. **Launch the GUI**:
   When you run the Python script, a GUI window will open titled **"Multi-Lingual Sentiment Analysis"**.

2. **Enter text**:
   - In the input box, enter the text for which you want to analyze the sentiment. This can be in any of the supported languages (e.g., English, Spanish, French, German, Hindi).
   
3. **Select language**:
   - From the dropdown menu, choose the language of your input text. This is important because the model supports multiple languages, and the correct language must be selected for accurate analysis.

4. **Click "Analyze Sentiment"**:
   - Once you've entered the text and selected the language, click the **"Analyze Sentiment"** button.

5. **View sentiment result**:
   - The sentiment of the entered text will be displayed on the GUI.
   - The sentiment will be classified as one of the following labels, which correspond to star ratings:
     - **"1 star"**: Very negative
     - **"2 stars"**: Negative
     - **"3 stars"**: Neutral
     - **"4 stars"**: Positive
     - **"5 stars"**: Very positive
     
   The result will be displayed in green and will show the sentiment label as text (e.g., `Sentiment: 4 stars`).

6. **Handling no input**:
   - If you click the analyze button without entering any text, the result label will show: `"Please enter text!"` in red.

### Step 4: Output

After entering the text and clicking "Analyze Sentiment," the output will display the sentiment as stars based on the text's sentiment. For example:

- If you enter a positive review like "I love this product!" and choose English, the result will be:
  ```
  Sentiment: 5 stars
  ```
  displayed in green text.

- For a negative sentence like "I hate waiting," the output might show:
  ```
  Sentiment: 1 star
  ```
  also displayed in green.

### Example Execution:

1. **Input**: "This is a great movie!"
   - **Language**: English
   - **Result**: Sentiment: 5 stars

2. **Input**: "I am not happy with this service."
   - **Language**: English
   - **Result**: Sentiment: 2 stars

### Expected Output on GUI:
```
----------------------------------------
| Multi-Lingual Sentiment Analysis     |
----------------------------------------
| Enter text:                          |
| [This is a great movie!]             |
----------------------------------------
| Select Language:                     |
| [English]                            |
----------------------------------------
| Sentiment: 5 stars                   |
----------------------------------------
```

### Troubleshooting:

- **Model error**: If the model is not found, make sure you have internet access, as the pre-trained model is downloaded from Hugging Face.
- **Text not displaying properly**: Ensure that the input text box is properly configured and the program is running without errors.

This is how the GUI-based sentiment analysis tool will work. It will analyze input text and display sentiment as stars based on the `nlptown/bert-base-multilingual-uncased-sentiment` model.

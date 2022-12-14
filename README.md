# Text_emotion_classification

### Here I have build a Text Emotion Classifier using Naive Bayes supervised machine learning algorithm.

## Data source: [Emotion Detection from text](https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text)

## Steps
<br> 1. Data Cleaning - Dropped unnessesary columns 
<br> 2. EDA - Created new columns like no. of characters, words, sentences in a data point, visualization of their count. Interesting word clouds of each classes.
<br> 3. Text preprocessing - lower casing, word tokenization, removal of special characters and punctuation and stemming
<br> 4. Model building - used countvectorizer and tfidvectorizer to vectorize the words and GaussianNB, MultinomialNB and BernoulliNB from Scikit learn for model building.
<br> 5. Evaluation - countvectorizer with MultinomialNB performed well.
<br> 6. Website deployment - Used Streamlit for deployement.


Click here to use this app: [Text Emotion Classifier](https://arpsgit-text-emotion-classification-main-9muey4.streamlit.app/)
# Text_emotion_classification

:smile: :pensive: :rage: :heart_eyes: :expressionless:

### Here I have build a Text Emotion Classifier using Naive Bayes supervised machine learning algorithm.

### Data source: [Emotion Detection from text](https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text) :floppy_disk:

## Steps
<br> 1. Data Cleaning - Dropped unnessesary columns :scissors: <br>
<br> 2. EDA - Created new columns like no. of characters, words, sentences in a data point, visualization of their count. Interesting word clouds of each classes. :bar_chart: <br>
<br> 3. Text preprocessing - lower casing, word tokenization, removal of special characters and punctuation and stemming. :pencil: <br>
<br> 4. Model building - used countvectorizer and tfidvectorizer to vectorize the words and GaussianNB, MultinomialNB and BernoulliNB from Scikit learn for model building. :wrench: <br>
<br> 5. Evaluation - countvectorizer with MultinomialNB performed well. :chart_with_upwards_trend: <br>

### To see those above mentioned steps : [Notebook](https://github.com/Arpsgit/Text_emotion_classification/blob/main/text_emotion_classification.ipynb) :notebook: 

<br> 6. Website deployment - Used Streamlit for deployement. :pushpin:

### To see the process of making the streamlit app : [App](https://github.com/Arpsgit/Text_emotion_classification/blob/main/main.py)


## Click here to use this app: [Text Emotion Classifier](https://arpsgit-text-emotion-classification-main-9muey4.streamlit.app/) :innocent:
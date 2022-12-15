import streamlit as st
import pickle
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
stemmer = PorterStemmer()


def text_preprocessing(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    alfa_num = []
    for token in text:
        if token.isalnum():
            alfa_num.append(token)

    text = alfa_num[:]
    alfa_num.clear()

    for token in text:
        if token not in stopwords.words('english'):
            alfa_num.append(token)

    text = alfa_num[:]
    alfa_num.clear()

    for token in text:
        alfa_num.append(stemmer.stem(token))

    text = alfa_num[:]
    alfa_num.clear()
    return " ".join(text)


vec = pickle.load(open('count_vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Text Emotion Classifier V1.0!!!")
input_text = st.text_area("Enter your text: ")

if st.button('Predict'):
    if input_text != '':
        # preprocess
        transformedtext = text_preprocessing(input_text)

        # vectorize
        vector_input = vec.transform([transformedtext])

        # predict
        result = model.predict(vector_input)[0]

        # display

        if result == 0:
            st.header('Angry / Hate / Bore')
        elif result == 1:
            st.header('Happy / Relief / Surprise')
        elif result == 2:
            st.header('Love / Fun / Enthusiasm')
        elif result == 3:
            st.header('Neutral')
        else:
            st.header('Sad')
    else:
        st.subheader('Please enter a text!')

st.subheader("Made by Arpan Manna.")
st.caption("Website: https://sites.google.com/view/arpanmanna")

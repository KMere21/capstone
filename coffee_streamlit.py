### borrowed code from BrainStation streamlit kick off 

### import libraries
import pandas as pd
import streamlit as st
import numpy as np
import joblib
from matplotlib import pyplot as plt

#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file


#######################################################################################################################################
### Create a title

# Press R in the app to refresh after changing the code and saving here

### You can also use markdown syntax.
#st.write('# Our last morning kick off :sob:')

### To position text and color, you can use html syntax
#st.markdown("<h1 style='text-align: center; color: blue;'>Our last morning kick off</h1>", unsafe_allow_html=True)

# https://www.coffeereview.com/review/colombia-la-esperanza-100-geisha-hanashaku/


#######################################################################################################################################
##### Model Demo 1##########
image0 = ('CoffeeReview.png')
st.image(image0)

st.title("Predicting Coffee Ratings with Review Data")

st.subheader("Let's test some  new reviews!")
# Load the model using joblib
model = joblib.load('/Users/katemondal/Documents/BrainStation/CapstoneProject/rating_pipeline.pkl')

# Set up input field
review = st.text_input('', '')

# Use the model to predict sentiment & write result
prediction = model.predict({review})

if review != '':
    st.subheader('The predicted score is:') 
    st.header(np.round_(prediction).astype(int))
else: 
    st.write('Enter text above to get predicted score.')

# Link to review page 1
st.write('[Review One](https://www.coffeereview.com/review/tinamit-toliman/)')
image1 = ('Review_1.png')
st.image(image1)

# Link to review page 2
st.write('[Review Two](https://www.coffeereview.com/review/colombia-castillo-fruit-maceration-series-peach/)')
image2 = ('Review_2.png')
st.image(image2)

# Link to review page 3
st.write('[Review Three](https://www.coffeereview.com/review/sumatra/)')
image3 = ('Review_3.png')
st.image(image3)


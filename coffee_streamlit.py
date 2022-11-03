### borrowed code from BrainStation streamlit kick off 

### import libraries
import pandas as pd
import streamlit as st
import joblib

#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file


#######################################################################################################################################
### Create a title

st.title("Predicting Coffee Ratings with Review Data")

# Press R in the app to refresh after changing the code and saving here

### You can also use markdown syntax.
#st.write('# Our last morning kick off :sob:')

### To position text and color, you can use html syntax
#st.markdown("<h1 style='text-align: center; color: blue;'>Our last morning kick off</h1>", unsafe_allow_html=True)


#######################################################################################################################################
### DATA LOADING

### A. define function to load data
@st.cache # <- add decorators after tried running the load multiple times
def load_data(path, num_rows):

    df = pd.read_csv(path, nrows=num_rows)

    return df

### B. Load the data
coffee = load_data("tfidf_Xremain_combo_df.csv", 4194)

### C. Display the dataframe in the app
st.dataframe(coffee)


#######################################################################################################################################
### STATION MAP

st.subheader('Coffee Origin Locations')      

#st.map(coffee)     


#######################################################################################################################################
### DATA ANALYSIS & VISUALIZATION

### B. Add filter on side bar after initial bar chart constructed

#st.sidebar.subheader("Usage filters")
#round_trip = st.sidebar.checkbox('Round trips only')

#if round_trip:
    #df = df[df['Start Station ID'] == df['End Station ID']]


### A. Add a bar chart of usage per hour

#st.subheader("Daily usage per hour")

#counts = df["Start Time"].dt.hour.value_counts()
#st.bar_chart(counts)

### The features we have used here are very basic. Most Python libraries can be imported as in Jupyter Notebook so the possibilities are vast.
#### Visualizations can be rendered using matplotlib, seaborn, plotly etc.
#### Models can be imported using *.pkl files (or similar) so predictions, classifications etc can be done within the app using previously optimized models
#### Automating processes and handling real-time data


#######################################################################################################################################
### MODEL INFERENCE

st.subheader("Using pretrained models with user input")

# A. Load the model using joblib
model = joblib.load('/Users/katemondal/Documents/BrainStation/CapstoneProject/rating_pipeline.pkl')

# B. Set up input field
text = st.text_input('Enter your review text below', 'Amazing coffee.')

# C. Use the model to predict sentiment & write result
prediction = model.predict({text})

st.write(prediction)

###### can keep or do something like this if predictions way off...
if prediction > 94:
    st.write('We predict that this is an exceptional coffee!')
elif prediction > 90:
    st.write('We predict that this is a very good coffee.')

else:
    st.write('We predict that this is a negative review!')



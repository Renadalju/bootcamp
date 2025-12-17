import pandas as pd 
import streamlit as st

#1 set up 
data = {
    "Name": ["Alice","Bob","charlie","Diana"],
    "Age": [25 ,30,35,28],
    "City": [" New York", "London", "Paris", "Tokyo"],
    "Active": [True, False, True, True]
}

df = pd.DataFrame(data)
st.title("Streamlit Table Demo")

# Method 1: interactive data frame
st.subheader("1. interactive data frame ")
st.write("this version allows users to sort columns and resize the table.")
st.dataframe(df) 

#method 2: static table 
st.subheader("2.static table")
st.write("this is a traditional, non-interactive table")
st.table(df)
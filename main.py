import streamlit as st
import pandas as pd

# Sample DataFrame to display in the first tab
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 27, 22], 'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Create a tabbed interface
tab1, tab2 = st.tabs(["DataFrame", "Other Info"])

# Add content to the first tab
with tab1:
    st.write("DataFrame Content:")
    st.dataframe(df)  # Displays the DataFrame in an interactive table format

# Add content to the second tab
with tab2:
    st.write("This is the second tab.")
    st.write("You can add more information or interactive widgets here.")

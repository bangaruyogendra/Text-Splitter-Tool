import streamlit as st
import pandas as pd
import time
st.title("Text Splitter Tool")
store_data = pd.DataFrame(columns = ("Given String","Operations/Methods","Output"))
def conversion(str,operation):
    if operation == "Upper Case":
        return str.upper()
    elif operation == "Lower Case":
        return str.lower()
    elif operation == "Title Case":
        return str.title()
    elif operation == "Split":
       return str.split(" ")
    elif operation == "find":
       ch = st.text_input("Enter the character to find index of that:")
       return str.find(ch)
    elif operation == "Count Vowels":
       with st.spinner("wait for results..."):
          time.sleep(3)
       str = str.lower()
       vowels = ["a","e","i","o","u"]
       cnt=0
       for ch in str:
          if ch in vowels:
             cnt+=1
       return cnt
    elif operation == "Count Consonates":
       with st.spinner("wait for results..."):
          time.sleep(3)
       str = str.lower()
       vowels = ["a","e","i","o","u"]
       cnt=0
       for ch in str:
          if ch not in vowels:
             cnt+=1
       return cnt
    elif operation == "Count Characters":
       with st.spinner("wait for results..."):
          time.sleep(3)
       str = str.lower()
       cnt=0
       for ch in str:
             cnt+=1
       return cnt
    
    else:
        return str[::-1]

str = st.text_input("Please enter the String to perform Operations :",key ="input_text")

operation = st.selectbox("Select option to perform method on Given String :",("None","Upper Case","Lower Case","Title Case","Reverse","Split","find","Count Vowels","Count Consonates","Count Characters"))
def res():
   str = st.session_state.input_text
   output = conversion(str,operation)
   new_row = {
    "Given String":str,
    "Operations/Methods":operation,
    "Output":output,
    }
   if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns = store_data.columns)
   st.session_state.data = pd.concat([st.session_state.data,pd.DataFrame([new_row])],ignore_index = True)
   st.dataframe(st.session_state.data)
   
if st.button("Convert"):
   res()



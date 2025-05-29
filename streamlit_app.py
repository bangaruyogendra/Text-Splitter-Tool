import streamlit as st
import pandas as pd
st.title("Text Splitter Tool")
store_data = pd.DataFrame(columns = ("Given String","Operations/Methods","Output"))
def conversion(str,operation):
    if operation == "Upper Case":
        return str.upper()
    elif operation == "Lower Case":
        return str.lower()
    elif operation == "Title Case":
        return str.captialize()
    elif operation == "Reverse":
        return str[::-1]
    else:
        return str

str = st.text_input("Given String:")

operation = st.selectbox("Select option to perform method on Given String",("Upper Case","Lower Case","Title Case","Reverse"))

output = conversion(str,operation)
new_row = {
    "Given String":str,
    "Operations/Methods":operation,
    "Output":output,
}
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns = store_data.columns)
 st.session_state.data = pd.concat([st.session_state.data,pd.DataFrame([new_row])],ignore_index = True)



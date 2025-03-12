import streamlit as st
import string_utils
st.title("Unscramble")
words = ["tree", "ocean"]
for word in words:
    scrambled = string_utils.shuffle(word)
    if st.text_input(scrambled) == "tree":
        st.text("Great job!!!")
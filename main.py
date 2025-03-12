import streamlit as st
import string_utils
st.title("Unscramble")
words = ["tree", "ocean"]
def scramble(in):
    return string_utils.shuffle(in)
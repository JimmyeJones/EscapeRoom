import streamlit as st
import string_utils
st.title("Unscramble")
scrambled = ["tere", "eonac", "otab"]
words = ["tree", "ocean", "boat"]
st.session_state["solved"] = []
try:
    ans
except NameError:
    ans = []
def scramble(a):
    return string_utils.shuffle(a)
for scrambled1 in scrambled:
    if st.text_input(scrambled1) == words[scrambled.index(scrambled1)]:
        if scrambled.index(scrambled1) not in st.session_state["solved"]:
            st.session_state["solved"].append(scrambled.index(scrambled1))


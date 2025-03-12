import streamlit as st
import string_utils
st.title("Unscramble")
scrambled = ["tere", "eonac", "otab"]
words = ["tree", "ocean", "boat"]
st.session_state["solved"] = []
def scramble(a):
    return string_utils.shuffle(a)
def is_in_ss(index, list):
    included = False
    for all in list:
        if index in all:
            return True
    if not included:         
        return False
        
for scrambled1 in scrambled:
    if is_in_ss(scrambled.index(scrambled1), st.session_state["solved"]):
        if st.text_input(scrambled1) == words[scrambled.index(scrambled1)]:
            if scrambled.index(scrambled1) not in st.session_state["solved"]:
                st.session_state["solved"].append(scrambled.index(scrambled1))
    else:
        st.subheader(words[scrambled.index(scrambled1)])
st.write(st.session_state["solved"])

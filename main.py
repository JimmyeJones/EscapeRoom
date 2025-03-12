import streamlit as st
import string_utils
st.title("Unscramble")
words = ["tree", "ocean", "boat"]
st.session_state["solved"] = []
st.session_state["scrambled"] = []
def scramble(a):
    return string_utils.shuffle(a)
if len(st.session_state["scrambled"]) == 0:
    for word in words:
        st.session_state["scrambled"].append(scramble(word))
scrambled = st.session_state["scrambled"]
        
for scrambled1 in scrambled:
    
    if st.text_input(scrambled1) == words[scrambled.index(scrambled1)]:
        if scrambled.index(scrambled1) not in st.session_state["solved"]:
            st.session_state["solved"].append(scrambled.index(scrambled1))

st.write(st.session_state["solved"])

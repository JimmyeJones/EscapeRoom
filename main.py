import streamlit as st
import string_utils
st.title("Welcome to the Sinclair Escape Room - 3rd Period!")
st.subheader("Unscramble the following words:")
st.write("*Note: type your answer in all lowercase letters*")
st.write("*Dashes are NOT in set positions*")
words = st.secrets["words"]
st.session_state["solved"] = []
try:
    len(st.session_state["scrambled"])
except KeyError:
    st.session_state["scrambled"] = []
def scramble(a):
    scramble_word = string_utils.shuffle(a)
    while scramble_word == a:
        scramble_word = string_utils.shuffle(a)
    return scramble_word
        
if len(st.session_state["scrambled"]) == 0:
    for word in words:
        st.session_state["scrambled"].append(scramble(word))
scrambled = st.session_state["scrambled"]
        
for scrambled1 in scrambled:
    
    if st.text_input(scrambled1) == words[scrambled.index(scrambled1)]:
        if scrambled.index(scrambled1) not in st.session_state["solved"]:
            st.session_state["solved"].append(scrambled.index(scrambled1))
            st.success("Correct!")

if len(st.session_state["solved"]) == len(scrambled):
    st.balloons()
    st.info(f"Congratulations! The final code is: '{st.secrets["final_code"]}'")

import streamlit as st
import string_utils
st.title("Unscramble")
words = ["tree", "ocean"]
def scramble(in):
    return string_utils.shuffle(in)
try:
    scrambled
except NameError:
    scrambled = []
    for word in words:
        scrambled.append(scramble(word))
        
for scrambled_word in scrambled:
    solved = st.text_input(scrambled_word)
    solved_words.append(solved)
for solved_word in solved_words:
    if solved_word == words[solved_words.len(solved_word)]:
        st.text("Nice Job!!!!")
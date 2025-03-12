import streamlit as st
import string_utils
st.title("Unscramble")
words = ["tree", "ocean"]
word_num = 0
word_input = []
for word in words:
    word_num += 1
    scrambled = string_utils.shuffle(word)
    word_input[word_num] = st.text_input(scrambled)
for word_i in word_input:
    if word_i == words[word_input.len(word_i)]:
        st.text("Great job!!!")
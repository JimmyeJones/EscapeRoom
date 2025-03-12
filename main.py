import streamlit as st
import string_utils
st.title("Unscramble")
words = ["tree", "ocean", "boat"]
try: 
    solved
except NameError:
    solved = []
    for x in words:
        solved.append(False)
    
def scramble(in):
    return string_utils.shuffle(in)


scrambled = []
for word in words:
    scrambled.append(scramble(word))
        
for scrambled_word in scrambled:
    solved1 = st.text_input(scrambled_word)
    solved_words.append(solved1)
for solved_word in solved_words:
    if solved_word == words[solved_words.len(solved_word)]:
        st.text("Nice Job!!!!")
        solved[solved_words.len(solved_word)] = True
import streamlit as st
import string_utils
st.title("Unscramble")
scrambled = ["tere", "eonac", "otab"]
words = ["tree", "ocean", "boat"]
def scramble(a):
    return string_utils.shuffle(a)
for scrambled1 in scrambled:
    ans[scrambled.len(scrambled1)] = st.text_input(scrambled1)

st.write(ans)

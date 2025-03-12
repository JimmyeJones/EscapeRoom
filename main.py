import streamlit as st
import string_utils
st.title("Unscramble")
scrambled = ["tere", "eonac", "otab"]
words = ["tree", "ocean", "boat"]
st.session_state["solved"]{0} = []
def scramble(a):
    return string_utils.shuffle(a)
for scrambled1 in scrambled:
    if scrambled.index(scrambled1) not in st.session_state["solved"]{0}:
        if st.text_input(scrambled1) == words[scrambled.index(scrambled1)]:
            if scrambled.index(scrambled1) not in st.session_state["solved"]{0}:
                st.session_state["solved"]{0}.append(scrambled.index(scrambled1))
    else:
        st.subheader(words[scrambled.index(scrambled1)])
st.write(st.session_state["solved"]{0})

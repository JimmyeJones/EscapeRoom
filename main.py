import streamlit as st
import string_utils
import uuid
st.title("Welcome to the Sinclair Escape Room - 3rd Period!")
st.subheader("Unscramble the following words:")
st.write("*Note: type your answer in all lowercase letters*")
st.write("*Dashes are NOT in set positions*")
words = st.secrets["words"]
sentences = st.secrets["sentences"]
final_code = st.secrets["final_code"]
st.session_state["solved"] = []
try:
    len(st.session_state["sent_ans"])
except KeyError:
    st.session_state["sent_ans"] = []
    for x in sentences:
        st.session_state["sent_ans"].append([])
        for g in x.split():
            if g not in words:
                st.session_state["sent_ans"][sentences.index(x)].append(g)
        
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

#if len(st.session_state["solved"]) == len(scrambled):
if True:
    st.info(f"Congratulations! You must now make a sentence using all the words.")
    st.subheader("Complete the sentence:")
    st.write("Note: Words may be used more than once")
    st.divider()
    st.write(st.session_state["sent_ans"])
    for sentence in sentences:
        for word_in_sent in sentence.split():
            
            if word_in_sent in words:
                st.secrets["sent_ans"][sentences.index(sentence)][words.index(word_in_sent)] == st.selectbox("", words, key=uuid.uuid4().int):
                    
            else:
                st.write(word_in_sent)
        st.divider()

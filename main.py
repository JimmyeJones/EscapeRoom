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
try:
    len(st.session_state["solved1"])
except KeyError:
    st.session_state["solved1"] = []
try:
    len(st.session_state["solved"])
except KeyError:
    st.session_state["solved"] = []
    for sentence in sentences:
        st.session_state["solved"].append("")

try:
    len(st.session_state["sent_ans"])
except KeyError:
    st.session_state["sent_ans"] = []
    for x in sentences:
        st.session_state["sent_ans"].append([])
        for g in x.split():
            if g not in words:
                st.session_state["sent_ans"][sentences.index(x)].append(g)
            else:
                st.session_state["sent_ans"][sentences.index(x)].append("")
        
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
    
    if st.text_input(scrambled1.lower()) == words[scrambled.index(scrambled1)].lower():
        if scrambled.index(scrambled1) not in st.session_state["solved1"]:
            st.session_state["solved1"].append(scrambled.index(scrambled1))
        st.success("Correct!")

if len(st.session_state["solved1"]) == len(scrambled):
#if True:   for testing
    st.info(f"Congratulations! You must now make a sentence using all the words.")
    st.subheader("Complete the sentences:")
    st.write("Note: Words may be used more than once")
    st.divider()
    for sentence in sentences:
        for word_in_sent in sentence.split():
            
            if word_in_sent in words:
                st.session_state["sent_ans"][sentences.index(sentence)][sentence.split().index(word_in_sent)] = st.selectbox("", words, key=f"{sentences.index(sentence)}{sentence.index(word_in_sent)}")                 
            else:
                st.write(word_in_sent)
        st.divider()
    for sentence1 in st.session_state["sent_ans"]:
        if " ".join(sentence1).lower() == sentences[st.session_state["sent_ans"].index(sentence1)].lower():
            st.session_state["solved"][st.session_state["sent_ans"].index(sentence1)] = True
        else:
            st.session_state["solved"][st.session_state["sent_ans"].index(sentence1)] = False
        #st.write(sentences[st.session_state["sent_ans"].index(sentence1)].lower())
error_codes = []
show_code = ""
for check in st.session_state["solved"]:
    if check == False:
        show_code = False
        error_codes.append(st.session_state["solved"].index(check))
    if show_code != False and check == True:
        show_code = True
error_codes1 = []
for error_code in error_codes:
    code1 = error_code*5
    error_codes1.append(code1)
if show_code == True:
    st.subheader(st.secrets["final_code"])
elif show_code == False:
    st.error(f"Whoops! You have selected (an) incorrect answer(s). Error Code(s): {", ".join(error_codes1)}")


import streamlit as st
import string_utils
import uuid
st.title("Welcome to the Sinclair Escape Room - 3rd Period!")
st.write("Your answers will NOT be saved after this page has been reloaded.")
st.subheader("Scenario")
st.write("You are trapped inside of General Zaroff’s trophy room and have to escape. There are notes in the room with scrambled up words on them. They aeration to the word lock on the door. In order to escape before general Zaroff gets suspicious, solve the problems below to break out!")
words = st.secrets["words"]
sentences = st.secrets["sentences"]
final_code = st.secrets["final_code"]
st.subheader("First, complete the wordle.")
st.link_button("Open Wordle", "https://mywordle.strivemath.com/?word=uotke")
if st.secrets["wordle"] in st.text_input("""Enter the "Copy This Attempt" from the Wordle"""):
    st.success("Great Job!")
    st.subheader("Unscramble the following words:")
    st.write("*Note: type your answer in all lowercase letters*")
    
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
            if show_code != False and check == True:
                show_code = True
        for index, value in enumerate(st.session_state["solved"]):
            if value == False:
                error_codes.append(index)
    
        error_codes1 = []
        for error_code in error_codes:
            code1 = ((int(error_code)*2)+4)**3-(int(error_code)*3)
            error_codes1.append(code1)
        if show_code == True:
            st.title("The final code is:")
            st.subheader(st.secrets["final_code"])
        elif show_code == False:
            if len(error_codes1) == 1:
                st.error(f"Whoops! You have selected an incorrect answer. Error Code: {str(error_codes1)}")
            else:
                st.error(f"Whoops! You have selected incorrect answers. Error Codes: {str(error_codes1)}")
            st.text("*Hint: This site's code is stored on Github.*\n *Hint x2: There may be a link somewhere... 🤔*")

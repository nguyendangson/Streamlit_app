import streamlit as st
from streamlit_chat import message

# pip install chatbotAI
#from chatbot import demo
#from chatbot import Chat, register_call
#demo()

from datetime import datetime
from st_pages import Page, Section, add_page_title, show_pages ,show_pages_from_config
add_page_title()

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/white-gray-geometric-pattern-background-vector_53876-136510.jpg?w=1060&t=st=1681246927~exp=1681247527~hmac=175d0a73d7a955330a694cda7e115db8bae29571a0caa75cae2b4f35da35a9dc");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

"My email address is sdnguyen1@crimson.ua.edu"
me="sdnguyen1@crimson.ua.edu"

"For networking and collaboration, please contact me on [LinkedIn](https://www.linkedin.com/in/son-nguyen-023885124/) or [Researchgate](https://www.researchgate.net/profile/Son-Nguyen-8)."

# https://formsubmit.co/       temperary email address
# my email linke to formsubmit: https://formsubmit.co/el/nukada
contact_form = """
<div class="container">
  <h1>Send an email directly to me</h1>
  <form target="_blank" 
action="https://formsubmit.co/sdnguyen1@crimson.ua.edu" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <div class="form-group">
      <div class="form-row">
        <div class="col">
          <input type="Message" name="name" class="form-control" 
placeholder="Your Full Name" required>
        </div>
        <div class="col">
          <input type="email" name="From email address" class="form-control" 
placeholder="Your email Address" required>
        </div>
      </div>
    </div>
    <div class="form-group">
      <textarea rows="10" cols="100" placeholder="Your Message" class="form-control" 
name="message" rows="10" required></textarea>
    </div>
    <button type="submit" class="btn btn-lg btn-dark btn-block">Submit Form</button>
  </form>
</div>
"""

st.markdown(contact_form , unsafe_allow_html=True)


#st.title("Leave your messages directly to me. My assistant is Blenderbot Chatbot of Facebook")
st.title("Leave your messages directly to me")

from transformers import BlenderbotTokenizer
from transformers import BlenderbotForConditionalGeneration
def get_models():
    # it may be necessary for other frameworks to cache the model
    # seems pytorch keeps an internal state of the conversation
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

if "history" not in st.session_state:
    st.session_state.history = []
if "date_time" not in st.session_state:
    st.session_state.date_time = []
if "your_message" not in st.session_state:
    st.session_state.your_message=""


def generate_answer():
    tokenizer, model = get_models()
    user_message = st.session_state.input_text
    inputs = tokenizer(st.session_state.input_text, return_tensors="pt")
    result = model.generate(**inputs)
    message_bot = tokenizer.decode(
        result[0], skip_special_tokens=True
    )  # .replace("<s>", "").replace("</s>", "")

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})
    st.session_state.date_time.append(datetime.now())

def record_chat():
    st.session_state.history.append({"message": st.session_state.input_text_record, "is_user": True})
    st.session_state.date_time.append(datetime.now())
    st.session_state.your_message=st.session_state.your_message + " " + st.session_state.input_text_record
    st.session_state.input_text_record = ''  # Clear input after done
#st.session_state.message_history=[{"message": "Hello, please let your message here if you want to contact to Son Nguyen. Thank you","is_user":False},{"message":"Hello bot","is_user":True},{"message": "Good morning","is_user":False},{"message": "Good morning you","is_user":True}]
st.text_input("Chat to me", key="input_text_record", on_change=record_chat)
#st.text_input("Chat to me", key="input_text_record", on_change=record_chat)    # key are variables
#st.session_state.input = st.text_input("you:")
#st.session_state.message_history.append({"message":st.session_state.input ,"is_user":True})

#if st.button("Delete all previous messages",key="delete_message"):
#   st.session_state.history=[]
#   st.session_state.date_time = []

for i,chat in enumerate(st.session_state.history):
    message(**chat)
    st.write(st.session_state.date_time[int(i//2)])
    
#st.write("Record=",st.session_state.your_message)

your_full_name = st.text_input("Your Full Name")
your_email_address= st.text_input("Your Email Address")
submit_your_chat=st.button("Submit your chat")
if your_full_name and your_email_address and submit_your_chat:
    contact_form_message = f"""
    <form action="https://formsubmit.co/sdnguyen1@crimson.ua.edu" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type= "hidden" name="Full Name" value="{your_full_name}">  
        <input type= "hidden" name="Message" value="{st.session_state.your_message}"> 
        <input type="hidden" name="From email address" value="{your_email_address}">
        <button type="submit">Send</button>
    </form>"""        # add variables into string https://matthew-brett.github.io/teaching/string_formatting.html
    #st.markdown(f"<style>{contact_form_message}</style>", unsafe_allow_html=True)
    st.markdown(contact_form_message, unsafe_allow_html=True)


#st.title("Audio record message")

#from audio_recorder_streamlit import audio_recorder

#audio_bytes = audio_recorder(
#    text="",
#    recording_color="#e8b62c",
#   neutral_color="#6aa36f",
#    icon_name="user",
#    icon_size="6x",
#) 
#if audio_bytes:
#    st.audio(audio_bytes, format="audio/wav")
# The recording will stop automatically
# 2 sec after the utterance end
#audio_bytes = audio_recorder(pause_threshold=2.0, sample_rate=41_000)


st.markdown(f"""<a href="https://info.flagcounter.com/xaga"><img src="https://s01.flagcounter.com/count2/xaga/bg_FFFFFF/txt_000000/border_CCCCCC/columns_3/maxflags_20/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>""", unsafe_allow_html=True)






    

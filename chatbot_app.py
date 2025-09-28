import streamlit as st

st.set_page_config(page_title="Custom Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 My Custom Chatbot")
st.write("Welcome! Type your message below to chat.")

class ConversationManager:
    def __init__(self, bot_name="ChatBot"):
        self.bot_name = bot_name
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def add_message(self, sender, text):
        st.session_state.messages.append({"sender": sender, "text": text})

    def get_messages(self):
        return st.session_state.messages

    def bot_response(self, user_input):
        # Basic demo responses (replace with AI model later)
        if "hello" in user_input.lower():
            return f"Hi there! I'm {self.bot_name}. How can I help you today?"
        elif "bye" in user_input.lower():
            return "Goodbye! Have a great day 😊"
        else:
            return "I’m still learning. Can you try rephrasing?"

manager = ConversationManager()

# Display chat history
for msg in manager.get_messages():
    if msg["sender"] == "user":
        st.markdown(f"**🧑 You:** {msg['text']}")
    else:
        st.markdown(f"**🤖 {manager.bot_name}:** {msg['text']}")

# Input box
user_input = st.text_input("Type your message:")

with st.sidebar:
    st.header("⚙️ Settings")
    bot_name = st.text_input("Bot Name", value="ChatBot")
    st.session_state["bot_name"] = bot_name

manager.bot_name = st.session_state["bot_name"]


if user_input:
    manager.add_message("user", user_input)
    response = manager.bot_response(user_input)
    manager.add_message("bot", response)
    st.experimental_rerun()



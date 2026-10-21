import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq

# 1. Load environment variables from the .env file
load_dotenv()

# 2. Configure the Streamlit page layout and header settings
st.set_page_config(page_title="AI Assistant", page_icon="🤖", layout="centered")
st.title("🤖 AI Assistant")

# 3. Initialize the LangChain ChatGroq model instance
model = ChatGroq(model="openai/gpt-oss-20b")

# 4. Initialize session state to maintain conversational memory across page rerenders
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content='You are a helpful AI Assistant!')
    ]

# 5. Iteratively render the existing conversation log onto the chat interface
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# 6. Capture dynamic user entries via the interactive chat input field
if user_input := st.chat_input("Type your message here..."):
    
    # Render user prompt in the chat box immediately
    with st.chat_message("user"):
        st.write(user_input)
    
    # Append the recent human token into session conversation logs
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    
    # Display processing state while the backend fetches model inferences
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            # Invoke the underlying LLM with cumulative state references
            result = model.invoke(st.session_state.chat_history)
            st.write(result.content)
            
    # Commit the calculated model response back into persistent conversation loops
    st.session_state.chat_history.append(AIMessage(content=result.content))





# There are three types of messages in langchain
# System message
# Human message
# AI messages
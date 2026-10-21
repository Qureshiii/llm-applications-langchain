import streamlit as st
from dotenv import load_dotenv
# Yahan load_prompt import kiya
from langchain_core.prompts import load_prompt 
from langchain_google_genai import ChatGoogleGenerativeAI 

# Environment variables load karein
load_dotenv()

# Gemini 3.8 Flash model initialize kiya
model = ChatGoogleGenerativeAI(model="gemini-3.8-flash") 

st.header('Research Tool')

# Inputs
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need",
"BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

# FIX: Yahan variable ka naam badal kar 'style_input' kar diya hai
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical",
"Code-Oriented", "Mathematical"] )

length_input = st.selectbox('Select Length', ["Short", "Medium", "Long"])

# --- YAHAN CHANGE KIYA HAI: JSON se template load ho raha hai ---
template = load_prompt('template.json')

# --------------------------------------------------------------

if st.button('Summarize'):
    with st.spinner('Analyzing documents and generating insights. Please wait...'):
        chain = template | model

        result = chain.invoke({
            'paper_input':paper_input,
            'style_input':style_input, # FIX: Ab ye match ho gaya hai
            'length_input':length_input
        })
                    # Output screen par print hoga
        st.success("Summary Generated Successfully!")
        st.subheader("Output:")
                
                # --- YAHAN CHANGE KIYA HAI: Format fixing logic ---
        output_data = result.content
                
                # Agar output dictionary ya JSON format me ho to text extract karein
        if isinstance(output_data, dict) and "text" in output_data:
            clean_text = output_data["text"]
        elif isinstance(output_data, list) and len(output_data) > 0 and isinstance(output_data[0], dict) and "text" in output_data[0]:
            clean_text = output_data[0]["text"]
        else:
                    # Agar string hai to as-is use karein
            clean_text = str(output_data)
                    
                # \n escape characters ko real line breaks me badlein
            clean_text = clean_text.replace(r'\n', '\n')
                
                # st.markdown se headings aur bold text sahi render honge
            st.markdown(clean_text)







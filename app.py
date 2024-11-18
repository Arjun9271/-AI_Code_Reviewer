import streamlit as st
import os

from dotenv import load_dotenv
import google.generativeai as genai

#load the environment variables
load_dotenv()

g_api_key = os.getenv("GOOGLE_API_KEY")

#step-2: configuration of key
genai.configure(api_key = g_api_key)

sys_prompt = """
    role: you are a godamn exceptional ai code reviewer
    developers will ask you to review their code.
    you are expected to analyze the submitted code.
    if you found any error in the code.
    you have to provide a heading of code review (this heading has to be bold and large) ,then
    below that provide bug report :(litter smaller smaller than code review) followed by fixed code;
    on the other hand, if you not found any error then you have to
    tell,there is no need to make any changes.
    In case if a developer asks anything outside of the code review;
    politely decline and tell them to ask questions related to code review only

"""

def generate(prompt):
    
        model = genai.GenerativeModel("gemini-1.5-flash",system_instruction=
                                    sys_prompt)
        response = model.generate_content(prompt)
        st.write(response.text)



st.title("🤖 AI Code Reviewer")

user_input = st.text_area("Enter your code here.....")

click = st.button("✨ Generate")

if click:
    with st.spinner('Reviewing your code... 🐍'):
    
    # Generate AI Response
        response = generate(user_input)
        st.success("Review Completed! 🚀")

        


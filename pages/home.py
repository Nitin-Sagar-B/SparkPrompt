import os
import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Home function for the Streamlit app
def home():
    st.title("SparkPrompt 🧙‍♂️")
    st.subheader("Prompt Writing Simulator to improve core prompt engineering skills🕹️")

    # Step 0: User input for Google API key
    api_key = st.text_input("Enter your Google API Key", type="password")
    
    if api_key:
        # Set the Google API key as an environment variable
        os.environ['GOOGLE_API_KEY'] = api_key
        
        # Initialize the Google Generative AI model
        model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

        # Initialize session state variables
        if 'problem_statement' not in st.session_state:
            st.session_state.problem_statement = ""
        if 'evaluation' not in st.session_state:
            st.session_state.evaluation = ""
        if 'best_prompt' not in st.session_state:
            st.session_state.best_prompt = ""

        # Step 1: User inputs
        st.subheader("Select Domain and Input Skills:")
        domain = st.selectbox("Select Domain", ["AI", "Data Science", "Web Development", "Machine Learning", "Sales & Marketing", "VLSI"])
        skills = st.text_input("Enter your skills (comma-separated)")

        if st.button("Generate Problem Statement"):
            st.session_state.problem_statement = generate_problem_statement(domain, skills)
        
        if st.session_state.problem_statement:
            st.write(st.session_state.problem_statement)

            # Step 2: User writes a prompt
            st.subheader("Write Your Prompt:")
            user_prompt = st.text_area("Enter your prompt here")

            if st.button("Evaluate Prompt"):
                st.session_state.evaluation = evaluate_prompt(user_prompt, st.session_state.problem_statement)
                st.session_state.best_prompt = generate_best_prompt(st.session_state.problem_statement)
            
            if st.session_state.evaluation:
                st.markdown("---")
                st.write(st.session_state.evaluation)
                st.markdown("---")
                st.write(st.session_state.best_prompt)
                st.markdown("---")

# Other functions for generating problem statements, evaluating prompts, and generating the best prompt
def generate_problem_statement(domain, skills):
    prompt_template = "Generate a problem statement which the user should write a prompt to, in the {domain} domain that requires the following skills: {skills}. The problem statement should be concise, and simple. Keep the problem statement relevant to making the user write a prompt."
    prompt = prompt_template.format(domain=domain, skills=skills)
    message = HumanMessage(content=prompt)
    response = model.stream([message])
    return ''.join([r.content for r in response])

def evaluate_prompt(user_prompt, problem_statement):
    evaluation_prompt = (
        f"Evaluate the following prompt based on its relevance, clarity, and completeness for the problem statement: {problem_statement} and give an overall score out of 10 to the user prompt.\n\n"
        "Keep the evaluation well structured and concise.\n\n"
        f"User Prompt: {user_prompt}\n\n"
    )
    message = HumanMessage(content=evaluation_prompt)
    response = model.stream([message])
    return ''.join([r.content for r in response])  # Concatenate response chunks

def generate_best_prompt(problem_statement):
    improvement_prompt = f"Generate the best possible prompt for the following problem statement: {problem_statement}. The prompt should be made utilizing core prompt engineering skills, understanding the prerequisites needed etc and should be brief. The prompt should be 10/10 and contain the critics mentioned in the evaluation of the user prompt. Best Prompt:"
    message = HumanMessage(content=improvement_prompt)
    response = model.stream([message])
    return ''.join([r.content for r in response])  # Concatenate response chunks

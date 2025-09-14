import streamlit as st
from openai import OpenAI

# Load API key securely from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Career Planner AI")
st.write("🚀 AI-powered mentor to generate personalized career roadmaps.")

# User input
career_goal = st.text_input("Enter your career goal (e.g., Data Scientist, Web Developer):")
timeline = st.selectbox("Timeline to achieve this goal:", ["3 months", "6 months", "1 year", "2 years"])

if st.button("Generate Roadmap") and career_goal:
    with st.spinner("Generating roadmap..."):
        try:
            prompt = f"""
            You are a career mentor. Generate a step-by-step roadmap for someone who wants to become a 
            {career_goal} within {timeline}. Break it into skills, stages, and suggest free resources for each skill.
            """

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=600,
                temperature=0.7
            )

            roadmap = response.choices[0].message.content.strip()
            st.markdown("### Your Career Roadmap")
            st.markdown(roadmap.replace("\n", "\n\n"))

        except Exception as e:
            st.error(f"Error generating roadmap: {e}")

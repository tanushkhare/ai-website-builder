import streamlit as st

st.set_page_config(page_title="AI Website Generator", layout="wide")

st.title("🚀 AI Website Generator")

prompt = st.text_area(
    "Describe the website",
    placeholder="Create a modern AI startup website with Home, About and Contact pages..."
)

theme = st.selectbox(
    "Theme",
    ["Dark", "Light", "Luxury"]
)

if st.button("Generate Website"):
    st.info("Generating website...")

    # Call your existing generator here
    # generate_website(prompt, theme)

    st.success("Website generated successfully!")
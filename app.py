# legal_advisor_gemini_direct_key.py
import streamlit as st
import google.generativeai as genai

# --- Gemini API Configuration (INSECURE - DO NOT DO THIS FOR PRODUCTION) ---
GEMINI_API_KEY = "AIzaSyCsmckjASuCwZ8R22I5KwiK1IANJEAEJzg"  # Replace with your actual API key

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# --- Function to Interact with Gemini API for Legal Advice ---
def get_legal_advice(query):
    """
    Calls the Gemini API with the given legal query and returns the response.
    """
    prompt = f"""You are a helpful and knowledgeable legal advisor for India.
    Based on your understanding of Indian law, provide guidance and information
    related to the following query:

    {query}

    Please note that this is for informational purposes only and does not constitute
    formal legal advice. Always consult with a qualified legal professional for
    specific legal matters.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while calling the Gemini API: {e}"

# --- Streamlit Application ---
st.title("🇮🇳 Indian Legal Advisor (Powered by Gemini AI)")
st.markdown("Ask a question about Indian law and receive informational guidance.")
st.markdown("_Disclaimer: This is a basic PoC and the information provided is for general informational purposes only. It does not constitute legal advice. Consult with a qualified legal professional for specific legal matters._")

legal_query = st.text_area("Enter your legal query:", height=150)

if st.button("Get Advice"):
    if legal_query:
        with st.spinner("Consulting the Legal AI..."):
            legal_response = get_legal_advice(legal_query)
        st.subheader("Legal Guidance:")
        st.markdown(legal_response)
    else:
        st.warning("Please enter your legal query.")

# --- Instructions for Running ---
st.sidebar.header("How to Run:")
st.sidebar.markdown("""
1.  **Save this code** as a Python file (e.g., `legal_advisor_direct_key.py`).
2.  **Replace `"YOUR_API_KEY"`** in the code with your actual Gemini API key.
3.  **Install necessary libraries:**
    ```bash
    pip install streamlit google-generativeai
    ```
4.  **Run the Streamlit app:**
    ```bash
    streamlit run legal_advisor_direct_key.py
    ```
5.  Open your web browser to the address displayed by Streamlit (usually `http://localhost:8501`).
""")
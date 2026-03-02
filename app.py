import streamlit as st
import requests

# --- THE BRAIN CONNECTOR ---
def get_ai_response(user_prompt):
    # Using the "Fast Brain" (Gemma) to bypass the loading delays
    API_URL = "https://api-inference.huggingface.co/models/google/gemma-1.1-2b-it"
    headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
    
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": user_prompt})
        # Extracting the text from the AI's response
        return response.json()[0]['generated_text']
    except:
        return "The AI Brain is still loading. Please wait 10 seconds and try again."

# --- APP LAYOUT ---
st.set_page_config(page_title="Nexus-Aegis AI", layout="wide")

# Sidebar Status
st.sidebar.title("🛡️ NEXUS-AEGIS")
if "HF_TOKEN" in st.secrets:
    st.sidebar.success("✅ Brain: ONLINE")
else:
    st.sidebar.error("❌ Brain: OFFLINE (Check Secrets)")

# Room Selection
mode = st.sidebar.radio("Mission Control:", ["Pathfinder", "Aegis Sentinel"])

if mode == "Pathfinder":
    st.title("🧠 Career Pathfinder")
    job = st.text_input("What is your 2026 dream job?")
    if st.button("Generate Career GPS"):
        with st.spinner("Consulting the AI..."):
            result = get_ai_response(f"Provide a 3-step career plan for a {job} in 2026.")
            st.write(result)

elif mode == "Aegis Sentinel":
    st.title("🚦 Aegis Sentinel")
    idea = st.text_area("Describe an AI system to audit:")
    if st.button("Run Ethics Audit"):
        with st.spinner("Scanning for Bias & Risk..."):
            audit = get_ai_response(f"Audit this AI idea for ethical risks: {idea}")
            st.warning("⚠️ Sentinel Analysis:")
            st.write(audit)

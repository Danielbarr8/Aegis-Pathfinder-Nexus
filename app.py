import streamlit as st
import requests

def get_ai_response(user_prompt):
    # THE 2026 PRECISION ROUTE
    API_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.2"
    
    headers = {
        "Authorization": f"Bearer {st.secrets['HF_TOKEN']}",
        "X-Wait-For-Model": "true" # This forces the brain to wake up BEFORE answering
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": user_prompt})
        
        if response.status_code == 200:
            return response.json()[0]['generated_text']
        else:
            return f"⚠️ SYSTEM STATUS {response.status_code}: {response.text}"
            
    except Exception as e:
        return f"🚨 CONNECTION ERROR: {str(e)}"

# --- APP LAYOUT ---
st.set_page_config(page_title="Nexus-Aegis AI", layout="wide")

st.sidebar.title("🛡️ NEXUS-AEGIS")
st.sidebar.info("2026 Sovereign Governance")

mode = st.sidebar.radio("Mission Control:", ["Pathfinder", "Aegis Sentinel"])

if mode == "Pathfinder":
    st.title("🧠 Career Pathfinder")
    job = st.text_input("What is your 2026 dream job?")
    if st.button("Generate Career GPS"):
        with st.spinner("Connecting to the Mistral Brain..."):
            ans = get_ai_response(f"Provide a 3-step career plan for {job}.")
            st.write(ans)

elif mode == "Aegis Sentinel":
    st.title("🚦 Aegis Sentinel")
    idea = st.text_area("AI Idea to Audit:")
    if st.button("Run Ethics Audit"):
        with st.spinner("Running 2026 Compliance Scan..."):
            ans = get_ai_response(f"Audit this AI idea for ethical risks: {idea}")
            st.write(ans)

import streamlit as st
import requests

def get_ai_response(user_prompt):
    # THE 2026 HUB-ROUTER ADDRESS
    # This format is the most stable for serverless 2026 calls
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    
    headers = {
        "Authorization": f"Bearer {st.secrets['HF_TOKEN']}",
        "x-wait-for-model": "true"
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": user_prompt})
        
        # If the direct route 410s again, the code will automatically try the alternate Router link
        if response.status_code == 410:
            ALT_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.2"
            response = requests.post(ALT_URL, headers=headers, json={"inputs": user_prompt})

        if response.status_code == 200:
            return response.json()[0]['generated_text']
        else:
            return f"⚠️ SYSTEM STATUS {response.status_code}: {response.text}"
            
    except Exception as e:
        return f"🚨 CONNECTION ERROR: {str(e)}"

# --- APP LAYOUT ---
st.set_page_config(page_title="Nexus-Aegis AI", layout="wide")
st.sidebar.title("🛡️ NEXUS-AEGIS")

mode = st.sidebar.radio("Mission Control:", ["Pathfinder", "Aegis Sentinel"])

if mode == "Pathfinder":
    st.title("🧠 Career Pathfinder")
    job = st.text_input("What is your 2026 dream job?")
    if st.button("Generate Career GPS"):
        with st.spinner("Consulting the AI..."):
            ans = get_ai_response(f"Provide a 3-step career plan for {job}.")
            st.write(ans)

elif mode == "Aegis Sentinel":
    st.title("🚦 Aegis Sentinel")
    idea = st.text_area("AI Idea to Audit:")
    if st.button("Run Ethics Audit"):
        with st.spinner("Scanning for Risks..."):
            ans = get_ai_response(f"Audit this AI idea for ethical risks: {idea}")
            st.write(ans)

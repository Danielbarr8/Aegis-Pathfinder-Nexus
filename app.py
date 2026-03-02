import streamlit as st
import requests

def get_ai_response(user_prompt):
    # The 'Brain' Address
    API_URL = "https://api-inference.huggingface.co/models/google/gemma-1.1-2b-it"
    headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
    
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": user_prompt})
        
        # If successful
        if response.status_code == 200:
            return response.json()[0]['generated_text']
        
        # If the brain is still loading (This is normal for the first 30 seconds)
        elif response.status_code == 503:
            return "🕒 The Brain is still warming up. Wait 15 seconds and click again."
        
        # If there is a problem with your Token (The 'Key')
        elif response.status_code == 401:
            return "❌ ERROR 401: Your Hugging Face Token is invalid. Double-check your Streamlit Secrets!"
        
        # Any other error
        else:
            return f"⚠️ SYSTEM ERROR {response.status_code}: {response.text}"
            
    except Exception as e:
        return f"🚨 CRITICAL ERROR: {str(e)}"

# --- APP LAYOUT ---
st.set_page_config(page_title="Nexus-Aegis AI", layout="wide")

st.sidebar.title("🛡️ NEXUS-AEGIS")
if "HF_TOKEN" in st.secrets:
    st.sidebar.success("✅ Vault: CONNECTED")
else:
    st.sidebar.error("❌ Vault: DISCONNECTED")

mode = st.sidebar.radio("Mission Control:", ["Pathfinder", "Aegis Sentinel"])

if mode == "Pathfinder":
    st.title("🧠 Career Pathfinder")
    job = st.text_input("What is your 2026 dream job?")
    if st.button("Generate Career GPS"):
        with st.spinner("Consulting the Nexus Brain..."):
            ans = get_ai_response(f"Provide a 3-step career plan for {job}.")
            st.write(ans)

elif mode == "Aegis Sentinel":
    st.title("🚦 Aegis Sentinel")
    idea = st.text_area("AI Idea to Audit:")
    if st.button("Run Ethics Audit"):
        with st.spinner("Scanning for Risks..."):
            ans = get_ai_response(f"Audit this AI idea for ethical risks: {idea}")
            st.write(ans)

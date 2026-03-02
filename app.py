import streamlit as st
import requests

# --- THE 2026 HUB-ROUTER BRAIN ---
def get_ai_response(user_prompt):
    # This is the exact 2026 path discovered through research
    API_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.2"
    
    headers = {
        "Authorization": f"Bearer {st.secrets['HF_TOKEN']}",
        "Content-Type": "application/json",
        "x-wait-for-model": "true"
    }
    
    # Mistral 2026 format requires a specific prompt structure
    payload = {
        "inputs": f"<s>[INST] {user_prompt} [/INST]</s>",
        "parameters": {"max_new_tokens": 250, "temperature": 0.7}
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            # Handle list or dict response
            if isinstance(result, list):
                return result[0].get('generated_text', 'No text returned.')
            return result.get('generated_text', 'Format error.')
        else:
            return f"⚠️ SYSTEM STATUS {response.status_code}: {response.text}"
            
    except Exception as e:
        return f"🚨 CONNECTION ERROR: {str(e)}"

# --- APP LAYOUT ---
st.set_page_config(page_title="Nexus-Aegis 2026", layout="wide")
st.sidebar.title("🛡️ NEXUS-AEGIS")

mode = st.sidebar.radio("Mission Control:", ["Pathfinder", "Aegis Sentinel"])

if mode == "Pathfinder":
    st.title("🧠 Career Pathfinder")
    job = st.text_input("Enter your 2026 dream job:")
    if st.button("Generate Career GPS"):
        with st.spinner("Consulting the Router..."):
            ans = get_ai_response(f"Provide a 3-step career plan for {job}.")
            # Clean up the response to remove the prompt markers
            clean_ans = ans.split("[/INST]</s>")[-1] if "[/INST]</s>" in ans else ans
            st.write(clean_ans)

elif mode == "Aegis Sentinel":
    st.title("🚦 Aegis Sentinel")
    idea = st.text_area("AI Idea to Audit:")
    if st.button("Run Ethics Audit"):
        with st.spinner("Scanning 2026 Compliance..."):
            ans = get_ai_response(f"Audit this AI idea for ethical risks: {idea}")
            clean_ans = ans.split("[/INST]</s>")[-1] if "[/INST]</s>" in ans else ans
            st.warning("⚠️ Sentinel Analysis:")
            st.write(clean_ans)

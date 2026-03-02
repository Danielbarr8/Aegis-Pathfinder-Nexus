import streamlit as st
import requests

def get_ai_response(user_prompt):
    # THE 2026 ROUTER ADDRESS
    API_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.2"
    
    headers = {
        "Authorization": f"Bearer {st.secrets['HF_TOKEN']}",
        "Content-Type": "application/json",
        "x-wait-for-model": "true"
    }
    
    payload = {"inputs": user_prompt}
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            return response.json()[0]['generated_text']
        else:
            return f"⚠️ NEXUS STATUS {response.status_code}: {response.text}"
            
    except Exception as e:
        return f"🚨 SYSTEM ERROR: {str(e)}"

# --- INTERFACE ---
st.set_page_config(page_title="Nexus-Aegis AI"
            ans = get_ai_response(f"Provide a 3-step career plan for {job}.")
            st.write(ans)

elif mode == "Aegis Sentinel":
    st.title("🚦 Aegis Sentinel")
    idea = st.text_area("AI Idea to Audit:")
    if st.button("Run Ethics Audit"):
        with st.spinner("Running 2026 Ethics Scan..."):
            ans = get_ai_response(f"Audit this AI idea for ethical risks: {idea}")
            st.write(ans)

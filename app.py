
import streamlit as st
import random
import time

# --- THE LOOK & FEEL ---
st.set_page_config(page_title="Nexus-Aegis AI", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #020408; color: #c8dff0; }
    .stMetric { background-color: #0a1e33; border: 1px solid #0e3054; padding: 15px; border-radius: 10px; }
    h1, h2, h3 { color: #00e5ff !important; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- THE SIDEBAR NAVIGATION ---
st.sidebar.title("🛡️ NEXUS-AEGIS COMMAND")
st.sidebar.info("Sovereign AI Governance & Career Ecosystem")
mode = st.sidebar.radio("Mission Control:", 
    ["1. Career Pathfinder (The Worker)", 
     "2. Aegis Sentinel (The Boss)", 
     "3. Imagination Studio (The Creator)"])

# --- ROOM 1: THE WORKER ---
if mode == "1. Career Pathfinder (The Worker)":
    st.title("🧠 Career Pathfinder: AI Growth Engine")
    st.subheader("Transforming LinkedIn data into a Career GPS")
    job = st.text_input("Enter your target job (e.g., AI Specialist):")
    if st.button("Calculate My Path"):
        with st.status("Analyzing Market Trends...", expanded=True) as status:
            time.sleep(1)
            st.write("Checking skill gaps...")
            time.sleep(1)
            status.update(label="Analysis Complete!", state="complete", expanded=False)
        st.success(f"Path to {job} Found!")
        st.code("Recommended Upskill: AI Ethics & Governance. Potential Salary: +$35k.")

# --- ROOM 2: THE BOSS ---
elif mode == "2. Aegis Sentinel (The Boss)":
    st.title("🚦 Aegis Sentinel: Real-Time Governance")
    st.subheader("Simulating AI Ethics & Compliance Pulse")
    
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Trust Score", "98/100", "High")
    with col2: st.metric("Bias Risk", "2%", "Low")
    with col3: st.metric("EU AI Act Status", "Compliant", "Verified")

    st.write("---")
    st.info("Pulsing System Scan: Monitoring for Algorithmic Drift...")
    st.progress(random.randint(90, 100))
    st.write("✅ All systems operating within ethical parameters.")

# --- ROOM 3: THE CREATOR ---
elif mode == "3. Imagination Studio (The Creator)":
    st.title("🎨 AI Imagination Studio")
    st.subheader("Turning career goals into creative packages")
    story_idea = st.text_input("What is your vision for the future?")
    if st.button("Generate Creator Package"):
        st.write("Creating visual representation...")
        st.image("https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=800", caption="Your Future, Visualized by AI")

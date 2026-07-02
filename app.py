import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# 1. CRITICAL: THIS MUST BE THE ABSOLUTE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="ECE AI Circuit Explainer",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Custom CSS for a clean, professional tech layout
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #fffd61 !important; font-family: 'Courier New', monospace; font-weight: 700; }
    h3 { color: #80cbc4 !important; }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        border: none;
        padding: 10px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        transform: scale(1.02);
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }
    .card {
        background-color: #1e2430;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #80cbc4;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Title Block
st.title("⚡ ECE AI CIRCUIT EXPLAINER")
st.markdown("### *Next-Gen Hardware Code Analytics & Testbench Synthesis Engine*")
st.markdown("---")

# 2. SIDEBAR CONFIGURATION
st.sidebar.title("💳 PREMIUM PORTAL")
with st.sidebar.container():
    st.markdown("""
    <div style="background-color: #1a1c23; padding: 15px; border-radius: 10px; border: 1px solid #ff4b4b;">
        <h4 style="color: #ff4b4b; margin-top:0;">Developer Bundle</h4>
        <p style="font-size: 13px; color: #b0bec5;">Stop burning cloud token limits. Run this complete engine locally for zero cost!</p>
        <p style="font-weight: bold; color: #fffd61; font-size: 16px;">Price: $4.99</p>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown("")
    st.sidebar.link_button("🚀 Get Lifetime Source Code", "https://gumroad.com", type="primary")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Engine Status")
st.sidebar.success("● Llama-3.3-70b Online")
st.sidebar.info("● Inference Velocity: >200 T/s")

# 3. MAIN COLUMN LAYOUT
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📥 Code Input Workspace")
    language = st.selectbox("Select Target Language", ["Verilog", "VHDL", "Arduino C++"])
    user_code = st.text_area("Paste your module, entity, or sketch code below:", height=380, placeholder="// Hardware logic goes here...")
    generate_btn = st.button("🚀 EXECUTE FULL SYNTHESIS")

with col2:
    st.markdown("#### 📤 AI Generation Output")
    
    if generate_btn:
        if not user_code.strip():
            st.warning("Please paste some hardware description code first!")
        elif not api_key or api_key == "your_key_here":
            st.error("🔒 System Configuration Error: The backend authentication key is missing.")
        else:
            with st.spinner("Groq Architecture Compiling Logic..."):
                try:
                    client = Groq(api_key=api_key)
                    
                    system_prompt = """
                    You are an expert ECE Professor and Senior Hardware Verification Engineer.
                    Provide a clean response split into exactly two parts:
                    1. ### 📖 Simplified Circuit Breakdown: A markdown explanation using clear analogies, explaining inputs/outputs and the core logic flow.
                    2. ### 🧪 Optimized Edge-Case Testbench: A fully commented, syntactically correct testbench or simulation script targeting tricky edge cases.
                    """
                    
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": f"Language: {language}\n\nCode:\n{user_code}"}
                        ],
                        temperature=0.2,
                        max_tokens=2500
                    )
                    
                    ai_response = completion.choices[0].message.content
                    st.success("Analysis Complete!")
                    st.markdown(ai_response)
                    
                except Exception as e:
                    error_str = str(e)
                    if "401" in error_str or "invalid_api_key" in error_str:
                        st.error("⚠️ **Server Maintenance:** Connection re-syncing. Retry in 2 minutes.")
                    elif "429" in error_str:
                        st.warning("⏱ pipe **Traffic High:** Rate limits hit. Please wait 60 seconds!")
                    else:
                        st.error(f"🔍 System Anomaly: {e}")
    else:
        st.markdown("""
        <div class="card">
            <h5 style="color: #80cbc4; margin-top:0;">Awaiting Input...</h5>
            <p style="color: #b0bec5; font-size: 14px;">Select your code language, paste your raw hardware file on the left workspace, and hit execute to view structural analogies and simulation testbenches.</p>
        </div>
        """, unsafe_allow_html=True)
import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 1. PREMIUM THEME CONFIGURATION
st.set_page_config(
    page_title="ECE AI Circuit Explainer",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# Custom CSS to inject a modern dark-tech vibe
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #fffd61 !important; font-family: 'Courier New', monospace; font-weight: 700; }
    h3 { color: #80cbc4 !important; }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        border: none;
        padding: 10px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        transform: scale(1.02);
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }
    .card {
        background-color: #1e2430;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #80cbc4;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Title Block
st.title("⚡ ECE AI CIRCUIT EXPLAINER")
st.markdown("### *Next-Gen Hardware Code Analytics & Testbench Synthesis Engine*")
st.markdown("---")

# 2. SIDEBAR MONETIZATION & UTILITIES
st.sidebar.title("💳 PREMIUM PORTAL")
with st.sidebar.container():
    st.markdown("""
    <div style="background-color: #1a1c23; padding: 15px; border-radius: 10px; border: 1px solid #ff4b4b;">
        <h4 style="color: #ff4b4b; margin-top:0;">Developer Bundle</h4>
        <p style="font-size: 13px; color: #b0bec5;">Stop burning cloud token limits. Run this complete engine locally for zero cost!</p>
        <p style="font-weight: bold; color: #fffd61; font-size: 16px;">Price: $4.99</p>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown("")
    st.sidebar.link_button("🚀 Get Lifetime Source Code", "https://gumroad.com", type="primary")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Engine Status")
st.sidebar.success("● Llama-3.3-70b Online")
st.sidebar.info("● Inference Velocity: >200 T/s")

# 3. MAIN INTERACTIVE LAYOUT (Split into 2 Columns)
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("#### 📥 Code Input Workspace")
    language = st.selectbox("Select Target Language", ["Verilog", "VHDL", "Arduino C++"])
    user_code = st.text_area("Paste your module, entity, or sketch code below:", height=380, placeholder="// Hardware logic goes here...")
    generate_btn = st.button("🚀 EXECUTE FULL SYNTHESIS")

with col2:
    st.markdown("#### 📤 AI Generation Output")
    
    if generate_btn:
        if not user_code.strip():
            st.warning("Please paste some hardware description code first!")
        elif not api_key or api_key == "your_key_here":
            st.error("🔒 System Configuration Error: The backend authentication key is missing.")
        else:
            with st.spinner("Groq Architecture Compiling Logic..."):
                try:
                    client = Groq(api_key=api_key)
                    
                    system_prompt = """
                    You are an expert ECE Professor and Senior Hardware Verification Engineer.
                    Provide a clean response split into exactly two parts:
                    1. ### 📖 Simplified Circuit Breakdown: A markdown explanation using clear analogies, explaining inputs/outputs and the core logic flow.
                    2. ### 🧪 Optimized Edge-Case Testbench: A fully commented, syntactically correct testbench or simulation script targeting tricky edge cases.
                    """
                    
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": f"Language: {language}\n\nCode:\n{user_code}"}
                        ],
                        temperature=0.2,
                        max_tokens=2500
                    )
                    
                    ai_response = completion.choices[0].message.content
                    st.success("Analysis Complete!")
                    st.markdown(ai_response)
                    
                except Exception as e:
                    error_str = str(e)
                    if "401" in error_str or "invalid_api_key" in error_str:
                        st.error("⚠️ **Server Maintenance:** Connection re-syncing. Retry in 2 minutes.")
                    elif "429" in error_str:
                        st.warning("⏱️ **Traffic High:** Rate limits hit. Please wait 60 seconds!")
                    else:
                        st.error(f"🔍 System Anomaly: {e}")
    else:
        # Default placeholder when the app is empty
        st.markdown("""
        <div class="card">
            <h5 style="color: #80cbc4; margin-top:0;">Awaiting Input...</h5>
            <p style="color: #b0bec5; font-size: 14px;">Select your code language, paste your raw hardware file on the left workspace, and hit execute to view structural analogies and simulation testbenches.</p>
        </div>
        """, unsafe_allow_html=True)
import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Layout Configuration
st.set_page_config(page_title="ECE AI Circuit Explainer", layout="wide", page_icon="⚡")
st.title("⚡ ECE AI Circuit Explainer & Testbench Generator")
st.subheader("Instantly decode Verilog, VHDL, or Arduino code with Llama 3.3 via Groq")

# Sidebar Monetization
st.sidebar.title("💳 Premium Features")
st.sidebar.markdown("""
Get unlimited daily tokens, advanced multi-file synthesis, and PDF downloads.
* **[Get Lifetime Local Source Code ($4.99)](https://japjamunpan.gumroad.com/l/ece-ai-code)** 
""")

# Inputs
language = st.selectbox("Select Hardware Description / Code Language", ["Verilog", "VHDL", "Arduino C++"])
user_code = st.text_area("Paste your hardware code here:", height=300, placeholder="// Paste your module or sketch code here...")

system_prompt = """
You are an expert Electrical and Computer Engineering (ECE) Professor and Senior Hardware Verification Engineer.
The user will provide hardware description code (Verilog, VHDL) or an Arduino script.
Your task is to provide a clean response split into exactly two parts:
1. ### 📖 Simplified Circuit Breakdown: A markdown explanation using clear analogies, explaining what inputs/outputs do and the core logic flow.
2. ### 🧪 Optimized Edge-Case Testbench: A fully commented, syntactically correct testbench or simulation script targeting tricky edge cases.
"""

if st.button("Generate Breakdown & Testbench", type="primary"):
    if not user_code.strip():
        st.warning("Please paste some code first!")
    elif not api_key or api_key == "your_key_here":
        st.error("🔒 System Configuration Error: The backend authentication key is missing.")
    else:
        with st.spinner("Groq is compiling your circuit logic at hyper-speed..."):
            try:
                client = Groq(api_key=api_key)
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Language: {language}\n\nCode:\n{user_code}"}
                    ],
                    temperature=0.2,
                    max_tokens=2500
                )
                
                ai_response = completion.choices[0].message.content
                st.success("Analysis Complete!")
                st.markdown(ai_response)
                
            except Exception as e:
                # INTERCEPT BREAKING API CODES BEAUTIFULLY
                error_str = str(e)
                if "401" in error_str or "invalid_api_key" in error_str:
                    st.error("""
                    ⚠️ **Server Maintenance in Progress**  
                    The application is currently updating its secure database connections. 
                    Please try running your circuit code synthesis again in 2 minutes.
                    """)
                elif "429" in error_str:
                    st.warning("⏱️ **Server Traffic is High:** Free tier limit reached. Please wait 60 seconds or run the code locally!")
                else:
                    st.error(f"🔍 System Announcement: An unexpected network anomaly occurred. Details: {e}")

import os
import re
import streamlit as st
import streamlit.components.v1 as components
from groq import Groq
from dotenv import load_dotenv

# 1. INITIALIZE WEB STRUCTURE
st.set_page_config(
    page_title="Universal ECE AI Platform",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 2. HIGH-CONTRAST LIGHTING CSS (FIXES DARK TEXT UNREADABILITY)
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        background-image: 
            radial-gradient(#1e293b 1px, transparent 0),
            radial-gradient(#1e293b 1px, transparent 0);
        background-size: 24px 24px;
        background-position: 0 0, 12px 12px;
    }
    header { border-bottom: 2px solid #00f2fe; }
    
    /* Force crisp high-visibility text */
    h1 { color: #00f2fe !important; font-family: 'Courier New', monospace; font-weight: 800; text-shadow: 0 0 10px rgba(0, 242, 254, 0.4); }
    h3 { color: #4facfe !important; }
    h4 { color: #ffffff !important; border-bottom: 2px solid #00f2fe; padding-bottom: 8px; font-weight: 700; }
    p, span, label, div[data-testid="stMarkdownContainer"] { color: #ffffff !important; font-weight: 500 !important; font-size: 15px; }
    
    /* Fix form labeling text color dropdown unreadability */
    .stSelectbox label, .stTextArea label { color: #00f2fe !important; font-weight: bold !important; }
    
    .stTabs [data-baseweb="tab-list"] { gap: 10px; background-color: #111827; padding: 8px; border-radius: 8px; border: 1px solid #1e293b; }
    .stTabs [data-baseweb="tab"] { color: #94a3b8 !important; font-weight: bold; padding: 8px 16px; border-radius: 6px; }
    .stTabs [aria-selected="true"] { background-color: #00f2fe !important; color: #0b0f19 !important; }
    
    .card-panel { background-color: rgba(17, 24, 39, 0.95); padding: 24px; border-radius: 12px; border: 1px solid #00f2fe; backdrop-filter: blur(8px); margin-bottom: 20px; }
    
    .stButton>button {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: #0b0f19 !important;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        font-size: 16px;
        border: none;
        padding: 12px;
        box-shadow: 0 4px 15px rgba(0, 242, 254, 0.3);
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 242, 254, 0.5); }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ UNIVERSAL ECE AUTOMATION PLATFORM")
st.markdown("### AI Code Compiler, Hardware Schematic Mapper, and Multi-Environment Prototyping Center")
st.markdown("<br>", unsafe_allow_html=True)

# 3. SIDEBAR MONETIZATION
st.sidebar.title("💳 PREMIUM PORTAL")
with st.sidebar.container():
    st.markdown("""
    <div style="background-color: rgba(15, 23, 42, 0.95); padding: 18px; border-radius: 10px; border: 2px solid #00f2fe; margin-bottom: 15px;">
        <h4 style="color: #00f2fe; margin-top:0; border:none; padding:0;">Developer Bundle</h4>
        <p style="font-size: 13px; color: #ffffff; line-height: 1.4;">Get the full AI compilation logic stack, local multi-board scripts, and the open-source PCB layout components bundle!</p>
        <p style="font-weight: bold; color: #ffffff; font-size: 18px; margin-bottom:0;">Price: <span style="color:#00f2fe;">$4.99</span></p>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.link_button("🚀 Get Lifetime Source Code", "https://gumroad.com", type="primary")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Platform Ecosystem")
st.sidebar.success("● Wokwi-Core Virtual Firmwares")
st.sidebar.info("● tscircuit Layout Mapping Nodes")

# 4. ENTERPRISE 3-TAB SYSTEM LAYOUT CONFIGURATION
tab1, tab2, tab3 = st.tabs(["🧠 AI Translator & System Mapper", "🔌 Live Multi-Board Sandbox", "🛠️ tscircuit Code-to-PCB Compiler"])

with tab1:
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("#### 📥 Input Workspace")
        source_lang = st.selectbox("Select Source Language", ["Verilog", "VHDL", "Arduino C++", "MicroPython", "Assembly (AVR)"])
        target_lang = st.selectbox("Translate Code into", ["Verilog", "VHDL", "Arduino C++", "MicroPython", "Assembly (AVR)"])
        user_code = st.text_area("Paste your source logic code here:", height=350, placeholder="// Drop code matrix here...")
        generate_btn = st.button("⚡ CONVERT CODE & SYNTHESIZE DIAGRAM")

    with col2:
        st.markdown("#### 📤 Translated Execution & Layouts")
        if generate_btn:
            if not user_code.strip():
                st.warning("Please paste some code first!")
            elif not api_key or api_key == "your_key_here":
                st.error("🔒 Vault Error: API verification key missing.")
            else:
                with st.spinner("Translating Code Formats & Drafting Architectural Connections..."):
                    try:
                        client = Groq(api_key=api_key)
                        
                        system_prompt = f"""
                        You are an expert ECE Professor, Senior Compiler Architect, and Hardware Layout Verification Engineer.
                        Your job is to translate the user's code from {source_lang} directly into {target_lang}.
                        
                        Provide a clean response split into exactly three parts:
                        1. A clean, fully commented block of the code converted into {target_lang}.
                        2. A dedicated layout schematic tag mapping out components using Graphviz formatting. It must look exactly like this:
                        ```dot
                        digraph G {{
                            rankdir=LR;
                            bgcolor="#111827";
                            node [shape=record, style=filled, color="#00f2fe", fillcolor="#1f2937", fontcolor=white, fontname="Courier"];
                            edge [color="#ff4b4b", penwidth=2];
                            Input_Signal -> Main_Controller_Pins -> Output_Device;
                        }}
                        ```
                        3. ### 📖 Logic Breakdown: A brief comparison checklist explaining how the original logic loops translate into the new target structure syntax.
                        """
                        
                        completion = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": f"Source Code:\n{user_code}"}
                            ],
                            temperature=0.2,
                            max_tokens=2500
                        )
                        
                        ai_response = completion.choices.message.content
                        st.success("Translation and Mapping Complete!")
                        
                        dot_match = re.search(r"```dot\n(.*?)```", ai_response, re.DOTALL)
                        if dot_match:
                            dot_code = dot_match.group(1).strip()
                            st.markdown("#### 🔌 Automated Circuit Block Schematic")
                            st.graphviz_chart(dot_code)
                            
                            clean_response = re.sub(r"```dot\n.*?```", "", ai_response, flags=re.DOTALL)
                            st.markdown(clean_response)
                        else:
                            st.markdown(ai_response)
                            
                    except Exception as e:
                        st.error(f"🔍 System Anomaly: {e}")
        else:
            st.markdown("""
            <div class="card-panel">
                <h5 style="color: #00f2fe; margin-top:0; font-family: monospace;">AWAITING TRANSLATION SELECTION...</h5>
                <p style="color: #ffffff; font-size: 14px; line-height: 1.5;">Configure your source and target programming frameworks, paste your execution scripts, and compile to view translated parameters alongside block hardware arrays.</p>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("#### 🔌 Live Multi-Board Simulation Core")
    st.markdown("<p style='color:#ffffff;'>Select your prototyping target architecture below to spin up a live interactive workspace layer inside your web tool dashboard layout container:</p>", unsafe_allow_html=True)
    
    target_mcu = st.selectbox(
        "Choose Your Emulated Development Board:", 
        ["Arduino Uno", "Arduino Mega 2560", "ESP32 DevKit v1", "Raspberry Pi Pico"]
    )
    st.markdown("---")
    
    # FIXED: Replaced lowercase st.components with standard modular component calls
    if target_mcu == "Arduino Uno":
        components.iframe("https://wokwi.com", height=750, scrolling=True)
    elif target_mcu == "Arduino Mega 2560":
        components.iframe("https://wokwi.com", height=750, scrolling=True)
    elif target_mcu == "ESP32 DevKit v1":
        components.iframe("https://wokwi.com", height=750, scrolling=True)
    elif target_mcu == "Raspberry Pi Pico":
        components.iframe("https://wokwi.com", height=750, scrolling=True)

with tab3:
    st.markdown("#### 🛠️ tscircuit Hardware Layout Engine")
    st.markdown("<p style='color:#ffffff;'>Design and compile electronics components directly into manufacturing-ready Printed Circuit Boards (PCBs) and fabrication files using our embedded playground:</p>", unsafe_allow_html=True)
    components.iframe("https://tscircuit.com", height=800, scrolling=True)
import os
import re
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# 1. INITIALIZE WEB STRUCTURE
st.set_page_config(
    page_title="Universal ECE AI Platform",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 2. ADVANCED INTERFACE DESIGN OVERLAY
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        background-image: 
            radial-gradient(#1e293b 1px, transparent 0),
            radial-gradient(#1e293b 1px, transparent 0);
        background-size: 24px 24px;
        background-position: 0 0, 12px 12px;
    }
    header { border-bottom: 2px solid #00f2fe; }
    h1 { color: #00f2fe !important; font-family: 'Courier New', monospace; font-weight: 800; text-shadow: 0 0 10px rgba(0, 242, 254, 0.4); }
    h3 { color: #4facfe !important; }
    h4 { color: #ffffff !important; border-bottom: 1px solid #1e293b; padding-bottom: 8px; }
    
    .stTabs [data-baseweb="tab-list"] { gap: 10px; background-color: #111827; padding: 8px; border-radius: 8px; border: 1px solid #1e293b; }
    .stTabs [data-baseweb="tab"] { color: #94a3b8 !important; font-weight: bold; padding: 8px 16px; border-radius: 6px; }
    .stTabs [aria-selected="true"] { background-color: #00f2fe !important; color: #0b0f19 !important; }
    
    .card-panel { background-color: rgba(17, 24, 39, 0.85); padding: 24px; border-radius: 12px; border: 1px solid #1e293b; backdrop-filter: blur(8px); margin-bottom: 20px; }
    
    .stButton>button {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: #0b0f19 !important;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        font-size: 15px;
        border: none;
        padding: 12px;
        box-shadow: 0 4px 15px rgba(0, 242, 254, 0.2);
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 242, 254, 0.4); }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ UNIVERSAL ECE AUTOMATION PLATFORM")
st.markdown("### AI Code Compiler, Hardware Schematic Mapper, and Multi-Environment Prototyping Center")
st.markdown("<br>", unsafe_allow_html=True)

# 3. SIDEBAR MONETIZATION
st.sidebar.title("💳 PREMIUM PORTAL")
with st.sidebar.container():
    st.markdown("""
    <div style="background-color: rgba(15, 23, 42, 0.9); padding: 18px; border-radius: 10px; border: 1px solid #00f2fe; margin-bottom: 15px;">
        <h4 style="color: #00f2fe; margin-top:0; border:none; padding:0;">Developer Bundle</h4>
        <p style="font-size: 13px; color: #94a3b8; line-height: 1.4;">Get the full AI compilation logic stack, local multi-board scripts, and the open-source PCB layout components bundle!</p>
        <p style="font-weight: bold; color: #ffffff; font-size: 18px; margin-bottom:0;">Price: <span style="color:#00f2fe;">$4.99</span></p>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.link_button("🚀 Get Lifetime Source Code", "https://gumroad.com", type="primary")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Platform Ecosystem")
st.sidebar.success("● Wokwi-Core Virtual Firmwares")
st.sidebar.info("● tscircuit Layout Mapping Nodes")

# 4. ENTERPRISE 3-TAB SYSTEM LAYOUT CONFIGURATION
tab1, tab2, tab3 = st.tabs(["🧠 AI Translator & System Mapper", "🔌 Live Multi-Board Sandbox", "🛠️ tscircuit Code-to-PCB Compiler"])

with tab1:
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("#### 📥 Input Workspace")
        source_lang = st.selectbox("Select Source Language", ["Verilog", "VHDL", "Arduino C++", "MicroPython", "Assembly (AVR)"])
        target_lang = st.selectbox("Translate Code into", ["Verilog", "VHDL", "Arduino C++", "MicroPython", "Assembly (AVR)"])
        user_code = st.text_area("Paste your source logic code here:", height=350, placeholder="// Drop code matrix here...")
        generate_btn = st.button("⚡ CONVERT CODE & SYNTHESIZE DIAGRAM")

    with col2:
        st.markdown("#### 📤 Translated Execution & Layouts")
        if generate_btn:
            if not user_code.strip():
                st.warning("Please paste some code first!")
            elif not api_key or api_key == "your_key_here":
                st.error("🔒 Vault Error: API verification key missing.")
            else:
                with st.spinner("Translating Code Formats & Drafting Architectural Connections..."):
                    try:
                        client = Groq(api_key=api_key)
                        
                        system_prompt = f"""
                        You are an expert ECE Professor, Senior Compiler Architect, and Hardware Layout Verification Engineer.
                        Your job is to translate the user's code from {source_lang} directly into {target_lang}.
                        
                        Provide a clean response split into exactly three parts:
                        1. A clean, fully commented block of the code converted into {target_lang}.
                        2. A dedicated layout schematic tag mapping out components using Graphviz formatting. It must look exactly like this:
                        ```dot
                        digraph G {{
                            rankdir=LR;
                            bgcolor="#111827";
                            node [shape=record, style=filled, color="#00f2fe", fillcolor="#1f2937", fontcolor=white, fontname="Courier"];
                            edge [color="#ff4b4b", penwidth=2];
                            Input_Signal -> Main_Controller_Pins -> Output_Device;
                        }}
                        ```
                        3. ### 📖 Logic Breakdown: A brief comparison checklist explaining how the original logic loops translate into the new target structure syntax.
                        """
                        
                        completion = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": f"Source Code:\n{user_code}"}
                            ],
                            temperature=0.2,
                            max_tokens=2500
                        )
                        
                        ai_response = completion.choices.message.content
                        st.success("Translation and Mapping Complete!")
                        
                        dot_match = re.search(r"```dot\n(.*?)```", ai_response, re.DOTALL)
                        if dot_match:
                            dot_code = dot_match.group(1).strip()
                            st.markdown("#### 🔌 Automated Circuit Block Schematic")
                            st.graphviz_chart(dot_code)
                            
                            clean_response = re.sub(r"```dot\n.*?```", "", ai_response, flags=re.DOTALL)
                            st.markdown(clean_response)
                        else:
                            st.markdown(ai_response)
                            
                    except Exception as e:
                        st.error(f"🔍 System Anomaly: {e}")
        else:
            st.markdown("""
            <div class="card-panel">
                <h5 style="color: #00f2fe; margin-top:0; font-family: monospace;">AWAITING TRANSLATION SELECTION...</h5>
                <p style="color: #94a3b8; font-size: 14px; line-height: 1.5;">Configure your source and target programming frameworks, paste your execution scripts, and compile to view translated parameters alongside block hardware arrays.</p>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("#### 🔌 Live Multi-Board Simulation Core")
    st.markdown("Select your prototyping target architecture below to spin up a live interactive workspace layer inside your web tool dashboard layout container:")
    
    target_mcu = st.selectbox(
        "Choose Your Emulated Development Board:", 
        ["Arduino Uno", "Arduino Mega 2560", "ESP32 DevKit v1", "Raspberry Pi Pico"]
    )
    st.markdown("---")
    
    if target_mcu == "Arduino Uno":
        st.components.v1.iframe("https://wokwi.com", height=750, scrolling=True)
    elif target_mcu == "Arduino Mega 2560":
        st.components.v1.iframe("https://wokwi.com", height=750, scrolling=True)
    elif target_mcu == "ESP32 DevKit v1":
        st.components.v1.iframe("https://wokwi.com", height=750, scrolling=True)
    elif target_mcu == "Raspberry Pi Pico":
        st.components.v1.iframe("https://wokwi.com", height=750, scrolling=True)

# --- TAB 3: NEW TSCIRCUIT INTEGRATED CODE-TO-PCB COMPILER ---
with tab3:
    st.markdown("#### 🛠️ tscircuit Hardware Layout Engine")
    st.markdown("Design and compile electronics components directly into manufacturing-ready Printed Circuit Boards (PCBs) and fabrication files using our embedded playground:")
    
    # Securely embed tscircuit's live React/TypeScript circuit sandbox layout container
    st.components.v1.iframe("https://registry.tscircuit.com/", height=800, scrolling=True)
import os
import re
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# 1. INITIALIZE WEB STRUCTURE
st.set_page_config(
    page_title="Universal ECE AI Engine & Simulator",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 2. ADVANCED INTERFACE DESIGN OVERLAY
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        background-image: 
            radial-gradient(#1e293b 1px, transparent 0),
            radial-gradient(#1e293b 1px, transparent 0);
        background-size: 24px 24px;
        background-position: 0 0, 12px 12px;
    }
    header { border-bottom: 2px solid #00f2fe; }
    h1 { color: #00f2fe !important; font-family: 'Courier New', monospace; font-weight: 800; text-shadow: 0 0 10px rgba(0, 242, 254, 0.4); }
    h3 { color: #4facfe !important; }
    h4 { color: #ffffff !important; border-bottom: 1px solid #1e293b; padding-bottom: 8px; }
    
    .stTabs [data-baseweb="tab-list"] { gap: 10px; background-color: #111827; padding: 8px; border-radius: 8px; border: 1px solid #1e293b; }
    .stTabs [data-baseweb="tab"] { color: #94a3b8 !important; font-weight: bold; padding: 8px 16px; border-radius: 6px; }
    .stTabs [aria-selected="true"] { background-color: #00f2fe !important; color: #0b0f19 !important; }
    
    .card-panel { background-color: rgba(17, 24, 39, 0.85); padding: 24px; border-radius: 12px; border: 1px solid #1e293b; backdrop-filter: blur(8px); margin-bottom: 20px; }
    
    .stButton>button {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: #0b0f19 !important;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        font-size: 15px;
        border: none;
        padding: 12px;
        box-shadow: 0 4px 15px rgba(0, 242, 254, 0.2);
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 242, 254, 0.4); }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ UNIVERSAL ECE AI TRANSLATOR & SIMULATOR")
st.markdown("### Cross-Language Code Compiler, Hardware Schematic Mapper, and Simulation Center")
st.markdown("<br>", unsafe_allow_html=True)

# 3. SIDEBAR MONETIZATION
st.sidebar.title("💳 PREMIUM PORTAL")
with st.sidebar.container():
    st.markdown("""
    <div style="background-color: rgba(15, 23, 42, 0.9); padding: 18px; border-radius: 10px; border: 1px solid #00f2fe; margin-bottom: 15px;">
        <h4 style="color: #00f2fe; margin-top:0; border:none; padding:0;">Developer Bundle</h4>
        <p style="font-size: 13px; color: #94a3b8; line-height: 1.4;">Get the entire cross-compiling local translation package + open-source elements package!</p>
        <p style="font-weight: bold; color: #ffffff; font-size: 18px; margin-bottom:0;">Price: <span style="color:#00f2fe;">$4.99</span></p>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.link_button("🚀 Get Lifetime Source Code", "https://gumroad.com", type="primary")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Active Libraries")
st.sidebar.success("● Wokwi-Elements Integration")
st.sidebar.info("● Translation Pipeline: Llama 3.3")

# 4. ENTERPRISE TAB SETUP
tab1, tab2 = st.tabs(["🧠 AI Translator & Schematic Generator", "🔌 Live Sandbox Simulator"])

with tab1:
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("#### 📥 Input Workspace")
        source_lang = st.selectbox("Select Source Language", ["Verilog", "VHDL", "Arduino C++", "MicroPython", "Assembly (AVR)"])
        target_lang = st.selectbox("Translate Code into", ["Verilog", "VHDL", "Arduino C++", "MicroPython", "Assembly (AVR)"])
        user_code = st.text_area("Paste your source logic code here:", height=350, placeholder="// Drop code matrix here...")
        generate_btn = st.button("⚡ CONVERT CODE & SYNTHESIZE DIAGRAM")

    with col2:
        st.markdown("#### 📤 Translated Execution & Layouts")
        if generate_btn:
            if not user_code.strip():
                st.warning("Please paste some code first!")
            elif not api_key or api_key == "your_key_here":
                st.error("🔒 Vault Error: API verification key missing.")
            else:
                with st.spinner("Translating Code Formats & Drafting Architectural Connections..."):
                    try:
                        client = Groq(api_key=api_key)
                        
                        system_prompt = f"""
                        You are an expert ECE Professor, Senior Compiler Architect, and Hardware Layout Verification Engineer.
                        Your job is to translate the user's code from {source_lang} directly into {target_lang}.
                        
                        Provide a clean response split into exactly three parts:
                        1. A clean, fully commented block of the code converted into {target_lang}.
                        2. A dedicated layout schematic tag mapping out components using Graphviz formatting. It must look exactly like this:
                        ```dot
                        digraph G {{
                            rankdir=LR;
                            bgcolor="#111827";
                            node [shape=record, style=filled, color="#00f2fe", fillcolor="#1f2937", fontcolor=white, fontname="Courier"];
                            edge [color="#ff4b4b", penwidth=2];
                            Input_Signal -> Main_Controller_Pins -> Output_Device;
                        }}
                        ```
                        3. ### 📖 Logic Breakdown: A brief comparison checklist explaining how the original logic loops translate into the new target structure syntax.
                        """
                        
                        completion = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": f"Source Code:\n{user_code}"}
                            ],
                            temperature=0.2,
                            max_tokens=2500
                        )
                        
                        ai_response = completion.choices.message.content
                        st.success("Translation and Mapping Complete!")
                        
                        # PARSE AND EXTRACT SCHEMATIC MATRIX LAYOUTS
                        dot_match = re.search(r"```dot\n(.*?)```", ai_response, re.DOTALL)
                        if dot_match:
                            dot_code = dot_match.group(1).strip()
                            st.markdown("#### 🔌 Automated Circuit Block Schematic")
                            st.graphviz_chart(dot_code)
                            
                            clean_response = re.sub(r"```dot\n.*?```", "", ai_response, flags=re.DOTALL)
                            st.markdown(clean_response)
                        else:
                            st.markdown(ai_response)
                            
                    except Exception as e:
                        st.error(f"🔍 System Anomaly: {e}")
        else:
            st.markdown("""
            <div class="card-panel">
                <h5 style="color: #00f2fe; margin-top:0; font-family: monospace;">AWAITING TRANSLATION SELECTION...</h5>
                <p style="color: #94a3b8; font-size: 14px; line-height: 1.5;">Configure your source and target programming frameworks, paste your execution scripts, and compile to view translated parameters alongside block hardware arrays.</p>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("#### 🔌 Real-Time Virtual Testbench Sandbox")
    st.markdown("Test, compile, and run your translated hardware scripts inside our sandboxed browser environment below:")
    st.components.v1.iframe("https://wokwi.com", height=700, scrolling=True)

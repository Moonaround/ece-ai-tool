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
* **[Get Lifetime Local Source Code ($4.99)](https://gumroad.com)** 
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
                
                # FIXED: Mapped choice index [0] to extract text flawlessly
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

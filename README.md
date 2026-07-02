# ⚡ ECE AI Circuit Explainer & Testbench Generator

A production-ready Streamlit web application that leverages Llama 3.3 via Groq to instantly decode hardware description languages (Verilog, VHDL) and Arduino scripts. It breaks down complex circuit logic using student-friendly analogies and automatically synthesizes comprehensive simulation testbenches.

## 🚀 Quick Start (Local Setup)

To run this application locally on your machine, follow these steps:

### 1. Clone or Download the Workspace
Extract this bundle into a dedicated folder on your computer.

### 2. Configure Your Environment Keys
Create a file named `.env` in the root folder and add your free Groq API key:
```text
GROQ_API_KEY=gsk_your_private_api_key_here
```

### 3. Initialize an Isolated Environment & Install Tools
Open your terminal inside the project directory and execute:
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the bubble
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt
```

### 4. Fire Up the Server
```bash
streamlit run app.py
```
Your local browser window will automatically open to `http://localhost:8501`.

## 🛠️ Architecture Stack
- **Frontend/UI:** Streamlit (Python-based framework)
- **AI Engine:** Llama-3.3-70b-versatile
- **API Management:** Groq Cloud SDK
- **Environment Rules:** Python-dotenv & PEP 668 isolation compliance

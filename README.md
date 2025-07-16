# Zeru AI Assistant (Mock Version)

This is an offline demo version of the AI chatbot that does **not require any API key**.

## Setup Instructions

### 1. Create virtual environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI backend
```bash
uvicorn main:app --reload
```

### 4. Run the Streamlit frontend
```bash
streamlit run ui_app.py
```

You can now chat with a simple mock AI reply system.
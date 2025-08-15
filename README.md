# GPT-5 Reasoning Chat Helper

A simple and beautiful Streamlit app that lets you interact with GPT-5 model with **reasoning effort** control and **chat history** tracking.

## Features

- **Beautiful UI** using Streamlit with wide layout and sidebar for instructions
- **Reasoning-effort control** (`minimal`, `low`, `medium`, `high`) - choose how much reasoning the model should do before answering
- **Persistent chat history**: entire conversation saved in `st.session_state`; survives page reloads
- **Clear History button**: sidebar button to easily reset chat history

## Screenshot

![Chat UI Screenshot](screenshot.png)

## Installation

```bash
git clone <this-repo-url>
cd <this-repo-directory>

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Linux/Mac:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Setup

Set your OpenAI API key:

```bash
# Option 1: Export as environment variable
export OPENAI_API_KEY="your_api_key_here"

# Option 2: Set in Streamlit secrets
# Add to .streamlit/secrets.toml
```

## Usage

```bash
streamlit run app.py
```

This will open your browser and run the app locally.

## App Flow

1. **Sidebar**: Instructions and "Clear Chat History" button
2. **History Initialization**: Default assistant greeting if no previous messages
3. **Reasoning Effort**: Choose from dropdown (minimal/low/medium/high)
4. **Chat Display**: Messages displayed using `st.chat_message`
5. **User Input**: Type prompt and press Enter
6. **Agent Call**: Uses `ModelSettings(reasoning={'effort': effort})`
7. **Response**: Assistant reply displayed in chat
8. **Reset**: Clear history and rerun app via sidebar button

## Customization Ideas

- Add header images or branding for more attractive UI
- Integrate tools like web search or summarization via Agents SDK
- Implement streaming responses using `Runner.run_streamed()`
- Add logging/tracing for insights on reasoning effort and response times

## Technical Details

This project demonstrates:
- Streamlit UI design
- Agents SDK integration
- State management (chat history)
- Advanced model parameters (reasoning effort)

## Requirements

- Python 3.8+
- Streamlit
- OpenAI Agents SDK
- OpenAI API key

# EIA – Education Insights Agent

An AI-powered academic analytics platform that analyzes student marksheets and provides intelligent insights, visualizations, and AI-driven recommendations using an agent-based AI architecture.

---

## Features

- Upload student marksheets (CSV format)
- Subject-wise and average score analysis
- AI-generated academic insights & recommendations
- Interactive AI follow-up chat
- Supports multiple students per user
- Secure authentication and session management
- Analysis history tracking
- Visual academic performance charts

---

## Tech Stack

### Frontend
- **Streamlit** – Interactive web UI

### Backend / AI
- **Python**
- **Groq API** – LLM-powered insights
- **Agent-based AI architecture**

### Database & Authentication
- **Supabase**
  - User authentication
  - Database storage
  - Row Level Security (RLS)

### Data & Visualization
- **Pandas**
- **Matplotlib / Plotly**

---

## Supabase Integration

Supabase is used for **authentication, data persistence, and session management**.

###  Authentication
- Email & password-based authentication
- Managed via **Supabase Auth**
- User identity is linked across all tables using `user_id`

###  Database Tables

| Table Name | Purpose |
|-----------|--------|
| `users` | Stores user account information |
| `profiles` | User profile details |
| `students` | Student information linked to users |
| `reports` | Uploaded marksheet files & extracted data |
| `analysis_history` | AI-generated academic insights |
| `chat_sessions` | Individual chat sessions |
| `chat_messages` | Chat history per session |

###  Security
- **Row Level Security (RLS)** enabled
- Users can only access **their own data**
- Foreign key relationships enforce data integrity

---

##  Screenshots

![Application Screenshot 1](https://github.com/user-attachments/assets/d16966f6-af45-4a36-8668-47fe136f5140)
![Application Screenshot 2](https://github.com/user-attachments/assets/8183253a-1d53-44c1-899e-94dd0c30aa08)

---

##  Project Structure

This project follows a modular architecture to separate concerns between the UI, AI logic, and database services.

```text
eia/
├── README.md
├── requirements.txt
├── .gitignore
├── .streamlit/
│   └── secrets.toml          # Local API keys (excluded from Git)
└── src/
    ├── main.py               # Application entry point
    ├── agents/               # AI Agent Logic
    │   ├── __init__.py
    │   ├── agent_manager.py  # Routes tasks to specific agents
    │   ├── analysis_agent.py # Academic performance analysis
    │   ├── chat_agent.py     # Follow-up chat logic
    │   └── model_manager.py  # LLM handling & model fallback
    ├── auth/                 # Authentication Services
    │   ├── auth_service.py   # Supabase authentication
    │   └── session_manager.py# User session handling
    ├── components/           # Streamlit UI Components
    │   ├── login.py          # Login/Signup interface
    │   ├── sessions.py       # Session history UI
    │   ├── analysis_form.py  # Data upload form
    │   └── chat_ui.py        # Interactive chat interface
    ├── services/             # External Integrations
    │   └── ai_service.py     # Groq AI API connection
    ├── config/               # App Configurations
    │   └── prompts.py        # System & AI prompts
    └── utils/                # Helper Functions
        ├── charts.py         # Performance visualization logic
        └── validators.py     # Data validation
```

---

##  Architecture Overview

- **Agent Manager** – Orchestrates AI tasks
- **Analysis Agent** – Generates academic insights
- **Chat Agent** – Handles follow-up questions
- **Model Manager** – Selects supported LLM models
- **Supabase** – Stores users, students, reports, chats
- **Streamlit UI** – Connects user actions to backend logic

---

##  Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/eia.git
cd eia
```

### Download Dependencies

```bash
pip install -r requirements.txt
```

### Configure Streamlit Secrets

Create `.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"
GROQ_API_KEY = "your-groq-api-key"
```

### Run the Application

```bash
streamlit run src/main.py
```

---



##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## Contact
 Ashna Hussain 

For questions or support, please open an issue on GitHub.

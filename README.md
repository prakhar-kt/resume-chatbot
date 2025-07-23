# 🤖 Resume Chatbot - Prakhar Srivastava

A modern, interactive AI-powered chatbot that answers questions about Prakhar Srivastava's professional background, experience, and skills. Built with DSPy framework, Claude AI, and a custom web interface.

![Resume Chatbot Demo](https://img.shields.io/badge/Status-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green) ![DSPy](https://img.shields.io/badge/DSPy-AI%20Framework-purple)

## 🌟 Features

- **🧠 AI-Powered Conversations**: Uses Claude 3.5 Sonnet via DSPy framework for intelligent responses
- **📄 Resume Intelligence**: Automatically parses PDF resume and generates comprehensive summaries
- **💬 Modern Web Interface**: Custom-built responsive chat interface (no Gradio dependency)
- **📱 Mobile Responsive**: Works seamlessly across desktop, tablet, and mobile devices
- **⚡ Real-time Chat**: Instant messaging with typing indicators and smooth animations
- **📧 Contact Detection**: Automatically detects and records user contact information
- **🔍 Context Awareness**: Maintains conversation history for natural interactions
- **🛡️ Error Handling**: Robust error handling with graceful fallbacks

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager
- Anthropic API key

### Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:prakhar-kt/resume-chatbot.git
   cd resume-chatbot
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   export ANTHROPIC_API_KEY=your_claude_api_key
   export PUSHOVER_TOKEN=your_pushover_token  # optional
   export PUSHOVER_USER=your_pushover_user    # optional
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8000` and start chatting!

## 🏗️ Architecture

### Technology Stack

- **Backend**: FastAPI + Python
- **AI Framework**: DSPy (Declarative Self-improving Language Programs)
- **LLM**: Anthropic Claude 3.5 Sonnet
- **Frontend**: HTML5 + CSS3 + Vanilla JavaScript
- **PDF Processing**: PyPDF for resume parsing
- **Notifications**: Pushover for contact alerts

### Project Structure

```
├── app.py                 # Main FastAPI application with DSPy implementation
├── run.py                 # Launch script for the web application
├── static/
│   ├── index.html        # Main chat interface
│   ├── style.css         # Styling for the web interface
│   └── script.js         # Chat functionality and API calls
├── selfinfo/
│   ├── ResumePS.pdf      # Resume PDF file
│   └── summary.txt       # Professional summary extracted from resume
├── pyproject.toml        # Project dependencies
├── CLAUDE.md            # Development documentation
└── README.md            # This file
```

### DSPy Framework Implementation

The application leverages DSPy's structured approach to AI interactions:

- **`ResumeChat`**: Main conversation handler with Chain-of-Thought reasoning
- **`ContactDetection`**: Identifies user contact information sharing
- **`KnowledgeCheck`**: Validates question answerability from context
- **`ResumeBot`**: Core module orchestrating all AI interactions

## 🛠️ Development

### Adding New Features

1. **Backend Changes**: Modify `app.py` for API endpoints or DSPy logic
2. **Frontend Updates**: Edit files in `static/` directory
3. **Content Updates**: Update `selfinfo/summary.txt` or replace the PDF

### Environment Setup

```bash
# Activate virtual environment
uv shell

# Install new dependencies
uv add package-name

# Install development dependencies
uv add --dev package-name

# Remove dependencies
uv remove package-name
```

### API Endpoints

- `GET /` - Serves the main chat interface
- `POST /chat` - Handles chat messages and returns AI responses
- `GET /health` - Health check endpoint
- `GET /static/*` - Serves static files (CSS, JS, images)

## 📊 Key Capabilities

### What the Chatbot Can Answer

- **Professional Background**: Career journey, roles, and experience
- **Technical Skills**: AI/ML, data engineering, cloud technologies
- **Projects**: Detailed project descriptions and achievements
- **Education**: Academic background and certifications
- **Contact Information**: How to get in touch
- **Achievements**: Quantified business impact and technical accomplishments

### Smart Features

- **Context Retention**: Remembers conversation history for natural flow
- **Contact Recording**: Automatically captures user email addresses
- **Unknown Question Tracking**: Logs questions that couldn't be answered
- **Professional Tone**: Maintains professional voice throughout conversations

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ANTHROPIC_API_KEY` | Claude API key | Yes |
| `PUSHOVER_TOKEN` | Pushover app token | No |
| `PUSHOVER_USER` | Pushover user key | No |

### Customization

- **Styling**: Edit `static/style.css` for visual customization
- **Content**: Update `selfinfo/summary.txt` and replace the PDF
- **Behavior**: Modify DSPy signatures in `app.py` for different AI behavior

## 🚀 Deployment

### Local Development
```bash
python run.py
```

### Production Deployment
The application is ready for deployment on platforms like:
- **Heroku**: Add `Procfile` with `web: uvicorn app:app --host=0.0.0.0 --port=${PORT:-5000}`
- **Railway**: Direct deployment with auto-detection
- **AWS/GCP**: Container deployment with Docker

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 About

Created by **Prakhar Srivastava** - Senior AI/ML Engineer with 6+ years of experience in building innovative data solutions and production-scale ML systems.

- 🌍 Location: Bengaluru, India
- 💼 LinkedIn: [Connect with me](https://linkedin.com/in/prakhar-srivastava)
- 📝 GitHub: [Follow my work](https://github.com/prakhar-kt)

---

**Try the chatbot live and ask me anything about my professional journey!** 🚀
# 🤖 Resume Chatbot - Prakhar Srivastava

A modern, interactive AI-powered chatbot that answers questions about Prakhar Srivastava's professional background, experience, and skills. Built with DSPy framework, Claude AI, and a custom web interface.

## 🌐 **Live Demo**
**Try it now:** [https://web-production-10596.up.railway.app](https://web-production-10596.up.railway.app)

![Resume Chatbot Demo](https://img.shields.io/badge/Status-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.11+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green) ![DSPy](https://img.shields.io/badge/DSPy-AI%20Framework-purple) ![Claude](https://img.shields.io/badge/Claude-3.5%20Sonnet-orange)

## 🌟 Features

- **🧠 AI-Powered Conversations**: Uses Claude 3.5 Sonnet via DSPy framework for intelligent, structured responses
- **📄 Resume Intelligence**: Automatically parses PDF resume and generates comprehensive summaries
- **💬 Modern Web Interface**: Custom-built responsive chat interface with professional design
- **📱 Mobile Responsive**: Works seamlessly across desktop, tablet, and mobile devices
- **⚡ Real-time Chat**: Instant messaging with typing indicators and smooth animations
- **📧 Smart Contact Detection**: Automatically detects and records user contact information via Pushover
- **🔍 Context Awareness**: Maintains conversation history for natural, flowing interactions
- **🛡️ Robust Error Handling**: Graceful fallbacks and comprehensive error management
- **🚀 Production Ready**: Deployed on Railway with health checks and monitoring

## 🎯 **What Makes This Special**

Unlike traditional static resumes, this chatbot provides:
- **Interactive Experience**: Ask specific questions about experience, skills, or projects
- **Natural Conversations**: Context-aware responses that feel like talking to a real person  
- **Instant Access**: No need to download or read through lengthy documents
- **Professional Presentation**: Clean, modern interface that showcases technical abilities
- **Lead Generation**: Automatic contact capture for networking and opportunities

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

The application leverages DSPy's structured approach to AI interactions, replacing manual prompt engineering with declarative signatures:

- **`ResumeChat`**: Main conversation handler with Chain-of-Thought reasoning for professional responses
- **`ContactDetection`**: Automatically identifies when users share contact information
- **`KnowledgeCheck`**: Validates whether questions can be answered from available context
- **`ResumeBot`**: Core module orchestrating all AI interactions with automatic optimization

**Why DSPy?** Unlike traditional prompt engineering, DSPy provides:
- **Type Safety**: Structured inputs/outputs with automatic validation
- **Optimization**: Automatic prompt improvement based on performance
- **Modularity**: Composable AI components that can be tested and refined
- **Maintainability**: Clear separation of AI logic from application code

## 🛠️ Development


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

### Live Production App
The application is **currently deployed** and running at:
**🌐 [https://web-production-10596.up.railway.app](https://web-production-10596.up.railway.app)**

### Local Development
```bash
python run.py
# or 
python start.py  # with comprehensive debugging
```

### Production Deployment Options
The application supports multiple deployment platforms:
- **✅ Railway** (currently used): Native Python deployment with automatic builds
- **Render**: Free tier available with Docker support
- **Heroku**: Container or buildpack deployment  
- **AWS/GCP**: Container deployment with provided Dockerfiles

### Railway Deployment Features
- **🔄 Auto-deployment**: Pushes to main branch trigger automatic deploys
- **📊 Health monitoring**: Built-in health checks and error tracking
- **🌍 Global CDN**: Fast response times worldwide
- **📈 Scaling**: Automatic scaling based on traffic

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

## 🔗 **Live Links**

- **🌐 Live App**: [https://web-production-10596.up.railway.app](https://web-production-10596.up.railway.app)
- **📂 GitHub**: [https://github.com/prakhar-kt/resume-chatbot](https://github.com/prakhar-kt/resume-chatbot)
- **💼 LinkedIn**: [Connect with Prakhar](https://linkedin.com/in/prakhar-srivastava)

**Try the chatbot live and ask me anything about my professional journey!** 🚀

## 🎉 **Project Highlights**

This project demonstrates:
- **Modern AI Engineering**: Using DSPy for structured LLM interactions
- **Full-Stack Development**: Custom frontend + FastAPI backend
- **DevOps Excellence**: Automated deployment with Railway
- **User Experience**: Professional, interactive resume presentation
- **Technical Innovation**: Moving beyond static PDFs to conversational interfaces

*Built with ❤️ by Prakhar Srivastava*
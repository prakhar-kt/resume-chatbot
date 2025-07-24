# Resume Chatbot - Prakhar Srivastava

An interactive AI chatbot that answers questions about Prakhar Srivastava's professional background, experience, and skills. Built with DSPy framework, Claude 3.5 Sonnet, and FastAPI.

## Live Demo
**Try it:** [https://web-production-10596.up.railway.app](https://web-production-10596.up.railway.app)

![Status](https://img.shields.io/badge/Status-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.11+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green) ![DSPy](https://img.shields.io/badge/DSPy-Framework-purple)

## Features

- **AI-Powered Conversations**: Uses Claude 3.5 Sonnet with DSPy framework for structured responses
- **Resume Intelligence**: Automatically parses PDF resume and generates summaries
- **Web Interface**: Custom responsive chat interface
- **Mobile Responsive**: Works across desktop, tablet, and mobile devices
- **Real-time Chat**: Instant messaging with typing indicators
- **Contact Detection**: Records user contact information via Pushover notifications
- **Context Awareness**: Maintains conversation history for natural interactions
- **Production Ready**: Deployed on Railway with monitoring

## Key Benefits

- Interactive alternative to static resume documents
- Ask specific questions about experience, skills, or projects
- Context-aware responses for natural conversation flow
- Professional presentation showcasing technical capabilities

## Quick Start

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

## Architecture

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
├── start.py               # Production startup script with debugging
├── static/
│   ├── index.html        # Main chat interface
│   ├── style.css         # Styling for the web interface
│   └── script.js         # Chat functionality and API calls
├── selfinfo/
│   ├── ResumePS.pdf      # Resume PDF file
│   └── summary.txt       # Professional summary extracted from resume
├── Dockerfile            # Production Docker image for AWS/GCS
├── Dockerfile.railway    # Railway-specific Docker configuration  
├── docker-compose.yml    # Local development setup
├── pyproject.toml        # Project dependencies
└── README.md            # This file
```

### DSPy Framework Implementation

The application leverages DSPy's structured approach to AI interactions, replacing manual prompt engineering with declarative signatures:

- **`ResumeChat`**: Main conversation handler with Chain-of-Thought reasoning for professional responses
- **`ContactDetection`**: Automatically identifies when users share contact information
- **`KnowledgeCheck`**: Validates whether questions can be answered from available context
- **`ResumeBot`**: Core module orchestrating all AI interactions with automatic optimization

**Why DSPy?** Unlike traditional prompt engineering, DSPy provides:
- Type safety with structured inputs/outputs
- Automatic prompt optimization based on performance
- Modular, composable AI components
- Clear separation of AI logic from application code

## Development


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

## Deployment

### Live Production App
The application is currently deployed at:
[https://web-production-10596.up.railway.app](https://web-production-10596.up.railway.app)

### Local Development
```bash
# For development with debugging
python start.py

# Or using Docker Compose
docker-compose up --build
```

### Production Deployment Options

#### Railway (Currently Used)
Railway uses native Python deployment without Docker:
```bash
# Automatic deployment from GitHub
# Uses railway.json configuration
```

#### AWS Fargate
Deploy using the main Dockerfile:
```bash
# Build and push to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-1.amazonaws.com
docker build -t resume-chatbot .
docker tag resume-chatbot:latest <account>.dkr.ecr.us-east-1.amazonaws.com/resume-chatbot:latest
docker push <account>.dkr.ecr.us-east-1.amazonaws.com/resume-chatbot:latest
```

#### Google Cloud Run
Deploy directly from source:
```bash
gcloud run deploy resume-chatbot \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Railway Deployment Features
- Auto-deployment from main branch
- Built-in health checks and monitoring
- Global CDN for fast response times
- Automatic scaling based on traffic

## Contributing

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

## Links

- **Live App**: [https://web-production-10596.up.railway.app](https://web-production-10596.up.railway.app)
- **GitHub**: [https://github.com/prakhar-kt/resume-chatbot](https://github.com/prakhar-kt/resume-chatbot)
- **LinkedIn**: [Connect with Prakhar](https://linkedin.com/in/prakhar-srivastava)

## Project Highlights

This project demonstrates:
- Modern AI engineering using DSPy for structured LLM interactions
- Full-stack development with custom frontend and FastAPI backend
- Automated deployment and DevOps practices
- Interactive alternative to traditional resume presentation

*Built by Prakhar Srivastava*
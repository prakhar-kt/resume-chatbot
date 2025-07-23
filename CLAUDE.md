# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a resume chatbot project for Prakhar Srivastava, built using DSPy framework with Claude AI backend. The chatbot answers questions about Prakhar's professional background, experience, and skills based on his resume and summary information.

## Development Setup

This project uses **uv** as the Python package manager and **DSPy** with **Claude** for the AI backend. To get started:

```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # or uv shell

# Set up environment variables
export ANTHROPIC_API_KEY=your_claude_api_key
export PUSHOVER_TOKEN=your_pushover_token  # optional
export PUSHOVER_USER=your_pushover_user    # optional

# Run the application
python app.py

# Add new dependencies
uv add <package-name>

# Add development dependencies
uv add --dev <package-name>
```

## Common Commands

### Package Management
- `uv sync` - Install/update all dependencies
- `uv add <package>` - Add a new dependency
- `uv add --dev <package>` - Add a development dependency
- `uv remove <package>` - Remove a dependency
- `uv shell` - Activate the virtual environment

### Development
- `python run.py` - Launch the web application (recommended)
- `python app.py` - Alternative way to launch the FastAPI server
- Access the chatbot at `http://localhost:8000`

### Project Structure
```
├── app.py                 # Main FastAPI application with DSPy implementation
├── run.py                 # Launch script for the web application
├── static/
│   ├── index.html        # Main chat interface
│   ├── style.css         # Styling for the web interface
│   └── script.js         # Chat functionality and API calls
├── selfinfo/
│   ├── ResumePS.pdf      # Prakhar's resume PDF
│   └── summary.txt       # Professional summary extracted from resume
├── pyproject.toml        # Project dependencies
└── CLAUDE.md            # This documentation file
```

## Architecture Notes

### DSPy Framework Implementation

The application uses DSPy (Declarative Self-improving Language Programs) for structured AI interactions:

- **DSPy Signatures**: Defined structured interfaces for different AI tasks
  - `ResumeChat`: Main conversation handler for answering questions about Prakhar Srivastava
  - `ContactDetection`: Detects user contact information sharing
  - `KnowledgeCheck`: Validates if questions can be answered from available context

- **DSPy Modules**: 
  - `ResumeBot`: Main bot module using ChainOfThought for reasoning
  - Automatic prompt optimization capabilities
  - Modular, testable component architecture

### Data Sources

- **Resume PDF**: `selfinfo/ResumePS.pdf` - Contains detailed professional experience
- **Summary**: `selfinfo/summary.txt` - Comprehensive professional summary extracted from resume
- **Context Building**: Combines both sources for comprehensive AI responses

### Key Features

- **Contact Recording**: Automatically detects and records user contact information via Pushover notifications
- **Unknown Question Tracking**: Records questions that cannot be answered from available context
- **Conversation History**: Maintains context across multiple exchanges
- **Error Handling**: Robust error handling with graceful fallbacks

## Recent Changes & Implementation Details

### DSPy Migration (Completed)
- **Migrated from OpenAI to Claude**: Changed backend from OpenAI GPT-4o-mini to Anthropic Claude-3.5-Sonnet
- **DSPy Framework Integration**: Replaced manual prompt engineering with structured DSPy signatures
- **Modular Architecture**: Implemented clean separation of concerns with DSPy modules
- **Code Reduction**: Achieved ~17% reduction in code complexity while improving functionality

### Current Implementation Status
- ✅ **Core Functionality**: Resume Q&A working with Claude backend
- ✅ **Data Sources**: Resume PDF parsing and summary generation completed  
- ✅ **DSPy Integration**: All signatures and modules implemented
- ✅ **Contact Detection**: Automatic email extraction and Pushover notifications
- ✅ **Error Handling**: Robust error handling with graceful degradation
- ✅ **Custom Frontend**: Modern web interface replacing Gradio
- ✅ **FastAPI Backend**: RESTful API with proper request/response handling

### Recent Updates
- **🎉 Custom Frontend**: Replaced Gradio with a professional web interface
- **🚀 FastAPI Backend**: Modern REST API architecture with proper async handling
- **💅 Modern UI**: Responsive design with professional styling and animations
- **⚡ Real-time Chat**: Instant messaging with typing indicators and smooth animations
- **📱 Mobile Responsive**: Works seamlessly on desktop, tablet, and mobile devices

### Important Considerations for Resume Chatbot

- ✅ Resume data properly parsed and structured using PyPDF
- ✅ Secure handling of personal information with environment variables
- ✅ Good conversation flow with DSPy ChainOfThought reasoning
- ✅ Context retention across multiple exchanges
- ✅ Professional summary generated from resume content
- 🔄 Future: Vector search for relevant experience matching
- 🔄 Future: Multiple output formats (conversational, structured data, etc.)
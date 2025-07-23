#!/usr/bin/env python3
"""
Launch script for the Resume Chatbot
Run this to start the web application
"""

import uvicorn
from app import app

if __name__ == "__main__":
    print("🚀 Starting Prakhar Srivastava Resume Chatbot...")
    print("📍 The application will be available at: http://localhost:8000")
    print("🔧 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        reload=False,  # Disable in production
        log_level="info"
    )
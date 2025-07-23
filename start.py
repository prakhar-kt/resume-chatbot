#!/usr/bin/env python3
"""
Startup script for Railway deployment
"""
import os
import sys

def main():
    print("=" * 50)
    print("🚀 Starting Resume Chatbot")
    print(f"Python version: {sys.version}")
    print(f"Working directory: {os.getcwd()}")
    print(f"PORT environment variable: {os.getenv('PORT', 'Not set')}")
    print(f"ANTHROPIC_API_KEY set: {'Yes' if os.getenv('ANTHROPIC_API_KEY') else 'No'}")
    
    print("\nFiles in current directory:")
    try:
        files = os.listdir(".")
        for f in sorted(files):
            print(f"  - {f}")
    except Exception as e:
        print(f"Error listing files: {e}")
    
    print("\nChecking selfinfo directory:")
    try:
        if os.path.exists("selfinfo"):
            selfinfo_files = os.listdir("selfinfo")
            for f in sorted(selfinfo_files):
                print(f"  - selfinfo/{f}")
        else:
            print("  selfinfo directory not found!")
    except Exception as e:
        print(f"Error checking selfinfo: {e}")
    
    print("=" * 50)
    
    # Import and test app initialization
    try:
        print("Testing app import...")
        from app import app
        print("✅ App imported successfully")
        
        # Test that bot can be initialized
        print("Testing bot initialization...")
        from app import Me
        # Don't actually initialize to avoid hanging, just test import
        print("✅ Bot class imported successfully")
        
    except Exception as e:
        print(f"❌ Error importing/testing app: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print("🎯 Starting uvicorn server...")
    return True

if __name__ == "__main__":
    if main():
        import uvicorn
        port = int(os.getenv("PORT", 8000))
        uvicorn.run("app:app", host="0.0.0.0", port=port, log_level="info")
    else:
        print("❌ Startup failed")
        sys.exit(1)
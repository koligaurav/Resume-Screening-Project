#!/usr/bin/env python3
"""
Simple launcher script for the Resume Category Predictor Streamlit app.
This script provides an easy way to start the application with proper error handling.
"""

import subprocess
import sys
import os
import webbrowser
import time

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import streamlit
        import pandas
        import numpy
        import sklearn
        print("✅ All required dependencies are installed.")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install dependencies using: pip install -r requirements.txt")
        return False

def check_model_files():
    """Check if model files exist"""
    required_files = ['tfidf.pkl', 'clf.pkl', 'encoder.pkl']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing model files: {', '.join(missing_files)}")
        print("Please ensure all model files are in the current directory.")
        return False
    
    print("✅ All model files found.")
    return True

def main():
    """Main function to launch the Streamlit app"""
    print("🚀 Resume Category Predictor - Streamlit App Launcher")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check model files
    if not check_model_files():
        sys.exit(1)
    
    print("\n🎯 Starting Streamlit application...")
    print("📱 The app will open in your default web browser.")
    print("🔗 URL: http://localhost:8501")
    print("\n💡 Tips:")
    print("   - Use Ctrl+C to stop the application")
    print("   - The app will automatically reload when you make changes")
    print("   - Check the terminal for any error messages")
    
    try:
        # Start Streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.headless", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user.")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

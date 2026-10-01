"""
VoiceSetu AI Launcher
Runs the FastAPI server and serves the frontend on http://localhost:8000
"""

import uvicorn
import os
import sys

# Ensure d:\projects\VoiceSetu is on sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("=================================================================")
    print(" Starting VoiceSetu AI Server")
    print(" Zero-Prior-Digital-Knowledge Voice Assistant for Rural Indian Women")
    print(" Access Web Interface at: http://localhost:8000")
    print("=================================================================")
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)

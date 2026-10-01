"""
Root ASGI Entrypoint for VoiceSetu AI
Enables running `uvicorn main:app` directly from d:\projects
"""

import sys
import os

# Add VoiceSetu to python search path
base_dir = os.path.dirname(os.path.abspath(__file__))
voicesetu_dir = os.path.join(base_dir, "VoiceSetu")
if voicesetu_dir not in sys.path:
    sys.path.insert(0, voicesetu_dir)

# Import the FastAPI application
# pyrefly: ignore [missing-import]
from backend.main import app

if __name__ == "__main__":
    # pyrefly: ignore [missing-import]
    import uvicorn
    print("=================================================================")
    print(" Starting VoiceSetu AI from root directory")
    print(" Web Interface: http://localhost:8000")
    print("=================================================================")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

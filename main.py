from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI()

# ----------------------------
# Middleware Configuration
# ----------------------------
# Enable CORS to allow requests from the frontend application (e.g., localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend domain
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers (e.g., Content-Type, Authorization)
)

# ----------------------------
# Request Model Definition
# ----------------------------
# Define the expected structure of the incoming JSON payload using Pydantic
class Reflection(BaseModel):
    text: str  # The user's reflection or input text to analyze

# ----------------------------
# Route: Emotion Analysis
# ----------------------------
# Accepts POST requests with user reflection text
# Returns a mock emotional analysis (can be replaced with real ML/AI logic)
@app.post("/analyze")
def analyze_emotion(reflection: Reflection):
    """
    Analyze the submitted reflection and return a mock emotion and confidence score.
    
    Parameters:
        reflection (Reflection): The user's text input.

    Returns:
        dict: Mock analysis result including emotion label and confidence score.
    """
    return {
        "emotion": "Calm",        # Mocked emotion label (replace with ML model output)
        "confidence": 0.87        # Mocked confidence score (0 to 1)
    }

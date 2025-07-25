
# Emotion Reflection Tool – Backend API

This is the backend API for the Emotion Reflection Tool, built with **FastAPI**. It accepts user reflections in text format and returns a mock emotional analysis including emotion type and confidence score.

---

## 🔧 Tech Stack

- **FastAPI** – for building the REST API
- **Pydantic** – for request validation
- **CORS Middleware** – to allow frontend communication
- **Python 3.10+**

---

## 🚀 How to Run the Backend Locally

### 1. Clone the Repository

```bash
git clone https://github.com/saranshjagwani/emotion-reflection-tool-backend.git
cd emotion-reflection-tool-backend
````

### 2. Install Dependencies

Make sure you have Python and pip installed.

```bash
pip install -r requirement.txt
```

### 3. Start the Server

```bash
uvicorn main:app --reload
```

This will run the server on:
`http://localhost:8000`

---

## 📫 API Endpoint

### `POST /analyze`

Accepts a reflection text and returns a mock emotion analysis.

#### Request Body (JSON):

```json
{
  "text": "I feel nervous about my job interview."
}
```

#### Response:

```json
{
  "emotion": "Calm",
  "confidence": 0.87
}
```

---

## 🌐 CORS Configuration

The API is configured to allow requests from all origins (`*`) for testing. You can restrict this in production.

---

## 📁 File Structure

```
main.py                # FastAPI app with /analyze endpoint
requirement.txt        # Python dependencies
README.md              # Project documentation
```

---

## ✅ Status

This is a demo API built as part of a Full Stack Emotion Reflection Tool project. The emotion analysis is mocked and can be integrated with real LLM or ML models in future iterations.

---

## 📄 License

MIT License

```

---

Let me know if you want me to generate the same for frontend or combine both into a single repo doc!
```

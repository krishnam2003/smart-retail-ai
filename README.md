# 🛍️ SmartRetailAI

> An AI-powered smart retail platform that combines **Product Classification, Face Recognition, Sentiment Analysis, and an AI Chatbot** into a unified web application.

SmartRetailAI is a full-stack AI application designed to demonstrate how modern AI and web technologies can be integrated into a retail environment. The platform provides intelligent features for product identification, customer recognition, customer sentiment analysis, and AI-powered assistance.

---

## 🚀 Features

### 📦 Product Classification

* Upload or provide an image of a product.
* AI model analyzes the image.
* Predicts the product category.
* Displays the classification result through the web interface.

### 👤 Face Recognition

* Detects and recognizes faces from images.
* Identifies registered users/customers.
* Useful for personalized retail experiences.

### 😊 Sentiment Analysis

* Analyzes customer reviews or text.
* Determines the sentiment of the input.
* Supports positive, negative, and neutral sentiment classification.
* Helps businesses understand customer feedback.

### 🤖 AI Chatbot

* Interactive AI-powered chatbot.
* Allows users to ask questions and receive intelligent responses.
* Can be extended to provide product-related assistance and customer support.

---

## 🏗️ Project Architecture

```text
                         ┌─────────────────────┐
                         │      User           │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   React Frontend    │
                         │     + Vite          │
                         └──────────┬──────────┘
                                    │
                              HTTP / REST API
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   FastAPI Backend   │
                         └──────────┬──────────┘
                                    │
                ┌───────────────────┼───────────────────┐
                │                   │                   │
                ▼                   ▼                   ▼
        ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
        │   Product    │    │     Face     │    │  Sentiment   │
        │ Classification│   │ Recognition  │    │   Analysis   │
        └──────────────┘    └──────────────┘    └──────────────┘
                                    │
                                    ▼
                            ┌──────────────┐
                            │  AI Chatbot  │
                            └──────────────┘
```

---

## 🛠️ Tech Stack

### Frontend

* **React.js**
* **Vite**
* **JavaScript**
* **HTML5**
* **CSS3**
* REST API integration

### Backend

* **Python**
* **FastAPI**
* **Uvicorn**

### Artificial Intelligence / Machine Learning

* Machine Learning models
* Computer Vision
* Image Classification
* Face Recognition
* Natural Language Processing
* Sentiment Analysis
* Conversational AI

### Development Tools

* Git
* GitHub
* VS Code
* REST APIs

---

## 📁 Project Structure

```text
SmartRetailAI/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── models/
│   │   ├── product_classifier/
│   │   ├── face_recognition/
│   │   └── sentiment_analysis/
│   │
│   ├── routes/
│   ├── services/
│   ├── main.py
│   └── requirements.txt
│
├── README.md
└── .gitignore
```

> The exact folder structure may vary depending on the current implementation.

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/SmartRetailAI.git
cd SmartRetailAI
```

---

# 🎨 Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will generally be available at:

```text
http://localhost:5173
```

---

# 🐍 Backend Setup

Open another terminal and navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The backend will generally run on:

```text
http://127.0.0.1:8000
```

FastAPI documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

# 🔌 API Integration

The React frontend communicates with the FastAPI backend through REST APIs.

Example flow:

```text
User uploads image
        ↓
React frontend
        ↓
HTTP POST request
        ↓
FastAPI endpoint
        ↓
AI/ML model
        ↓
Prediction
        ↓
JSON response
        ↓
React UI
```

Example response:

```json
{
  "success": true,
  "prediction": "Laptop",
  "confidence": 0.94
}
```

---

# 🧠 AI Modules

## 1. Product Classification

The product classification module uses computer vision and machine learning to identify products from images.

### Workflow

```text
Product Image
     ↓
Image Preprocessing
     ↓
ML Model
     ↓
Feature Extraction
     ↓
Classification
     ↓
Predicted Product
```

---

## 2. Face Recognition

The face recognition module detects and identifies faces from an image.

### Workflow

```text
Input Image
     ↓
Face Detection
     ↓
Face Encoding
     ↓
Compare With Stored Encodings
     ↓
Identity Prediction
```

---

## 3. Sentiment Analysis

The sentiment analysis module analyzes customer feedback and determines the overall sentiment.

Example:

```text
Input:
"The product quality is excellent and delivery was very fast."

Output:
Positive
```

Possible classifications:

```text
Positive
Negative
Neutral
```

---

## 4. AI Chatbot

The chatbot provides an interactive conversational interface.

Example:

```text
User:
"Can you recommend a product?"

        ↓

AI Chatbot

        ↓

"Sure! What type of product are you looking for?"
```

The chatbot can be extended with product databases, recommendation systems, RAG, or external LLM APIs.

---

# 🔐 Environment Variables

If the project uses API keys or external AI services, create a `.env` file.

Example:

```env
VITE_API_URL=http://localhost:8000

AI_API_KEY=your_api_key
```

**Never commit `.env` files or API keys to GitHub.**

Add them to `.gitignore`:

```gitignore
.env
.env.*
venv/
__pycache__/
node_modules/
```

---

# 📊 Use Cases

SmartRetailAI can be used for:

* 🛒 Intelligent product identification
* 👥 Personalized customer experiences
* 😊 Customer feedback analysis
* 🤖 AI-powered customer support
* 📦 Automated product categorization
* 🧑‍💼 Retail analytics
* 🎯 Personalized recommendations

---

# 🔮 Future Improvements

The project can be further extended with:

* [ ] Product recommendation system
* [ ] RAG-based product assistant
* [ ] LLM-powered chatbot
* [ ] Customer purchase history
* [ ] Personalized recommendations
* [ ] Product search using natural language
* [ ] Voice-enabled chatbot
* [ ] Real-time camera-based product recognition
* [ ] Admin dashboard
* [ ] Sales analytics
* [ ] Customer behavior analytics
* [ ] Redis caching
* [ ] Docker containerization
* [ ] Cloud deployment
* [ ] Authentication and role-based access

---

# 🐳 Docker Deployment

The application can be containerized using Docker.

Example architecture:

```text
              SmartRetailAI
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
   React Container    FastAPI Container
          │                 │
          └────────┬────────┘
                   │
                   ▼
              AI Models
```

Example commands:

```bash
docker build -t smart-retail-ai .
```

Run:

```bash
docker run -p 8000:8000 smart-retail-ai
```

---

# 📈 Project Highlights

* Full-stack AI application
* React + Vite frontend
* FastAPI backend
* Multiple AI/ML modules
* Computer Vision integration
* NLP-based sentiment analysis
* AI chatbot
* REST API architecture
* Modular AI design
* Scalable architecture for future AI features

---

# 👨‍💻 Author

**Krishnam Singh**

B.Tech – Computer Science & Engineering
VIT Bhopal

---

# ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!

---

## 📄 License

This project is developed for educational and demonstration purposes.

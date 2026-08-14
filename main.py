from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


app = FastAPI(
    title="Career Compass API",
    description="Backend API for career guidance and website navigation.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",
        "http://127.0.0.1:8501",
        "https://pathfinder-compass-83.lovable.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500)


class ChatResponse(BaseModel):
    user_message: str
    bot_reply: str
    category: str
    destination: str
    destination_label: str


CAREERS = [
    {"id": "software-engineering", "name": "Software Engineering", "category": "technical"},
    {"id": "web-development", "name": "Web Development", "category": "technical"},
    {"id": "app-development", "name": "App Development", "category": "technical"},
    {"id": "ai-machine-learning", "name": "AI / Machine Learning", "category": "technical"},
    {"id": "data-science", "name": "Data Science", "category": "technical"},
    {"id": "cybersecurity", "name": "Cybersecurity", "category": "technical"},
    {"id": "cloud-devops", "name": "Cloud / DevOps", "category": "technical"},
    {"id": "ui-ux-design", "name": "UI/UX Design", "category": "technical"},
    {"id": "product-management", "name": "Product Management", "category": "technical"},
    {"id": "entrepreneurship", "name": "Entrepreneurship", "category": "technical"},
    {"id": "communication-practice", "name": "Practice Your Communication", "category": "technical"},
    {"id": "core-engineering", "name": "Core Engineering", "category": "core"},
    {"id": "research-higher-studies", "name": "Research / Higher Studies", "category": "core"},
]


@app.get("/")
def home():
    return {
        "message": "Career Compass API is running",
        "docs": "/docs"
    }


@app.get("/careers")
def get_careers():
    return {"careers": CAREERS}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    message = request.message.lower().strip()

    if any(word in message for word in [
        "web development", "website", "web developer",
        "html", "css", "javascript"
    ]):
        reply = (
            "Web Development is a good path if you enjoy building websites. "
            "Start with HTML, CSS, JavaScript, then create small projects."
        )
        category = "technical"
        destination = "web-development"
        label = "Web Development"

    elif any(word in message for word in [
        "app development", "mobile app", "android", "ios",
        "react native", "kotlin", "swift"
    ]):
        reply = (
            "App Development focuses on mobile experiences. "
            "You can start with React Native, Kotlin for Android, or Swift for iOS."
        )
        category = "technical"
        destination = "app-development"
        label = "App Development"

    elif any(word in message for word in [
        "software engineering", "programming", "software developer",
        "dsa", "git", "java", "python", "c++", "c language"
    ]):
        reply = (
            "Software Engineering could suit you if you enjoy coding and solving problems. "
            "Pick one language, practise data structures, and build projects."
        )
        category = "technical"
        destination = "software-engineering"
        label = "Software Engineering"

    elif any(word in message for word in [
        "machine learning", "artificial intelligence", " ai ", "ml"
    ]):
        reply = (
            "AI and Machine Learning may suit you if you enjoy Python, maths, "
            "patterns, and creating intelligent systems."
        )
        category = "technical"
        destination = "ai-machine-learning"
        label = "AI / Machine Learning"

    elif any(word in message for word in [
        "data science", "data analyst", "data", "analytics", "sql"
    ]):
        reply = (
            "Data Science is about turning data into useful decisions. "
            "Start with Python, statistics, SQL, and simple data projects."
        )
        category = "technical"
        destination = "data-science"
        label = "Data Science"

    elif any(word in message for word in [
        "cybersecurity", "security", "hacking", "networking"
    ]):
        reply = (
            "Cybersecurity focuses on protecting systems and data. "
            "Start with networking, Linux, and security basics."
        )
        category = "technical"
        destination = "cybersecurity"
        label = "Cybersecurity"

    elif any(word in message for word in [
        "cloud", "devops", "docker", "deployment", "ci/cd"
    ]):
        reply = (
            "Cloud and DevOps is a strong path if you enjoy deploying and maintaining software. "
            "Learn Linux, Git, Docker, and cloud fundamentals."
        )
        category = "technical"
        destination = "cloud-devops"
        label = "Cloud / DevOps"

    elif any(word in message for word in [
        "ui", "ux", "design", "figma"
    ]):
        reply = (
            "UI/UX Design may suit you if you enjoy making products clear, useful, and visually appealing. "
            "Start with design basics, Figma, and user research."
        )
        category = "technical"
        destination = "ui-ux-design"
        label = "UI/UX Design"

    elif any(word in message for word in [
        "product management", "product manager", "product"
    ]):
        reply = (
            "Product Management combines user understanding, communication, and decision-making. "
            "Practise user research, prioritisation, and writing product ideas."
        )
        category = "technical"
        destination = "product-management"
        label = "Product Management"

    elif any(word in message for word in [
        "startup", "entrepreneur", "entrepreneurship", "business idea"
    ]):
        reply = (
            "Entrepreneurship is about finding real problems and creating useful solutions. "
            "Start by speaking to people and validating one small idea."
        )
        category = "technical"
        destination = "entrepreneurship"
        label = "Entrepreneurship"

    elif any(word in message for word in [
        "group discussion", "communication", "interview",
        "speaking", "presentation"
    ]):
        reply = (
            "Communication practice will help with group discussions, interviews, "
            "teamwork, and leadership. Regular short practice is the best start."
        )
        category = "technical"
        destination = "communication-practice"
        label = "Practice Your Communication"

    elif any(word in message for word in [
        "gate", "gre", "research", "higher studies", "masters"
    ]):
        reply = (
            "Research and Higher Studies can suit you if you enjoy learning deeply "
            "and exploring a subject in detail."
        )
        category = "core"
        destination = "research-higher-studies"
        label = "Research / Higher Studies"

    elif any(word in message for word in [
        "mechanical", "civil", "electrical", "electronics", "core engineering"
    ]):
        reply = (
            "Core Engineering includes mechanical, civil, electrical, and electronics. "
            "Explore the subjects you enjoy most and try hands-on projects."
        )
        category = "core"
        destination = "core-engineering"
        label = "Core Engineering"

    else:
        reply = (
            "Tell me the subjects you enjoy, your strengths, and the kind of work you prefer. "
            "For example: coding, design, data, speaking, business, or science."
        )
        category = "technical"
        destination = "career-directions"
        label = "Explore Career Directions"

    return {
        "user_message": request.message,
        "bot_reply": reply,
        "category": category,
        "destination": destination,
        "destination_label": label
    }
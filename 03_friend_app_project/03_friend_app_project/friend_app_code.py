import random
from typing import List, Dict, Optional

# --------------------------
# FRIEND App Core Logic
# Built during innovateHER 2025 cohort
# Purpose: Connect students to peers, support and resources
# --------------------------

# Sample reference data
students = [
    {"id": 1, "name": "Alice", "interests": ["study", "party"], "course": "Math", "friend_type": "study partner"},
    {"id": 2, "name": "Bob", "interests": ["church", "party"], "course": "History", "friend_type": "church friend"},
    {"id": 3, "name": "Sicelo", "interests": ["study", "party"], "course": "Math", "friend_type": "party friend"},
    {"id": 4, "name": "Busi", "interests": ["study", "church"], "course": "Physics", "friend_type": "study partner"},
]

counselors = [
    {"id": 1, "name": "Dr. Smith", "type": "psychologist"},
    {"id": 2, "name": "Gog Zulu", "type": "traditional healer"},
]

lecturers = [
    {"id": 1, "name": "Prof. Green", "course": "Math"},
    {"id": 2, "name": "Dr. Madoba", "course": "History"},
]

anonymous_questions = []

# --------------------------
# App Features
# --------------------------

# Match users by interests and connection type
def find_friends(user_id: int, interest: str, friend_type: str) -> List[Dict]:
    return [s for s in students if s["id"] != user_id and interest in s["interests"] and s["friend_type"] == friend_type]

# Book support services
def book_counselor(counselor_type: str) -> Optional[Dict]:
    options = [c for c in counselors if c["type"] == counselor_type]
    return random.choice(options) if options else None

# Send anonymous questions to staff
def ask_lecturer(course: str, question: str):
    lecturer = next((l for l in lecturers if l["course"] == course), None)
    if lecturer:
        anonymous_questions.append({"course": course, "question": question, "lecturer": lecturer["name"]})
        return f"✅ Question sent anonymously to {lecturer['name']}"
    else:
        return "❌ No lecturer found for this course."

# --------------------------
# Test the features
# --------------------------
print("🔍 Find study partners interested in study:", find_friends(1, "study", "study partner"))
print("\n📅 Book a psychologist:", book_counselor("psychologist"))
print("\n📩 Ask lecturer:", ask_lecturer("Math", "What topics will be on the exam?"))
print("\n📋 All anonymous questions:", anonymous_questions)

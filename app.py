from dotenv import load_dotenv
import dspy
import os
import requests
from pypdf import PdfReader
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict
import uvicorn


load_dotenv(override=True)


def push(text):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user": os.getenv("PUSHOVER_USER"),
            "message": text,
        },
    )


def record_user_details(email: str, name: str = "Name not provided", notes: str = "not provided") -> dict:
    """Record that a user is interested in being in touch and provided an email address"""
    push(f"Recording {name} with email {email} and notes {notes}")
    return {"recorded": "ok"}


def record_unknown_question(question: str) -> dict:
    """Record any question that couldn't be answered"""
    push(f"Recording {question}")
    return {"recorded": "ok"}


class ResumeChat(dspy.Signature):
    """Answer questions about Prakhar Srivastava's background professionally as if you are Prakhar Srivastava himself"""
    context = dspy.InputField(desc="Resume and summary information about Prakhar Srivastava")
    question = dspy.InputField(desc="User's question about Prakhar Srivastava")
    answer = dspy.OutputField(desc="Professional response as Prakhar Srivastava, staying in character")

class ContactDetection(dspy.Signature):
    """Detect if user is sharing contact information or if we should ask for it"""
    conversation = dspy.InputField(desc="The conversation context")
    contains_email = dspy.OutputField(desc="yes/no - whether the conversation contains an email address")
    should_ask_contact = dspy.OutputField(desc="yes/no - whether to ask for contact information")

class KnowledgeCheck(dspy.Signature):
    """Check if a question can be answered from the given context"""
    context = dspy.InputField(desc="Available knowledge about Prakhar Srivastava")
    question = dspy.InputField(desc="User's question")
    can_answer = dspy.OutputField(desc="yes/no - whether this question can be answered from the context")


class ResumeBot(dspy.Module):
    
    def __init__(self):
        super().__init__()
        self.chat_predictor = dspy.ChainOfThought(ResumeChat)
        self.contact_detector = dspy.Predict(ContactDetection)
        self.knowledge_checker = dspy.Predict(KnowledgeCheck)
        self.name = "Prakhar Srivastava"
        
        # Load resume data
        reader = PdfReader("selfinfo/ResumePS.pdf")
        self.resume = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                self.resume += text
        
        with open("selfinfo/summary.txt", "r", encoding="utf-8") as f:
            self.summary = f.read()
        
        # Create context for DSPy
        self.context = f"You are Prakhar Srivastava. \
            Be professional and engaging as if talking to a potential \
            client or employer.\n\n## Summary:\n{self.summary}\n\n## Resume:\n{self.resume}"
    
    def forward(self, question: str, conversation_history: str = "") -> str:
        # Check if we can answer the question
        knowledge_check = self.knowledge_checker(
            context=self.context,
            question=question
        )
        
        if knowledge_check.can_answer.lower() == "no":
            record_unknown_question(question)
        
        # Generate response
        result = self.chat_predictor(
            context=self.context,
            question=question
        )
        
        # Check for contact information
        full_conversation = f"{conversation_history}\nUser: {question}\nPrakhar: {result.answer}"
        contact_check = self.contact_detector(conversation=full_conversation)
        
        if contact_check.contains_email.lower() == "yes":
            # Extract email using simple regex-like approach
            import re
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(email_pattern, full_conversation)
            if emails:
                record_user_details(email=emails[0], notes="Extracted from conversation")
        
        return result.answer


class Me:
    def __init__(self):
        # Initialize DSPy with Claude
        lm = dspy.LM(
            model="anthropic/claude-3-5-sonnet-20241022",
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        dspy.settings.configure(lm=lm)
        self.bot = ResumeBot()
    
    def chat(self, message: str, history: List[Dict[str, str]] = None) -> str:
        try:
            # Convert history to string for context
            if history and len(history) > 0:
                conversation_history = "\n".join([
                    f"User: {h.get('user', '')}\nPrakhar: {h.get('bot', '')}"
                    for h in history[-3:]  # Last 3 exchanges
                ])
            else:
                conversation_history = ""
            
            result = self.bot.forward(message, conversation_history)
            return result
            
        except Exception as e:
            print(f"Error in chat: {e}")
            import traceback
            traceback.print_exc()
            return "I apologize, but I encountered an error. Please try again."


# Pydantic models for API
class ChatMessage(BaseModel):
    message: str
    history: List[Dict[str, str]] = []

class ChatResponse(BaseModel):
    response: str
    status: str = "success"

# FastAPI app
app = FastAPI(title="Prakhar Srivastava Resume Chatbot")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize the chatbot
bot_instance = None

@app.on_event("startup")
async def startup_event():
    global bot_instance
    print("Initializing Resume Chatbot...")
    bot_instance = Me()
    print("Resume Chatbot initialized successfully!")

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_data: ChatMessage):
    try:
        if not bot_instance:
            raise HTTPException(status_code=503, detail="Chatbot not initialized")
        
        response = bot_instance.chat(chat_data.message, chat_data.history)
        return ChatResponse(response=response)
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "bot_ready": bot_instance is not None}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

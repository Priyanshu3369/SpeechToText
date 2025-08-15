from fastapi import FastAPI
import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["stt_app"]

@app.get("/ping")
async def ping():
    collections = await db.list_collection_names()
    return {"status": "ok", "collections": collections}

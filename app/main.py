from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI(title="Photo Uploader API")

# Response model for uploads
class UploadResponse(BaseModel):
    key: str
    filename: str
    size: int

# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to the Photo Uploader API! Visit /docs for interactive API docs."}

# Health check
@app.get("/health")
async def health():
    return {"status": "ok"}

# Upload endpoint (local-only, no AWS S3)
@app.post("/upload", response_model=UploadResponse)
async def upload_image(file: UploadFile = File(...)):
    content = await file.read()

    if not content:
        raise HTTPException(status_code=400, detail="Empty file")

    # Generate a fake key instead of uploading to S3
    key = f"uploads/{uuid.uuid4()}_{file.filename}"

    # Just return metadata (no AWS interaction)
    return {"key": key, "filename": file.filename, "size": len(content)}

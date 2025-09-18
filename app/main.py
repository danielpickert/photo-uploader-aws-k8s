from fastapi import FastAPI, UploadFile, File, HTTPException
import boto3
import uuid
import os
from pydantic import BaseModel


app = FastAPI(title="Cloud-Native Showcase API")


S3_BUCKET = os.environ.get("S3_BUCKET")
if not S3_BUCKET:
S3_BUCKET = "example-bucket-placeholder"


s3 = boto3.client("s3")


class UploadResponse(BaseModel):
key: str
filename: str
size: int


@app.get("/health")
async def health():
return {"status": "ok"}


@app.post("/upload", response_model=UploadResponse)
async def upload_image(file: UploadFile = File(...)):
content = await file.read()
if not content:
raise HTTPException(status_code=400, detail="Empty file")
key = f"uploads/{uuid.uuid4()}_{file.filename}"
try:
s3.put_object(Bucket=S3_BUCKET, Key=key, Body=content, ContentType=file.content_type)
except Exception as e:
raise HTTPException(status_code=500, detail=str(e))
return {"key": key, "filename": file.filename, "size": len(content)}
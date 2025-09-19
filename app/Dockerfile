# Use an official lightweight Python image
FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


COPY main.py ./


ENV PORT=8080
EXPOSE ${PORT}

# Run FastAPI with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
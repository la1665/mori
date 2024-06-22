FROM python:3.10-slim

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install  --default-timeout=100 --no-cache-dir --no-deps -r requirements.txt --index-url https://pypi.org/simple

COPY . .

# Run the db main file
RUN python app/db/main.py

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.12.11-alpine3.22

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]
# Dockerfile
FROM python:3.9-slim
FROM ghcr.io/open-webui/open-webui:main

RUN pip install huggingface_hub[hf_xet]
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Expondo porta padrão do Django
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
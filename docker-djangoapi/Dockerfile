# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /api_app
COPY requirements.txt /api_app/
RUN pip install -r requirements.txt
COPY . /api_app/
CMD ["app.py"]

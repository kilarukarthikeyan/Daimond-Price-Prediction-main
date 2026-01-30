FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app

# This forces Python to find the 'src' folder
ENV PYTHONPATH=/app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "application.py"]
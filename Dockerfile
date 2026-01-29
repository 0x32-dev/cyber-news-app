FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt /app/requirements.txt

COPY app.py /app
COPY templates/index.html /app/templates/index.html
COPY static/css/style.css /app/static/css/style.css

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python","app.py"]



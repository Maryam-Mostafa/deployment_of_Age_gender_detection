FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY . .

EXPOSE 5000

CMD ["flask", "run"]

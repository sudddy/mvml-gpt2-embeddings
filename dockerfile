# Use an official Python runtime as a parent image
FROM python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=./app/index.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

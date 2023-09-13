FROM python:latest

WORKDIR /app/
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
CMD ["python", "-u", "/app/main.py"]

FROM python:3.6-slim-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "networkScanner.py", "192.168.0.2", "192.168.0.4"]

FROM python:latest

ADD scanner.py .

CMD ["python3", "scanner.py", "192.168.0.1", "192.168.0.2"]
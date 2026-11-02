FROM python:3.12-slim
WORKDIR /app
COPY gamble.html server.py ./
EXPOSE 6767
CMD ["python3", "server.py", "6767"]

FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
# Run as a non-root user
RUN useradd --create-home appuser
USER appuser
CMD ["python", "-m", "src.main"]

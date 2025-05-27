# 1. Base image
FROM python:3.9-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy code
COPY . .

# 5. Expose port
EXPOSE 5000

# 6. Launch
CMD ["python", "app.py"]

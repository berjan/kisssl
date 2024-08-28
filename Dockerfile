FROM python:3.9

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory
COPY app/ ./app/

# Create data directory and an empty domains.txt file
RUN mkdir -p /app/data && touch /app/data/domains.txt

EXPOSE 80

CMD ["python", "-m", "app.main", "--interactive"]

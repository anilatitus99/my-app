# Use the official Python image.
FROM python:3.9

# Install dependencies.
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy app code
COPY app.py .

# Run the web server
CMD ["python", "app.py"]


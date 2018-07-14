# Select official python 3 runtime
FROM python:3

# Creates a directory in /usr/src/app
RUN mkdir -p /usr/src/app

# Change work directory to it
WORKDIR /usr/src/app

# Copy current directory into the created directory
COPY . /usr/src/app

# Install all dependencies
RUN python -mpip install -r requrinments.txt

# Expose the port
EXPOSE 5000

# Start the application
CMD ["python", "main.py"]

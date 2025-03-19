FROM python:3.9
# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the rest of the application code into the container
COPY . .

# Run the application
CMD ["python", "Mimic_Strategy.py"]

# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home/app

# Copy the script and data files into the container
COPY scripts.py /home/app/
COPY IF.txt /home/data/
COPY AlwaysRememberUsThisWay.txt /home/data/

# Install necessary dependencies (if any)
# RUN pip install --no-cache-dir some_python_package
RUN mkdir -p /home/data/output && chmod -R 777 /home/data

# Run the Python script when the container starts
CMD ["sh", "-c", "python scripts.py && tail -f /dev/null"]


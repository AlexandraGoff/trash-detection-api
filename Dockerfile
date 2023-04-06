# Start from the Python 3.9 image
FROM python:3.9.16-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install required packages for building and running models
RUN apt-get update && apt-get install -y \
    git \
    curl \
    sudo \
    gcc \
    unzip

# Clone the TensorFlow models repository
RUN git clone https://github.com/tensorflow/models.git

# Install the protobuf compiler
RUN PROTOC_ZIP=protoc-3.15.8-linux-x86_64.zip && \
    curl -OL https://github.com/google/protobuf/releases/download/v3.15.8/$PROTOC_ZIP && \
    sudo unzip -o $PROTOC_ZIP -d /usr/local bin/protoc && \
    sudo unzip -o $PROTOC_ZIP -d /usr/local include/* && \
    rm -f $PROTOC_ZIP

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Build the object_detection package
RUN cd models/research \
    && protoc object_detection/protos/*.proto --python_out=. \
    && cp object_detection/packages/tf2/setup.py . \
    && python3 -m pip install .

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 8080

# Define environment variables
ENV FLASK_APP=server.py
ENV FLASK_DEBUG=0
ENV PORT=8080

# Expose port 8080 for the Waitress server
EXPOSE 8080

# Start the Waitress server
CMD ["waitress-serve", "--port=8080", "server:app"]
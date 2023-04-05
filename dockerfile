FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get install -y protobuf-compiler && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/tensorflow/models.git /app/models

RUN cd /app/models/research && \
    protoc object_detection/protos/*.proto --python_out=. && \
    cp object_detection/packages/tf2/setup.py . && \
    python3 -m pip install --use-feature=2020-resolver .

COPY . /app

WORKDIR /app

CMD ["python", "server.py"]
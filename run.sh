#!/bin/bash

IMAGE_NAME="rapidfort-project:latest"
PORT_MAPPING="5000:5000"

docker run -d -p "$PORT_MAPPING" "$IMAGE_NAME"
